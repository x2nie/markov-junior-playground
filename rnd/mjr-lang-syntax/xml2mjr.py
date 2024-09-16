# Author : x2nie
# Date: 2023 Nov 25

import os,re

cwd =  os.path.dirname(__file__)

def xml2mjr(s):
    s = s.replace('<!--','{')
    s = s.replace('-->','}')
    s = re.sub(r'\s+\/>', r'/>', s)
    # s = s.replace('</','# ')
    # s = s.replace('>','):')
    # s = re.sub(r'</(\w+)>', r'#-\1', s)
    s = re.sub(r'</(\w+)>', r'', s)
    s = re.sub(r' comment="([^"]+)"([/>]+)', r'\2 # \1', s)
    s = s.replace('"/>','")')
    s = re.sub(r'<(\w+) ', r'\1 (', s)
    s = s.replace('<','')
    s = s.replace('">','"):')
    s = s.replace('>',':')
    # s = re.sub(r'in="([\w?\*/\|@ ]+)" out="([\w?\*/\|@ ]+)" ', r'\1 -> \2, ', s)
    # s = re.sub(r'in="([\w?\*/\|@ ]+)" out="([\w?\*/\|@ ]+)"', r'\1 -> \2', s)
    s = re.sub(r'in="([^"]+)" out="([^"]+)"', r'\1 -> \2', s)
    s = re.sub(r'"\s(\w+)=', r'", \1=', s)

    return s

if __name__ == '__main__':
    filename = 'BasicKeys'
    # filename = 'BacktrackerCycle'
    # filename = 'BasicBrickWall'
    # filename = 'Apartemazements'
    filename = 'ModernHouse'
    filename = 'Dungeon'
    filename = 'SeaVilla'
    filename = 'MarchingHills'

    with open(os.path.join(cwd,'original', filename +'.xml'), 'r') as f:
        src = f.read()

    result = xml2mjr(src)

    print( result )

    with open(os.path.join(cwd, 'transformed', filename +'.mjr'), 'w') as f:
        f.write(result)
