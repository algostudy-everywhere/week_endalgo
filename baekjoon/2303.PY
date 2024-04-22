'''
풀이 by 준우
'''

from itertools import combinations

def calculate_combinations(numbers):
    # 세 장의 합을 저장할 리스트
    sums = []
    
    # 주어진 리스트에서 세 장의 조합을 구하고 각 조합의 합을 계산하여 sums 리스트에 추가
    for combination in combinations(numbers, 3):
        sums.append(sum(combination) % 10)  # 합의 일의 자리 수만 저장
        
    return sums

N = int(input())
ans = []

for i in range(N):
    lst = list(map(int, input().split()))
    lst = calculate_combinations(lst)
    ans.append(max(lst))

max_ans = max(ans)

if ans.count(max_ans) != 1:
    max_indices = [i + 1 for i, x in enumerate(ans) if x == max_ans]
    print(max_indices[-1])  # 번호가 가장 큰 사람의 번호 출력
else:
    print(ans.index(max_ans) + 1)
