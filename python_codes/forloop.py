mylist = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def even_odd():
    for _ in mylist:
        if _ % 2 == 0:
            print(_)
        else:
            print(f'Odd Number: {_}')


even_odd()
