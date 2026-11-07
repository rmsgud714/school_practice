"""
글로벌시스템융합과 프로그래밍(1) 실습 문제
실습 20: 연속된 수의 합으로 표현하기

주어진 수 N을 연속된 자연수의 합으로 표현할 수 있는 모든 경우를 출력합니다.
예: 15 = 1+2+3+4+5 = 4+5+6 = 7+8

힌트: 시작 수를 1부터 늘려가며, 연속된 수를 더해 N이 되는지 확인합니다.
"""

N = int(input("N을 입력하세요: "))

# 아래에 N을 연속된 자연수의 합으로 표현하는 모든 경우를 출력하세요

# 첫 반복문
for start in range(1, N):
    # 변수 초기화
    total = 0
    list_total = [] 
    
    # 두번째 반복문
    for end in range(start, N):
        # 누적 덧셈
        total += end
        list_total.append(end)
        
        # N인 경우 출력
        if total == N:
            print(f"{N} = {' + '.join(map(str, list_total))}")
            
            
        # 15 이상이 된 경우 반복문 종료
        if total > N:
            break
        
"""
[실행 결과 예시] (N=15)
15 = 1 + 2 + 3 + 4 + 5
15 = 4 + 5 + 6
15 = 7 + 8
"""
