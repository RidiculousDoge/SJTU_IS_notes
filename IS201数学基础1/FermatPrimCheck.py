import math
import copy
import random
from Eratoshenes import Eratosthenes,isPrim
from GCD import GCD
from legendre import getFactList

# times marks the time we repeat the check
def FermatCheck(item_to_check,times=30):
    random_list=[]
    for i in range(times):
        random_list.append(random.randint(1,100))
    
    for i in range(times):
        r=pow(random_list[i],item_to_check-1)%item_to_check
        if(r==1):
            continue
        else:
            return False
    # probability of false discrimination lower than 2^{-30}
    return True

def get_random_prim(left_bound,right_bound):
    prim2check=random.randint(left_bound,right_bound)
    while(not FermatCheck(prim2check)):
        prim2check=random.randint(left_bound,right_bound)
    return prim2check

def main():
    print(get_random_prim(pow(2,12),pow(2,13)))

if __name__=='__main__':
    main()
         