def solution(numbers, hand):
    answer = ""
    left = [3,1]
    right = [3,3]
    hand = -0.1 if hand == "left" else 0.1
    for i in numbers:
        i = i if i >0 else 11
        if i % 3 == 1:
            answer += "L"
            left = [i //3 , 1]
        elif i % 3 == 0:
            answer += "R"
            right = [i//3-1, 3]
        else:
            distanceLeft = abs(left[0]-(i // 3)) + abs(left[1]-(i % 3)) + hand
            distanceRight = abs(right[0]-(i // 3)) + abs(right[1]-(i % 3))
            if distanceLeft < distanceRight:
                answer += "L"
                left = [i//3,2]
            else:
                answer += "R"
                right = [i//3,2]
    return answer