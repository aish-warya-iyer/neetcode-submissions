def add_two_numbers() -> int:
    l = []
    inp = (input(""))
    inp_sep = inp.split(",")
    for i in inp_sep:
        l.append(int(i))
    return l[0]+l[1]



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
