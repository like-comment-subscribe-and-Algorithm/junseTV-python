def formatint(total, num):
    current = list(map(int, str(num)))
    if len(current) < total:
        for i in range(total-len(current)):
            current.insert(0,0)
    return current

def compare(a, b):
    compared = []
    for i in range(len(a)):
        if a[i] != b[i]:
            compared.append((a[i], b[i]))
    return compared

def compare2(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    return count

def main():
    a = list(map(int, input().split(' ')))

    n = a[0] # 1이상 n 이하로 바꿀 예정
    k = a[1] # 디스플레이 자릿수
    p = a[2] # 최소 1개, 최대 p개 바꿀 예정
    x = a[3] # 현재 엘리베이터 층

    current = formatint(k,x)

    zero = [1,1,1,0,1,1,1]
    one = [0,0,1,0,0,1,0]
    two = [0,1,1,1,1,0,1]
    three = [0,1,1,1,0,1,1]
    four = [1,0,1,1,0,1,0]
    five = [1,1,0,1,0,1,1]
    six = [1,1,0,1,1,1,1]
    seven = [0,1,1,0,0,1,0]
    eight = [1,1,1,1,1,1,1]
    nine = [1,1,1,1,0,1,1]

    allnum = [zero, one, two, three, four, five, six, seven, eight, nine]

    built = dict()
    for i in range(10):
        built[i] = []

    for i in range(10):
        for j in range(10):
            temp = built[i]
            temp.append(compare2(allnum[i], allnum[j]))
            built[i] = temp

    answer = 0

    for i in range(1, n+1):
        if x == i:
            continue
        diff = compare(formatint(k,i), current)
        tempcount = 0
        boolean = True
        for j in diff:
            tempcount += built[j[0]][j[1]]
            if tempcount > p:
                boolean = False
                break
            else:
                boolean = True
        if boolean:
            answer += 1

    print(answer)

main()