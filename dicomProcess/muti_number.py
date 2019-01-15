N = raw_input("please input n")
n_p = raw_input("please input n numbers split with space")
M = raw_input('please input m')
list_p = []
for p in range(int(N)):
    list_p.append(int(n_p.split(' ')[p]))
    
list1 = []
def sumOfkNumber1(sum, n, m, list_p):
    if n <= 0 or sum <= 0:
        return
    if sum == m:
        list1.reverse()
        if list1 == []:
            print '0'
            return 0
        else:
            print n, " + ", " + ".join(str(x) for x in list1)
            return 1
        list1.reverse()
    list1.append(list_p[n-1])
    sumOfkNumber1(sum - list_p[n-1], n-1, m, list_p) #
    list1.pop()
    sumOfkNumber1(sum, n-1, m, list_p)

if __name__ == '__main__':
    sumOfkNumber1(0, N, M, list_p)