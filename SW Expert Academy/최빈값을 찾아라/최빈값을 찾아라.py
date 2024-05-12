from collections import Counter

T = int(input())
for _ in range(T):
    tcase = int(input())
    score_count = Counter(map(int, input().split()))
    max_score = max(score_count, key=lambda x: (score_count[x], x))
    print(f'#{tcase} {max_score}')
