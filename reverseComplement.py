def reverse(DNA):
    reverse = []
    for i in DNA:
        if i == "A": 
            reverse.append("T")
        elif i == "G":
            reverse.append("C")
        elif i == "T":
             reverse.append("A")
        else:
            if i == "C":
               reverse.append("G")
    return str(''.join(reverse[::-1])) 