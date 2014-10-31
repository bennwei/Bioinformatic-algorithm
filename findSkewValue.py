def findSkewValue(dna):
    skew_value = 0
    skew_list = []
    
    for n in dna:
        
        if n == 'C':
            skew_value -= 1
            skew_list.append(skew_value)
        elif n == 'G':
            skew_value += 1
            skew_list.append(skew_value)
        else:
            skew_value += 0
            skew_list.append(skew_value)
    
    for i in skew_list: 
         l = ' '.join(map(str, skew_list))
    
             
    