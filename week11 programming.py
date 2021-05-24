import time
import random

def deco():
    print("ㅡ"*30)

start_time= int(time.time())
timer=0
count = 0


while(1):

    while(1):
        deco()
        print("구구단을 외자! 구구단을 외자!")
        menu = int(input("1. 게임 시작/2. 게임 방법 : "))

        if menu == 1 :
            break

        elif menu == 2 :
            deco()
            print("2단 부터 9단까지 랜덤으로 구구단이 출력됩니다.")
            print("제한시간 10초안에 최대한 많은 문제를 풀어보세요!")
            print("게임 종료 후 맞힌 개수가 출력되니 친구와 함께 내기를 해보세요!")

    print("준비...")
    time.sleep(3)
    print("시작!")

    while(1):
        timer = int(time.time()) - start_time
        a = int(random.randint(2, 9))
        b = int(random.randint(2, 9))
        deco()

        result = int(input("%d X %d = "%(a,b)))
        if timer > 10:
            deco()
            print("시간 초과!")
            print("맞힌개수 : %d"%count)
            break
        elif result == a*b :
            deco()
            print("정답!")
            count = count + 1
            continue
        else:
            deco()
            print("오답!")
            continue

    while(1):
        menu2 = int(input("계속 하시겠습니까? 1. yes / 2.no : "))

        if menu2 == 1:
            start_time = time.time()
            timer = 0
            count = 0
            break
        elif menu2 == 2:
            print("종료 합니다")
            quit()
        else:
            print("다시 입력해주십시오")
            continue





