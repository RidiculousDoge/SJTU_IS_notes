# 选择[[a,b],[c,d]]广义表数据结构
# a,c表示次数，b,d表示系数
# 如f(x)=x^2+2x表示成[[2,1],[1,2]]

# 算法简化相当相当相当重要!!

# ** ATTENTION!! 每次提升的时候都要对原多项式对现在提升的模p^i 重新取简化式！！ **
import math
# copy模块可以解决参数引用传值的问题
import copy
from GCD import GCD


def getAdv(p, a):    # 关于模p,a*a^{-1}\equiv 1 (mod p),逆元唯一
    if(p <= 1 or a < 1 or p != int(p) or a != int(a)):
        print("error")
        return 0
    else:
        for i in range(1, p+1):
            if(a*i % p == 1):
                return i


class Poly:
    def __init__(self, outPoly):
        self.poly = outPoly
        self.normalize()

    def display(self):
        if(self.poly == [[0, 0]]):
            print("f(x)=0")
            return
        sentence = "f(x)="
        for i in range(len(self.poly)-1):
            degree = self.poly[i][0]
            param = self.poly[i][1]
            if(param == 1):
                sentence += "x^"+str(degree)+"+"
            elif(param < 0):
                sentence += "("+str(param)+")x^"+str(degree)+"+"
            else:
                sentence += str(param)+"x^"+str(degree)+"+"
        cur = len(self.poly)-1
        degree = self.poly[cur][0]
        param = self.poly[cur][1]
        if(param == 1):
            sentence += "x^"+str(degree)
        elif(param < 0):
            sentence += "("+str(param)+")x^"+str(degree)
        else:
            sentence += str(param)+"x^"+str(degree)

        print(sentence)

    def normalize(self):
        # 规范化

        # 第一步删除所有系数为0的项
        length = len(self.poly)
        i = 0
        while(i < length):
            if(self.poly[i][1] == 0):
                del self.poly[i]
                length -= 1
                continue
            else:
                i += 1
        if(self.poly == []):
            self.poly = [[0, 0]]
        # 第二步整理，看看有没有degree重复的项，整合加在一起
        i = 0
        j = 1
        while(i < length):
            while(j < length):
                if(self.poly[i][0] == self.poly[j][0]):
                    self.poly[i][1] += self.poly[j][1]
                    del self.poly[j]
                    length += -1
                else:
                    j += 1
            i += 1
            j = i+1

        # 第二步排成降序
        for i in range(len(self.poly)):
            for j in range(i+1, len(self.poly)):
                if(self.poly[i][0] < self.poly[j][0]):  # 交换
                    tmp = self.poly[j]
                    self.poly[j] = self.poly[i]
                    self.poly[i] = tmp
                else:
                    pass
        self.degree = self.poly[0][0]

    def getPoly(self):
        return self.poly

    def compute(self, x):    # 计算f(x)
        result = 0
        for i in range(len(self.poly)):
            result += self.poly[i][1]*pow(x, self.poly[i][0])
        return result

    def getSolForP(self, p):   # 计算满足p|f(x)对应的x
        simp = getSimp(self, p)
        result = []
        for i in range(p):
            if(simp.compute(i) % p == 0):
                result.append(i)
        return result


# 调用一次getMinus()会修改传入参数的值，待修改
def getMinus(Otherpoly):
    tmp = copy.deepcopy(Otherpoly.getPoly())
    tmp_obj = Poly(tmp)
    for i in range(len(tmp_obj.poly)):
        tmp_obj.poly[i][1] = -tmp_obj.poly[i][1]
    tmp_obj.normalize()
    return tmp_obj

# 多项式加法


def polynomiaAdd(poly1, poly2):
    result = []
    for i in range(len(poly1.poly)):
        flag = False          # 表示在i给定的时候对于j跑一个周期是否找到相同次数项
        for j in range(len(poly2.poly)):
            # 如果相同次数
            if(poly1.poly[i][0] == poly2.poly[j][0]):
                flag = True
                degree = poly1.poly[i][0]
                param = poly1.poly[i][1]+poly2.poly[j][1]
                tmp = []
                tmp.append(degree)
                tmp.append(param)
                result.append(tmp)
            else:
                continue
        j = 0
        if(flag == False):
            result.append(poly1.poly[i])
    for i in range(len(poly2.poly)):
        flag = False
        for j in range(len(poly1.poly)):
            if(poly2.poly[i][0] == poly1.poly[j][0]):
                flag = True
                break
        if(flag == False):
            result.append(poly2.poly[i])
    resultPoly = Poly(result)
    return resultPoly

