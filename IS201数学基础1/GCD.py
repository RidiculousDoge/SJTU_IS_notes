#利用辗转相除法求最大公因数

import math
def GCD(a,b):
    high=max(abs(a),abs(b))
    low=min(abs(a),abs(b))
    c=high%low
    if (c==0):
        return low
    else:
        return GCD(c,low)
        
'''
def main():
    while(1):
        str=(input("Please enter: "))
        a,b=str.split()
        a=eval(a)
        b=eval(b)
        print(GCD(a,b))

main()
'''