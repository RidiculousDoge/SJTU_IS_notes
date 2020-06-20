import random

def get_random_arr(n):
    arr=[]
    for i in range(n):
        item=random.randint(0,pow(16,4))
        item=hex(item)
        item=item[2:]+'h'
        if(isAlphabet(item[0])):
            i-=1
            continue
        else:
            arr.append(item)
    return arr
def get_random_int_arr(n):
    arr=[]
    for i in range(n):
        item=random.randint(0,pow(16,3))
        arr.append(item)
    return arr

def isAlphabet(ch):
    if(ch in ['a','b','c','d','e','f']):
        return True
    else:
        return False



arr=get_random_int_arr(50)
print(arr)
