import re

def solution(skill, skill_trees):
    p = re.compile("[" + skill + "]")
    answer = 0
    for i in skill_trees:
        m = ''.join(p.findall(i))
        if skill.startswith(m):
            answer += 1
    return answer

# def solution(skill, skill_trees):
#     answer = len(skill_trees)
#     for s1 in skill_trees:
#         cnt = 0
#         for s2 in s1:
#             if s2 in skill:
#                 if skill.index(s2) == cnt:
#                     cnt+= 1
#                 else:
#                     answer -= 1
#                     break
#     return answer