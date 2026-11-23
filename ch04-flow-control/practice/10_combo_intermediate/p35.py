"""
글로벌시스템융합과 프로그래밍(1) 실습 문제
실습 35: 엘리베이터 시뮬레이션

엘리베이터의 이동을 시뮬레이션합니다.
- 건물: 지하 1층(B1) ~ 지상 10층
- 현재 층: 1층에서 시작
- 이동할 층을 입력받아 한 층씩 이동하는 과정을 출력
- -1 입력: 지하 1층, 0 입력: 종료
- 현재 층과 같은 층 입력 시 안내 메시지
- 범위 밖(< -1 또는 > 10) 입력 시 오류 메시지

힌트:
- 현재 층 변수를 두고, 목표 층까지 1씩 증가/감소하며 출력합니다.
- 0층은 건물에 없으므로, 0을 건너뛰는 처리가 필요합니다.
  (단, 여기서는 -1을 지하 1층으로 간주하고 0은 종료로 사용합니다.)
"""

current = 1  # 현재 층

# 아래에 엘리베이터 시뮬레이션 코드를 작성하세요

current = 1  # 현재 층

# 엘리베이터 반복
while True:
    # 현재 층 출력
    if current == -1:
        print("현재 층: B1층")
    else:
        print(f"현재 층: {current}층")

    # 이동할 층 입력
    target = int(input("이동할 층 입력 (0: 종료): "))

    # 종료
    if target == 0:
        print("엘리베이터를 종료합니다.")
        break

    # 범위 확인
    if target < -1 or target > 10:
        print("이동할 수 없는 층입니다.")
        continue

    # 같은 층 확인
    if current == target:
        print("현재 층과 같은 층입니다.")
        continue

    # 이동 과정 출력
    print_value = ""

    # 위로 이동
    if current < target:
        while current < target:
            if current == -1:
                current = 1
            else:
                current += 1

            if current == -1:
                floor = "B1층"
            else:
                floor = f"{current}층"

            print_value += floor + " → "

    # 아래로 이동
    else:
        while current > target:
            if current == 1:
                current = -1
            else:
                current -= 1

            if current == -1:
                floor = "B1층"
            else:
                floor = f"{current}층"

            print_value += floor + " → "

    # 마지막 화살표 제거
    print_value = print_value[:-3]

    # 이동 과정 출력
    if current == -1:
        print(f"2층 → 1층 → B1층" if target == -1 else print_value)
        print("B1층에 도착했습니다.")
    else:
        print(print_value)
        print(f"{current}층에 도착했습니다.")
        
"""
[실행 결과 예시]
현재 층: 1층
이동할 층 입력 (0: 종료): 5
1층 → 2층 → 3층 → 4층 → 5층
5층에 도착했습니다.

현재 층: 5층
이동할 층 입력 (0: 종료): 2
5층 → 4층 → 3층 → 2층
2층에 도착했습니다.

현재 층: 2층
이동할 층 입력 (0: 종료): -1
2층 → 1층 → B1층
B1층에 도착했습니다.

현재 층: B1층
이동할 층 입력 (0: 종료): 0
엘리베이터를 종료합니다.
"""
