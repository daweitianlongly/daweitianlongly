#九九乘法表
for i in range(1,10):#范围在1，2，3，4，5，6，7，8，9
    for j in range (1,i):
        print("\t",end="")
    for k in range (i,10):
        print("%dx%d=%d" % (i,k,k*i), end="\t")
    print()
#九九乘法表逆时针输出
for i in range(9,0,-1):
    for j in range (1,i):
        print("\t",end="")
    for k in range (i,10):
        print("%dx%d=%d" % (i,k,k*i), end="\t")
    print()


# 一个四位数 abcd，满足 abcd * 4 = dcba，求这个数
for i in range(1000,9999):
        a = i//1000
        b = i%1000//100
        c = i%1000%100//10
        d = i%1000%100%10
        if i*4 == d*1000+c*100+b*10+a:
           print(i,i,'*',4,'=',d*1000+c*100+b*10+a)




