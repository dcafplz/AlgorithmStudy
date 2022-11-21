def solution(brown, yellow):
    for i in range((brown+yellow),0,-1):
        if (brown+yellow)%(i+2) == 0 and yellow%i == 0:
            return [i+2,(brown+yellow)//(i+2)]