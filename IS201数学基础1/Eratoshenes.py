import math
#函数返回不大于n的素数列表
def Eratosthenes(n):
    ls=[]
    if n==3:
        ls.extend([2,3])
    elif n==2:
        ls.append(2)
    else:
        tmp=Eratosthenes(int(math.sqrt(n)))
        ls.extend(tmp)
        for i in range(1,n):
            flag=1
            for p in range(len(tmp)):
                if (i+1)%(tmp[p])==0:     #若i+1被tmp[p]整除
                    flag=0
                    break
            if flag:
                ls.append(i+1)
    return ls
def isPrim(n):
    if(n==2 or n==3):
        return True
    ls=Eratosthenes(int(math.sqrt(n)))
    flag=True
    for i in ls:
        if(n%i==0):
            flag=False
            return flag
        else:
            pass
    return flag
    
if __name__=="__main__":
    n=eval(input("请求输入:"))
    ls=Eratosthenes(n)
    for i in range(len(ls)):
        print(ls[i],end=' ')
        
