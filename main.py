#张淑唯 信息1701
#右上三角格式输出九九乘法表
for i in range(1,10):
    for k in range(1,i):
        print (end="       ")
    for j in range(i,10):
            print("%dx%d=%2d" % (i,j,i*j),end=" ")
    print()
