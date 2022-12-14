# https://school.programmers.co.kr/learn/courses/30/lessons/133499
# replace나 in연산이나 비슷한 시간복잡도일테니 ayaaya in을 활용하는게 더 빠를거같다

def solution(babbling):
    dict = {'aya':'1', 'ye':'2', 'woo':'3', 'ma':'4', '11':'f', '22':'f', '33':'f', '44':'f'}
    cnt = 0
    for b in babbling:
        for k in dict:
            b = b.replace(k, dict[k])
        cnt += b.isdigit()
    return cnt