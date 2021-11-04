inStr, outStr = "",""
ch = ""


inStr = input("문자열을 입력하세요 : ")
count = len(inStr)

for i in range(0,count):
    #대문자 -> 소문자
    if ((inStr[i]>="A") and (inStr[i]<="Z")):
        inStr[i].lower()

    #소문자 -> 대문자
    elif (inStr[i]>="a" and inStr[i]<="z"):
        inStr[i].upper()
    
    else:
        None
print("바뀐 문자열 : %s"%inStr)
#왜 안됨

#

