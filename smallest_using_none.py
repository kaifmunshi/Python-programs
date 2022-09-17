small=None
for value in [11,22,21,12,1,2,34,5,76]:
    if small is None:
        small=value
    elif value<small:
        small=value
print("smallest number is",small)