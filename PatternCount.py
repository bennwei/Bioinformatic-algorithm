import timeit
def patternCount(Text, Pattern):
    """Count the requency of a pattern in a DNA seqeunce.
    >>>patternCount("ACAACTATGCATACTATCGGGAACTATCCT"," ACTAT")
    3
    
    """
    start_time = timeit.default_timer()
    count = 0
    k = len(Text)-len(Pattern)
    for i in range(0, k):
        if Text[i : (i+len(Pattern))] == Pattern:
            count += 1
    return count
    stop_time = timeit.default_timer()
    print str(stop_time - start_time) + " sec" 

