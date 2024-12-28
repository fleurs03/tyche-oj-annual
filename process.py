from datetime import datetime
from datetime import datetime
from zoneinfo import ZoneInfo

from utils.crawl_utils import time_format
from utils.mail_utils import datetime_format, date_format, body
from utils.process_utils import result2str

def reorganize_submission_list(submissionList):
    """reorganize submission list by name"""
    ids = set()
    submissions = dict()
    for submission in submissionList:
        id = submission["name"]
        if id in ids:
            submissions[id].append(submission)
        else:
            ids.add(id)
            submissions[id] = [submission]
    return ids, submissions

def process_all(gname, endTimes, pid2tittle, totalTasks, submissionList):
    """process all submissions"""
    totalSubmissions = len(submissionList)
    dateCounts = dict()
    hourCounts = dict()
    pidCounts = dict()
    idCounts = dict()
    lastHourCounts = 0
    lastDayCounts = 0
    for submission in submissionList:
        submitedTime = submission["submitedTime"]
        submitedTime = datetime.strptime(submitedTime, time_format)
        submitedTime = submitedTime.replace(tzinfo=ZoneInfo("UTC")).astimezone(ZoneInfo("Asia/Shanghai"))
        
        date = submitedTime.date()
        if date not in dateCounts:
            dateCounts[date] = 1
        else:
            dateCounts[date] += 1
        
        hour = submitedTime.hour
        if hour not in hourCounts:
            hourCounts[hour] = 1
        else:
            hourCounts[hour] += 1
            
        endTime = endTimes[submission["tid"]]
        if submitedTime.date() == endTime.date():
            # last hour count, take both 11:59 and 12:00 into consideration
            if endTime.minute > 0 and hour == endTime.hour or endTime.minute == 0 and hour == endTime.hour - 1:
                lastHourCounts += 1
            lastDayCounts += 1
            
        pid = submission["pid"]
        if pid not in pidCounts:
            pidCounts[pid] = 1
        else:
            pidCounts[pid] += 1 
        
        id = submission["name"]
        if id not in idCounts:
            idCounts[id] = 1
        else:
            idCounts[id] += 1 
            
    # sort by counts
    dateCounts = sorted(dateCounts.items(), key=lambda x: x[1], reverse=True)
    hourCounts = sorted(hourCounts.items(), key=lambda x: x[1], reverse=True)
    pidCounts = sorted(pidCounts.items(), key=lambda x: x[1], reverse=True)
    idCounts = sorted(idCounts.items(), key=lambda x: x[1], reverse=True)
        
    pre_body = body.format(
        totalTasks, len(pidCounts), len(idCounts), totalSubmissions, idCounts[0][1], idCounts[0][1]/totalSubmissions*100,
        dateCounts[0][0].strftime(date_format), dateCounts[1][0].strftime(date_format), dateCounts[2][0].strftime(date_format), dateCounts[3][0].strftime(date_format), dateCounts[4][0].strftime(date_format), sum(dateCounts[i][1] for i in range(5))/totalSubmissions*100,
        hourCounts[0][1]/totalSubmissions*100, hourCounts[0][0], hourCounts[0][0]+1, hourCounts[1][1]/totalSubmissions*100, hourCounts[1][0], hourCounts[1][0]+1, hourCounts[2][1]/totalSubmissions*100, hourCounts[2][0], hourCounts[2][0]+1,
        lastDayCounts, lastDayCounts/totalSubmissions*100, lastHourCounts, lastHourCounts/totalSubmissions*100,
        pid2tittle[pidCounts[0][0]], pidCounts[0][1], pid2tittle[pidCounts[1][0]], pidCounts[1][1], pid2tittle[pidCounts[2][0]], pidCounts[2][1], pid2tittle[pidCounts[3][0]], pidCounts[3][1], pid2tittle[pidCounts[4][0]], pidCounts[4][1], sum(pidCounts[i][1] for i in range(5))/totalSubmissions*100,
        gname, totalSubmissions
    )
    return pre_body

