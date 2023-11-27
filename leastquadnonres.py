def leastquadnonres(p: int):
    residues = set()
    nonresidues = set(range(1,p))
    for i in range(1,p):
        q = i**2
        i = q
        while i - p >= 0:
            i = i - p
        residues.add(i)
        nonresidues.discard(i)
    if nonresidues == set():
        return "There are no quadratic residues for this set."
    else:
        return min(nonresidues)
