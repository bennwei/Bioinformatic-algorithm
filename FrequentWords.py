def PatternCount(Text, Pattern):
    count = 0
    k = len(Text)-len(Pattern)
    for i in range(0, k):
        if Text[i : (i+len(Pattern))] == Pattern:
            count += 1
    return count
    
def FrequentWords(DNA, k):
    FrequentPatterns = []
    for i in range(0, (len(DNA)+1-k)):
        Pattern = DNA[i, i+k]
        count = PatternCount(DNA, Pattern)
    maxCount = max(count)
    for i in range(len(k)+1-k):
        if count == maxCount:
            FrequentPatterns.append(Pattern)
    return FrequentPatterns
        