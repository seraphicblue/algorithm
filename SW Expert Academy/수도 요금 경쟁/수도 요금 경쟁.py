T = int(input())  # 테스트 케이스 수 입력

for t in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())  # 각 수도 요금 계산에 필요한 변수 입력
    
    # A사 요금 계산
    cost_A = W * P
    
    # B사 요금 계산
    if W <= R:
        cost_B = Q
    else:
        cost_B = Q + (W - R) * S
    
    # 두 요금 비교 후 더 낮은 요금 출력
    result = min(cost_A, cost_B)
    print(f"#{t} {result}")
