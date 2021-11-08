def coffee_machine(button):
    print()
    print("1.뜨거운 물을 준비합니다")
    print("2.종이컵을 준비한다.")

    if button==1:
        print("3.아메리카노를 준비한다.")
    elif button==2:
        print("3.카페라떼를 준비한다.")
    elif button==3:
        print("3.카푸치노를 준비한다")
    elif button==4:
        print("3.에스프레소를 준비한다")
    else:
        print("1~4번중에서 골라주시길 바랍니다.")

coffee = int(input("A손님, 어떤 커피를 드릴까요? (1:아메리카노, 2:카페라떼 3: 카푸치노, 4:에스프레소) "))
coffee_machine(coffee)
print("A손님 커피 나왔습니다.")

coffee = int(input("B손님, 어떤 커피를 드릴까요? (1:아메리카노, 2:카페라떼 3: 카푸치노, 4:에스프레소) "))
coffee_machine(coffee)
print("B손님 커피 나왔습니다.")

coffee = int(input("C손님, 어떤 커피를 드릴까요? (1:아메리카노, 2:카페라떼 3: 카푸치노, 4:에스프레소) "))
coffee_machine(coffee)
print("C손님 커피 나왔습니다.")

coffee = int(input("D손님, 어떤 커피를 드릴까요? (1:아메리카노, 2:카페라떼 3: 카푸치노, 4:에스프레소) "))
coffee_machine(coffee)
print("D손님 커피 나왔습니다.")
