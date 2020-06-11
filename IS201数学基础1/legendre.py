# 化简legendre符号(\frac{a}{p})
# 利用公式：
#   1. (\frac{1}{p})=1
#   2. (\frac{2}{p})=(-1)^{\frac{p^2-1}{8}}
#   3. 周期性等三条性质
#   4. 二次互反律

import math
import copy
from Eratoshenes import Eratosthenes,isPrim
from GCD import GCD

# 获得因数分解式：以广义表形式返回[[x,y],[a,b]]
# x,a表示素因子，y,b表示该素因子对应指数

def getFactList(x):
    # 剔除错误输入
    if (x<=2 or x!=int(x)):
        return []

    factor_list=[]
    # 判定为素数
    if(isPrim(x)):
        factor_list.append([x,1])
        return factor_list

    # 一般情况
    # 可能的素数列表
    prim_list=Eratosthenes(x)
    for i in prim_list:
        j=1
        flag=False
        while(x%math.pow(i,j)==0):
            j+=1
            flag=True
        if(flag):
            factor_list.append([i,j-1])
    return factor_list

def isEven(a):  # 判断是否为偶数
    if(a%2==0):
        return True
    else:
        return False
    
def lengdre(a,b):    #化简(\frac{a}{b})
    # 排除错误输入,特别注意b必须为素数
    if(a<0 or b<0 or int(a)!=a or int(b)!=b):
        print("false input!")
        return 0

    # 以下情形a都为素数
    # 若a=1，则lengdre(a,b)=1
    if(a==1):
        return 1
    if(a==b):
        return 0

    # 化简
    # 利用周期性
    if(a>b):
        # 把周期去掉
        return lengdre(a%b,b)

    # a<b的情况下
    # 1.a=2
    if(a==2):
        if(b%8==1 or b%8==-1):
            return 1
        else:
            return -1
    # 把a化成素数的积
    if(not isPrim(a)):
        fact=getFactList(a)
        result=1
        for i in range(len(fact)):
            if(fact[i][1]%2==0):
                pass
            else:
                result*=lengdre(fact[i][0],b)
        return result
    # 2. 利用二次互反律(\frac{p}{q}=(-1)^{((p-1)/2)*(q-1)/2})(\frac{q}{p})
    # sig表示符号
    # 不要用(-1)的乘方形式，太耗算力
    tmp=int((a-1)/2)*int((b-1)/2)
    if(isEven(tmp)):
        sig=1
    else:
        sig=-1
    return sig*lengdre(b,a)

def main():
    #print(getFactList(10))
    #print(isPrim(7))
    #print(lengdre(79,pow(2,10)-1))
    #print( not isPrim(41))
    p=pow(2,192)-pow(2,64)+32+16-1
    is_ls=[]
    not_ls=[]
    for i in range(101,201):
        if(lengdre(i,p)==1):
            is_ls.append(i)
        else:
            not_ls.append(i)
    print("是模%d平方剩余的数有"%(p),end=" ")
    print(is_ls)
    print('--------------------------------------------------------------------')
    print("是模%d平方非剩余的数有"%(p),end=" ")
    print(not_ls)

if __name__=='__main__':
    main()

