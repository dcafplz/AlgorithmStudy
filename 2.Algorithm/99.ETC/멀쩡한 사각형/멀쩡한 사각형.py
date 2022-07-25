def solution(w,h):
    answer = w * h - w - h
    if w < h:
        w, h = h, w
    while h != 0:
        w, h = h, w % h
    return answer +w
