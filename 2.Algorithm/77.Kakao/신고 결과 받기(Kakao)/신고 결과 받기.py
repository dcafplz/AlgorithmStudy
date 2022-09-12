def solution(id_list, report, k):
    report = list(set(report))
    reporters = {}
    reportees = {}

    reportersCount = {x:0 for x in id_list}
    reporteesCount = {x:0 for x in id_list}

    for i in range(len(report)):
        temp = report[i].split(" ")
        reporters[i] = temp[0]
        reportees[i] = temp[1]
        reporteesCount[temp[1]] += 1

    for i in range(len(report)):
        if reporteesCount[reportees[i]] >= k:
            reportersCount[reporters[i]] +=1

    return list(reportersCount.values())

# 

def solution(id_list, report, k):
    reportee = {}
    reporter = {x:0 for x in id_list}
    for r in report:
        a, b = r.split(' ')
        if b in reportee:
            reportee[b].add(a)
        else:
            reportee[b] = {a}
        
    for key in reportee:
        if len(reportee[key]) >= k:
            for i in reportee[key]:
                reporter[i] += 1
    
    return list(reporter.values())