# markov-junior-playground
MarkovJunior Playground

### Sample syntax:
```python
# BasicKeys.xml
sequence (BDIRGYNOKPFCU, origin=True):
    all (DB* -> *ID) # "draw a grid"

    one (D -> G, limit=1) # "put an end"

    # put a start far from the end
    one: 
        rule (D -> R limit=1)
        field (for="R" from="G" on="RID")
    
    one (RID -> *NO, limit=1)

    # draw a non-optimal path from start to end
    one (temperature=2.0): 
        rule (OID -> YNO)
        rule (OIG -> YNG)
        field (for=O, to=G, on="GIDO")
    
    one (RNY -> KFR, limit=1)

    markov:
        one (UID -> CCU)
        one (RID -> OCU)
        one:
            rule (RNY -> FFR)
            rule (ONY -> FPR)
            rule (RNG -> FFG)
            rule (ONG -> FPG)

    all (CID -> *CC)
    all (I -> B)
```