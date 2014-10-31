def Matching(pattern, seq):
    match = []
    l = len(seq)-len(pattern)
    for i in range(0, l):
        if seq[i : (i+len(pattern))] == pattern:
            match.append(i)
    return ' '.join(map(str, match))