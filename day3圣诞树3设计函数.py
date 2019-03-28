def tree(n, h, a):
    for i in range(n):
        print(" "*(n-i)+a*(i*2-1))
    for j in range(1,h+1):
        print(" "*(n-1)+"|")
tree(5,3,'*')