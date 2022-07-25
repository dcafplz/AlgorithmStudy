def solution(participant, completion):

    def dic(todic):
        counts = {}
        for x in todic:
            if x in counts:
                counts[x] += 1
            else: counts[x] = 1
        return counts

    a = dic(participant)
    b = dic(completion)
    
    for i in a:
        try:
            if a[i] != b[i]:
                return i
        except:
            return i