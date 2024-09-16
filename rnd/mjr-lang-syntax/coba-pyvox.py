import os
from sty import fg,bg, rs
from pyvox.parser import VoxParser, Vox, ParsingException, Chunk
# from pyvox 
# from pyvox.writer import VoxWriter

class MyVoxParser(VoxParser):


    def _parseChunk(self):

        _id, N, M = self.unpack('4sii')

        # log.debug("Found chunk id %s / len %s / children %s", _id, N, M)

        content = self.unpack('%ds'%N)[0]

        start = self.offset
        chunks = [ ]
        while self.offset<start+M:
            chunks.append(self._parseChunk())

        return Chunk(_id, content, chunks)

    def parse(self):

            header, version = self.unpack('4si')
            if header != b'VOX ': raise ParsingException("This doesn't look like a vox file to me")
            if version != 150: raise ParsingException("Unknown vox version: %s expected 150"%version)
            main = self._parseChunk()

            palette = None
            model_count = 1
            # size =  None
            # xyzi = None
            pres = []
            materials = []

            for chunk in main.chunks:
                # print(chunk.id)
                if chunk.id == b'PACK':
                    model_count = chunk.models
                elif chunk.id == b'RGBA':
                    palette = chunk.palette
                elif chunk.id == b'SIZE':
                    pres.append([chunk])
                elif chunk.id == b'XYZI':
                    pres[-1].append(chunk)
                # elif chunk.id == b'MATL':
                #     materials.append(chunk.material)

            models = [ self._parseModel(m[0], m[1]) for m in pres ]

            return Vox(models, palette, materials)

cwd = os.path.dirname(__file__)

# m1 = VoxParser(os.path.join(cwd, 'original', 'Wall.vox')).parse()
# m1 = VoxParser(os.path.join(cwd, 'original', '3x3x3.vox')).parse()
m1 = MyVoxParser(os.path.join(cwd, 'original', 'Wall.vox')).parse()
m1 = MyVoxParser(os.path.join(cwd, 'original', 'In.vox')).parse()

print(m1)

pal = m1.palette
print('default-pal=', m1.default_palette)
# print('pal:', pal)
for c in pal:
    color =  bg(c.r, c.g, c.b)
    print(color+'  '+ bg.rs, end=' ')
print('<')

for i,m in enumerate(m1.models):
    print('model:#',i)
    s = m.size
    print('Size:', s.x, s.y, s.z)
    print('voxel.count:', len(m.voxels))
    for v in m.voxels:
        c = pal[v.c]
        color =  bg(c.r, c.g, c.b)
        print(v.x, v.y, v.z, v.c, color+'  '+ bg.rs, '#%02x%02x%02x' % (c.r, c.g, c.b), c)
