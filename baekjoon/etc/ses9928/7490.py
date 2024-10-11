from collections import deque

def main():
    testcount = int(input())
    testnum = []
    for i in range(testcount):
        testnum.append(int(input()))
    answer = []
    for i in testnum:
        logics = buildgraph(i)
        tempnum = 1
        temp = '1'
        for j in logics:
            for k in j:
                tempnum += 1
                temp += str(k)
                temp += str(tempnum)
            calcul = temp.replace(' ','')
            if eval(calcul) == 0:
                answer.append(temp)
            temp = '1'
            tempnum = 1
        answer.append('')
    for i in range(len(answer)-1):
        print(answer[i])

def buildgraph(n):
    result = [['+'],['-'],[' ']]

    for i in range(n-2):
        temp = []
        for j in result:
            aa = j.copy()
            ab = j.copy()
            ac = j.copy()
            aa.append('+')
            ab.append('-')
            ac.append(' ')
            temp.append(aa)
            temp.append(ab)
            temp.append(ac)
        result = temp
    result.sort()
    return list(result)

main()