def process_individual(name, endTimes, pid2tittle, totalTasks, overallTotalSubmissions, submissions, pre_body):
    """process individual's submission list"""
    totalSubmissions = len(submissions)
    dateCounts = dict()
    hourCounts = dict()
    pidCounts = dict()
    resultCounts = dict()
    lastHourCounts = 0
    lastDayCounts = set()
    
    submissions = sorted(submissions, key=lambda x: x["submitedTime"], reverse=False)
    
    firstSubmission = submissions[0]["submitedTime"]
    firstSubmission = datetime.strptime(firstSubmission, time_format)
    firstSubmission = firstSubmission.replace(tzinfo=ZoneInfo("UTC")).astimezone(ZoneInfo("Asia/Shanghai"))
    curDate = datetime.now().date()
    days = (curDate - firstSubmission.date()).days
    
    # use 5:00 as the separator
    earlistSubmission = firstSubmission.astimezone(ZoneInfo("Europe/Moscow"))
    latestSubmission = firstSubmission.astimezone(ZoneInfo("Europe/Moscow"))
    
    for submission in submissions:
        submitedTime = submission["submitedTime"]
        submitedTime = datetime.strptime(submitedTime, time_format)
        submitedTime = submitedTime.replace(tzinfo=ZoneInfo("UTC")).astimezone(ZoneInfo("Asia/Shanghai"))
        
        date = submitedTime.date()
        if date not in dateCounts:
            dateCounts[date] = 1
        else:
            dateCounts[date] += 1
        
        hour = submitedTime.hour
        if hour not in hourCounts:
            hourCounts[hour] = 1
        else:
            hourCounts[hour] += 1
        
        shifted = submitedTime.astimezone(ZoneInfo("Europe/Moscow"))
        if shifted.time() < earlistSubmission.time():
            earlistSubmission = shifted
        if shifted.time() > latestSubmission.time():
            latestSubmission = shifted
            
        result = submission["result"]
        if result not in resultCounts:
            resultCounts[result] = 1
        else:
            resultCounts[result] += 1 
        
        tid = submission["tid"]
        endTime = endTimes[tid]
        if submitedTime.date() == endTime.date():
            # last hour count, take both 11:59 and 12:00 into consideration
            if endTime.minute > 0 and hour == endTime.hour or endTime.minute == 0 and hour == endTime.hour - 1:
                lastHourCounts += 1
            lastDayCounts.add(tid)
            
        pid = submission["pid"]
        if pid not in pidCounts:
            pidCounts[pid] = 1
        else:
            pidCounts[pid] += 1 
            
    # sort by counts
    dateCounts = sorted(dateCounts.items(), key=lambda x: x[1], reverse=True)
    hourCounts = sorted(hourCounts.items(), key=lambda x: x[1], reverse=True)
    
    pidCounts[-1] = 0
    pidCounts[-2] = 0
    pidCounts = sorted(pidCounts.items(), key=lambda x: x[1], reverse=True)
    
    resultCounts[2] = -1 # 2 is pass
    resultCounts[14] = 0 # in case there is only 1 kind of failed result
    resultCounts = sorted(resultCounts.items(), key=lambda x: x[1], reverse=True)
    body = pre_body.format(
        name,
        firstSubmission.strftime(datetime_format), days,
        totalSubmissions, totalSubmissions/overallTotalSubmissions*100, result2str[resultCounts[0][0]], resultCounts[0][1], result2str[resultCounts[1][0]], resultCounts[1][1],
        dateCounts[0][0].strftime(date_format), dateCounts[0][1],
        earlistSubmission.astimezone(ZoneInfo("Asia/Shanghai")).strftime(datetime_format), latestSubmission.astimezone(ZoneInfo("Asia/Shanghai")).strftime(datetime_format), hourCounts[0][0], hourCounts[0][0]+1, hourCounts[0][1],
        len(lastDayCounts), lastHourCounts,
        pid2tittle.get(pidCounts[0][0], "N/A"), pid2tittle.get(pidCounts[1][0], "N/A"), pid2tittle.get(pidCounts[2][0], "N/A"), pidCounts[0][1], pidCounts[1][1], pidCounts[2][1], sum(pidCounts[i][1] for i in range(3))/totalSubmissions*100
    )
    return body