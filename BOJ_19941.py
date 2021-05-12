n, k = list(map(int,input().split()))
tables = input()
#20 2
#HHPHPPHHPPHPPPHPHPHP
checkList = [False]*n
result = 0
for i in range(n):
    if checkList[i] != True:

        if tables[i] == 'H':
            for j in range(i-k,i+k+1):

                if j < 0 or j >= n:
                    continue
                if checkList[j] == False and tables[j] == 'P':
                    #i는 H
                    checkList[i] = True
                    result += 1
                    #j는 P
                    checkList[j] = True
                    break
        if tables[i] == 'P':
            for m in range(i-k,i+k+1):

                if m < 0 or m >= n:
                    continue
                if checkList[m] == False and tables[m] == 'H':
                    #i는 P
                    checkList[i] = True
                    #i는 H
                    checkList[m] = True
                    result += 1
                    break
print(result)



