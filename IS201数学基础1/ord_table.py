import math
import copy
from Eratoshenes import Eratosthenes,isPrim
from GCD import GCD
from legendre import getFactList
from prettytable import PrettyTable
#-----------------------------------------------------------------------
# 功能开发模块
#获得原根
def get_primitive_root_for_prim(p):

    # 判断模p是否为素数
    if(not isPrim(p)):
        print("false input!")
        return

    #获取p-1素因子q_i
    #q_i=factList[i][0]
    factList=getFactList(p-1)

    for g in range(2,p):

        # flag表示g是否满足原根的式子
        flag=0
        for q in factList:
            tmp=int((p-1)/q[0])
            if(pow(g,tmp)%p==1):
                flag=1
                break
        if(not flag):
            return g

#返回一个列表，[[i,j]],代表i=g^j
def rewrite_num_given_prim(p):
    if(not isPrim(p)):
        print("not prim!")
        return 
    g=get_primitive_root_for_prim(p)
    ls=[]
    # i表示原来的数
    for raw_num in range(1,p):
        #j表示指数
        for ord_num in range(p):
            if(pow(g,ord_num)%p==raw_num):
                ls.append([raw_num,ord_num])
                break
    return ls

def get_ord_table_given_prim(p):
    prim_root=get_primitive_root_for_prim(p)
    change_table=rewrite_num_given_prim(p)
    ord_table=[]
    for element in change_table:
        raw=element[0]
        alpha=element[1]
        #求ord_num,解一次同余式alpha*ord_num\equiv \varphi(p)(mod p)
        ord_num=1
        for num in range(1,p):
            if((alpha*num) %(p-1)==0):
                ord_num=num
                break
        tmp=[raw, ord_num]
        ord_table.append(tmp)
    return ord_table
def print_table(p):
    table=PrettyTable(["a_value","ord"])
    ord_table=get_ord_table_given_prim(p)
    for element in ord_table:
        table.add_row([element[0],element[1]])
    print(table)

def test_primitive_root(root,p):
    factList=getFactList(p-1)
    for q in factList:
        tmp=int((p-1)/q[0])
        if(pow(root,tmp)%p==1):
            return False
    return True



# -----------------------------------------------------------------
# 测试模块
def test_get_root():
    prim_list=Eratosthenes(100)
    for prim in prim_list:
        if(prim==2):
            print("primitive root for 2 does not exist.")
        else:
            print("primitive root for prim number %d is %d" %(prim,get_primitive_root_for_prim(prim)))

def test_rewrite(p):
    ls=rewrite_num_given_prim(p)
    for i in ls:
        print("the substitude ord number for %d is %d" %(i[0],i[1]))
def test_ord_table(p):
    ord_table=get_ord_table_given_prim(p)
    for element in ord_table:
        print("ord for %d is %d" %(element[0],element[1]))


def test_test_primitive(root,p):
    result=test_primitive_root(root,p)
    return result

def test_all_primitive(root,p):
    true_ls=[]
    false_ls=[]
    for i in range(2,p*p):
        if(test_test_primitive(i,p*p)):
            true_ls.append(i)
        else:
            false_ls.append(i)
    print(true_ls)
    print(len(true_ls))
    print(false_ls)
    print(len(false_ls))
# ----------------------------------------------------------

def main():
   p=41
   print_table(p)
if __name__=="__main__":
    main()