# 多项式减法


def polynomiaSub(poly1, poly2):  # poly1-poly2
    tmp = getMinus(poly2)
    return polynomiaAdd(poly1, tmp)


def polynomiaMulti(poly1, poly2):  # poly1*poly2
    result = []
    for i in range(len(poly1.poly)):
        for j in range(len(poly2.poly)):
            param = poly1.poly[i][1]*poly2.poly[j][1]
            degree = poly1.poly[i][0]+poly2.poly[j][0]
            tmp = []
            tmp.append(degree)
            tmp.append(param)
            result.append(tmp)
    return Poly(result)
# 利用递归写出多项式除法


def polynomialDiv(poly1, poly2):   # 记录poly1/poly2,poly1,poly2是类的两个实例化
    q = []        # 保存商式
    r = []        # 保存余式
    if (poly2.degree > poly1.degree):
        q.append([0, 0])
        r = copy.deepcopy(poly1.getPoly())
    else:
        # 类似于除法的中间结果
        param = poly1.poly[0][1]/poly2.poly[0][1]
        degree = poly1.degree-poly2.degree
        tmp = []
        tmp.append(degree)
        tmp.append(param)
        q.append(tmp)
        poly_tmp_q = Poly(q)            # 一位数的结果
        poly_to_sub = polynomiaMulti(poly_tmp_q, poly2)
        poly_to_rediv = polynomiaSub(poly1, poly_to_sub)
        q_rest_poly, r_rest_poly = polynomialDiv(poly_to_rediv, poly2)
        r = r_rest_poly.poly
        q.extend(q_rest_poly.poly)
    return Poly(q), Poly(r)


def getDerivative(outerPoly):   # 获得导式f'(x)
    tmp = copy.deepcopy(outerPoly.poly)
    for i in range(len(tmp)):
        tmp[i][1] *= tmp[i][0]
        tmp[i][0] -= 1
    tmp_obj = Poly(tmp)
    return tmp_obj

# ------------------------------------------------------------------------------------
# 这俩函数有时间再重构8···
# 这俩内容还不太一样 佛了


def getSimp(poly1, p):   # 关于模p，利用x^{t+k(p-1)}\equiv x^t(mod p)化简得到最简多项式形式
    # 剔除p<=1或者p不为整数的情况
    if(p <= 1 or int(p) != p):
        return None
    # 剔除不良输入：如果存在负指数，返回None
    tmp = copy.deepcopy(poly1.poly)
    for i in range(len(tmp)):
        if(tmp[i][0] < 0):
            print("该多项式无法获取最简形式！")
            return None
    # 处理指数
    if(tmp[0][0] < p):
        pass
    else:
        for i in range(len(tmp)):
            # x^{t+k(p-1)}\equiv x^t(mod p)只在k,t为正整数时才恒成立。需要排除掉t=0的情况
            # 其实t=0就是回到了欧拉定理的情形。欧拉定理需要满足底数和模互素才可以，即(x,p)=1
            if(tmp[i][0] == p-1):
                pass
            else:
                tmp[i][0] = tmp[i][0] % (p-1)
    # 必须要在处理完指数以后实例化tmp,不然处理完系数以后再normalize还是要处理系数
    tmp_obj = Poly(tmp)
    # 处理系数
    for i in range(len(tmp)):
        tmp_obj.poly[i][1] = tmp_obj.poly[i][1] % p
    tmp_obj.normalize()
    return tmp_obj


