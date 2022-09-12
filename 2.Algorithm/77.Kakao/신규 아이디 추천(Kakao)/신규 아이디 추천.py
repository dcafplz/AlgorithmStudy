import re

def solution(new_id):
    new_id = new_id.lower()
    p = re.compile("[^a-z0-9._-]")
    k = p.findall(new_id)
    
    for i in k:
        new_id = new_id.replace(i,"")
        
    while ".." in new_id:
        new_id = new_id.replace("..", ".")
    

    if new_id[-1:] == ".":
        new_id = new_id[:-1]
    
    try:
        if new_id[0] == "." and len(new_id) >= 2:
                new_id = new_id[1:]
    except:
        new_id = ""
    
    if len(new_id) >= 16:
        new_id = new_id[:15-len(new_id)]
        if new_id[-1:] == ".":
            new_id = new_id[:-1]
    elif new_id == "":
        new_id = "a"
        
    if len(new_id) <= 2:
        new_id = new_id + new_id[-1:]*3
        new_id = new_id[0:3]
        
    return new_id


##

import re

def solution(new_id):

    # 1, 2단계
    new_id = re.sub('[^0-9a-z._-]', '', new_id.lower())
    
    # 3단계
    new_id = re.sub('\.+', '.', new_id)
    
    # 4단계
    new_id = re.sub('^[.]|[.]$', '', new_id)
    
    # 5단계
    if not new_id: new_id = 'a'
    
    # 6단계
    new_id = re.sub('[.]$', '', new_id[:min(len(new_id), 15)])
    
    # 7단계
    if len(new_id) <= 2: new_id = new_id + new_id[-1] * (3 - len(new_id))
    
    return new_id