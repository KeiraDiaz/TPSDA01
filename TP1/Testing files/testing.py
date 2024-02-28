def bitstr(a):
    if a == 0:
        return 0
    if a == 1:
        return 0
    if a == 2:
        return 1
    if a == 3:
        return 4
    else:
        return 2*bitstr(a-1) + bitstr(a-2)    
print(bitstr(4))