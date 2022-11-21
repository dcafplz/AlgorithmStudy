import re

def num_to_time(num):
    hh, mm = str(num//60), str(num%60)
    return f'{(2-len(hh)) * "0"}{hh}:{(2-len(mm)) * "0"}{mm}'

def solution(n, t, m, timetable):

    p = re.compile('(\d{2}):(\d{2})')
    shuttle_times = [x for x in range(540, 541+(n-1)*t, t)]
    times = []
    for i, time in enumerate(timetable):
        hh, mm = p.findall(time)[0]
        time = int(hh)*60 + int(mm)
        if time <= shuttle_times[-1]:
            times.append(time)
    times.sort(reverse=True)

    for t in shuttle_times:
        cnt = 0
        while times:
            if times[-1] <= t:
                cnt += 1
                temp = times.pop()
                if cnt == m:
                    break
            else:
                break        
    if times or cnt == m:
        return num_to_time(temp-1)

    return num_to_time(shuttle_times[-1])