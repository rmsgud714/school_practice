"""
글로벌시스템융합과 프로그래밍(1) 실습 문제
실습 22: 숫자 다이아몬드

높이 n(홀수)을 입력받아 다이아몬드 모양에 숫자를 채워 출력합니다.
각 줄에 1부터 시작하여 해당 줄의 숫자 개수만큼 증가했다가 감소합니다.

힌트: 각 줄마다 공백 출력 후, 1부터 증가했다가 감소하는 숫자를 출력합니다.
"""

n = int(input("높이(홀수) 입력: "))

# 아래에 숫자 다이아몬드를 출력하는 코드를 작성하세요

space = n // 2

# 위쪽 숫자 다이아몬드 출력
for num in range(1, n // 2 + 2):
    # 공백 출력
    print(space * " ", end="")

    # 숫자가 증가하는 부분
    for i in range(1, num + 1):
        print(i, end="")

    # 숫자가 감소하는 부분
    for i in range(num - 1, 0, -1):
        print(i, end="")

    print()
    space -= 1

# 아래쪽 공백 초기화
space = 1

# 아래쪽 숫자 다이아몬드 출력
for num in range(n // 2, 0, -1):
    # 공백 출력
    print(space * " ", end="")

    # 숫자가 증가하는 부분
    for i in range(1, num + 1):
        print(i, end="")

    # 숫자가 감소하는 부분
    for i in range(num - 1, 0, -1):
        print(i, end="")

    print()
    space += 1
    
    
"""
[실행 결과 예시] n = 5
  1
 121
12321
 121
  1
"""
