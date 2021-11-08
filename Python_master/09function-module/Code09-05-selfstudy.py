def cal(num1,num2,oper):
    if oper=="+":
        print("계산결과 : {0} {1} {2} = {3}".format(num1,oper,num2,(num1+num2)))
    elif oper=="-":
       print("계산결과 : {0} {1} {2} = {3}".format(num1,oper,num2,(num1-num2)))
    elif oper=="*":
        print("계산결과 : {0} {1} {2} = {3}".format(num1,oper,num2,(num1*num2)))
    elif oper=="/":
        if(num2==0):
            print("0으로는 나눌 수 없습니다.")
        else:
            print("계산결과 : {0} {1} {2} = {3}".format(num1,oper,num2,(num1/num2)))
    elif oper=="**":
        print("계산결과 : {0} {1} {2} = {3}".format(num1,oper,num2,(num1**num2)))
    else:
        print("연산자 중에서 선택하시기 바랍니다.")

num1 = int(input("첫번째 수를 입력하세요 : "))
oper = input("계산을 입력하세요. (+,-,*,/,**) : ")
num2 = int(input("두번째 수를 입력하세요 : "))
cal(num1,num2,oper)