def getSimp_two_params(poly1, p, q):    # 指数对着p简化，系数对着q简化
    # 剔除输入错误
    if (p <= 1 or int(p) != p or q <= 1 or int(q) != q):
        return None
    # 剔除不良输入：如果存在负指数，返回None
    tmp = copy.deepcopy(poly1.poly)
    for i in range(len(tmp)):
        if(tmp[i][0] < 0):
            print("该多项式无法获取最简形式！")
            return None
    # 处理指数
    if(tmp[0][0] < p):
        pass
    else:
        for i in range(len(tmp)):
            tmp[i][0] = tmp[i][0] % p
    # 必须要在处理完指数以后实例化tmp,不然处理完系数以后再normalize还是要处理系数
    tmp_obj = Poly(tmp)
    # 处理系数
    for i in range(len(tmp)):
        tmp_obj.poly[i][1] = tmp_obj.poly[i][1] % q
    tmp_obj.normalize()
    return tmp_obj
# -------------------------------------------------------------------------------------------------------


def get_avai_x_1_list(outerPoly, p):        # 筛选有效的x_1
    x_1_list = outerPoly.getSolForP(p)
    SimpDerPoly = getSimp(getDerivative(outerPoly), p)  # 取导式以后简化
    # 筛选：如果(f'(x_1),p)=1 才可以提升
    i = 0
    length = len(x_1_list)
    while(i < length):
        x_cur = x_1_list[i]
        y = SimpDerPoly.compute(x_cur)                # 计算f'(x_1)
        if(GCD(y, p) != 1):
            del x_1_list[i]
            length -= 1
        else:
            i += 1
    return x_1_list


def get_single_x_1_list(outerPoly, x1, p, alpha):
    # 导式的简化形式不变
    der_poly = getDerivative(outerPoly)       # f'(x)
    der_poly_simp = getSimp(der_poly, p)       # f'(x)等价形式g(x)
    der_poly_simp_x1 = der_poly_simp.compute(x1)      # g(x1)
    # 简化计算！
    der_poly_simp_x1 = der_poly_simp_x1 % p             # g(x1)\equiv p
    # 准备循环变量
    x_cur = x1
    t_cur = 0

    # 准备存储空间
    x_list = []
    t_list = []
    x_list.append(x1)

    # 执行循环
    for i in range(2, alpha+1):      # i=2,3,...alpha, 跟书上对齐
        p_cur = pow(p, i)              # 当前的有效模
        # 根据欧拉定理，由于p是素数，所以x_1必与p互素，从而有x_1^{\varphi(p)}\equiv 1(mod p_cur)
        # 而\varPhi(p^i)=p^i-p^{i-1}
        # 所以对f(x)对模p_cur的简化可以从算法上优化成：
        # f(x)的指数对p_varPhi简化，f(x)的系数对p_cur简化
        p_varPhi = p_cur-pow(p, i-1)
        poly_cur = getSimp_two_params(outerPoly, p_varPhi, p_cur)   # f(x)的简化式
        poly_cur.display()
        # 计算t_cur

        # 这部分处理很重要的一点就是要随时去掉多余部分，简化算法！
        a = (poly_cur.compute(x_cur)) % p_cur
        for t in range(1, p+1):
            if((a+t*der_poly_simp_x1*pow(p, i-1)) % pow(p, i) == 0):
                t_cur = t
                t_list.append(t_cur)
                break
        # 计算x_cur
        x_cur = (x_cur+t_cur*pow(p, i-1)) % p_cur
        x_list.append(x_cur)
    return x_list, t_list


def main():
    outerP1 = [[20150514, 3], [201505, 1], [2015, 1], [2, 1], [0, 1]]
    outerP2 = [[20140515, 20140515], [201405, 201495], [
        2014, 2014], [8, 8], [6, 1], [3, 4], [1, 1], [0, 1]]
    poly1 = Poly(outerP1)
    poly2 = Poly(outerP2)

    # 取导式以后简化跟简化后取导式不同!
    x_list, t_list = get_single_x_1_list(poly1, 3, 7, 3)
    print(x_list)
    print(t_list)
    M_1 = getAdv(99, 100*101)
    M_2 = getAdv(100, 99*101)
    M_3 = getAdv(101, 99*100)
    print('%d,%d,%d' % (M_1, M_2, M_3))


if __name__ == '__main__':
    main()
