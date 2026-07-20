from typing import List

def read_integers() -> List[int]:
    l = []
    inp = (input(""))
    inp_sep = inp.split(",")
    for i in inp_sep:

        l.append(int(i))
    return l

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
