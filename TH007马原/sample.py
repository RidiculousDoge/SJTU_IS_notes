import random

def create(fn, encoding="utf-8"):
    fp = open(fn, "r", encoding=encoding)
    lines = fp.readlines()
    probs = []
    curr = []
    for l in lines:
        s = l[0]
        if ord("0") <= ord(s) <= ord("9"):
            if curr:
                probs.append(curr)
            p = a = ""
            for c in l:
                if ord("A") <= ord(c) <= ord("E"):
                    a += c
                else:
                    p += c
            curr = [[p, a]]
        elif ord("A") <= ord(s) <= ord("E"):
            curr.append(l)
    return probs
    
def main():
    probs = create("base.txt")
    WrongList=[]
    correct=0
    wrong=0
    overall=0
    random.shuffle(probs)
    for p in probs:
        a = p[0][1]
        print(p[0][0])
        for n in p[1:]:
            print(n)
        answer=input("输入答案 ")
        print("答案：", a)
        if(answer==a):
            correct+=1
        else:
            wrong+=1
            WrongList.append(p)
        overall+=1
        q=eval(input("输入0以继续，1以结束\n"))
        if(q):
            break
    for p in WrongList:
        a = p[0][1]
        print(p[0][0])
        for n in p[1:]:
            print(n)
        input("输入答案 ")
        print("答案：", a)
        input("回车以继续...\n")
    print("正确率是",correct/overall)


    
        
if __name__ == "__main__":
    main()
