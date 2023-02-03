#출처 https://github.com/saetakki/KT-algorithm/blob/main/lottos.py

def solution(lottos, win_nums):
    
    rank = [6,6,5,4,3,2,1]
    candidate = lottos.count(0)
    remain = len(set([i for i in lottos if i != 0]) & set(win_nums))
    
    return [rank[remain+candidate], rank[remain]]

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
answer = solution(lottos, win_nums)
print(answer)