def solution(priorities, location):
    position = [x for x in range(len(priorities))]
    answer = []
    while 1:
        if len(priorities) <= 0:
            break
        elif max(priorities) <= priorities[0]:
            priorities.pop(0)
            answer.append(position.pop(0))
        else:
            priorities.append(priorities.pop(0))
            position.append(position.pop(0))
    return answer.index(location) + 1