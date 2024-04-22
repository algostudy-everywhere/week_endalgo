'''
꺽쇠의 인덱스를 리스트에 저장.

풀이 by 준우 (미완)
'''

from collections import deque
N = input()
point = []
index = 0  # 시작 인덱스를 0으로 초기화
while True:
    # 꺾쇠(`<`)의 인덱스를 찾음
    start_index = N.find('<', index)
    # 꺾쇠(`<`)를 더 이상 찾지 못한 경우 반복 종료
    if start_index == -1:
        break
    # 꺾쇠(`<`)의 인덱스를 리스트에 추가
    point.append(start_index)
    # 꺾쇠(`<`) 다음에 나오는 꺾쇠(`>`)의 인덱스를 찾음
    end_index = N.find('>', start_index)
    # 꺾쇠(`>`)의 인덱스를 리스트에 추가
    point.append(end_index)
    # 다음 탐색을 위해 시작 인덱스를 꺾쇠(`<`) 다음부터 설정
    index = end_index + 1

print(point)


