def solution(id_list, report, k):
    id_report = dict(); reports = []; banList = []
    attackId = [0 for x in range(len(id_list))]
    id_reporter = dict()
    for x in id_list:
        id_report[x] = set()
        id_reporter[x] = set()
        
    for x in report:
        dx = x.split()
        id_report[dx[1]].add(dx[0])
        id_reporter[dx[0]].add(dx[1])
        
    for key, value in id_report.items():
        reports.append(len(value))
    
    for x in range(len(reports)):
        if reports[x] >= k:
            banList.append(list(id_report.keys())[x])
            
    for i in banList:
        for x in range(len(id_list)):
            if i in list(id_reporter.values())[x]:
                attackId[x] += 1
        
    return attackId


# 문제는 카카오 '신고 결과 받기'에 대한 저의 해결 방안입니다.