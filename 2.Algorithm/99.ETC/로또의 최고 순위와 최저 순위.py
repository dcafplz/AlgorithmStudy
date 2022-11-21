def solution(lottos, win_nums):
    hit = sum([(x in win_nums) for x in lottos])
    zero = lottos.count(0)
    
    return [min(6,7-hit-zero),min(6, 7-hit)]