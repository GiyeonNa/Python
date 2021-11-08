#문자와 숫자가 섞여 있는 데이터가 있을때 숫자를 기준으로 데이터를 정렬하는 프로그램을 만든다.
import random

def getNumber(strData):
    numStr = ''
    for ch in strData:
        if ch.isdigit():
            numStr += ch

    return int(numStr)

data = []
i,k = 0,0

if __name__ == "__main__":
    for i in range(0,10):
        tmp = hex(random.randrange(0,100000))
        tmp = tmp[2:]
        data.append(tmp)

    print('정렬 전 데이터 : ',end='')
    [print(num, end='')for num in data]

    for i in range(0, len(data) - 1):
        for k in range(i+1, len(data)):
            if getNumber(data[i])>getNumber(data[k]):
                tmp = data[i]
                data[i] = data[k]
                data[k] = tmp
    
    print('\n정렬 후 데이터 : ', end='')
    [print(num,end='')for num in data]