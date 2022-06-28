def palin(v):
    if len(v) < 1:
        return True
    else:
        if v[0] == v[-1]:
            return palin(v[1:-1])
        else:
            return False

a = input()
if(palin(a)):
    print("True")
else:
    print("False")