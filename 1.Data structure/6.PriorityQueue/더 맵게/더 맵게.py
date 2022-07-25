import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    try:
        while scoville[0]<K:
            heapq.heappush(scoville, heapq.heappop(scoville)+heapq.heappop(scoville)*2)
            answer += 1
        return answer
    except:
        return -1