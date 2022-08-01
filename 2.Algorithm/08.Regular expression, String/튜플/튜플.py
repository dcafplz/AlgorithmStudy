def solution(s):
    ntuple = list(map(int, s.replace("{","").replace("}","").split(",")))
    return sorted(list(set(ntuple)), key = lambda x : -ntuple.count(x))