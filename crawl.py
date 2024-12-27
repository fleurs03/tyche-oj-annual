import json
import requests
import time
import random 
from datetime import datetime
from zoneinfo import ZoneInfo
from tqdm import tqdm
from fake_useragent import UserAgent
from utils.crawl_utils import *

# actually there is no anti-spider mechanism in Tyche
# so you can comment out all the time.sleep() calls

ua = UserAgent()

def get_gname_and_tids(gid, cookie):
    """get group name and task ids of a group"""
    time.sleep(random.random())
    url = group_url.format(gid)
    headers = base_headers.copy()
    headers["Cookie"] = cookie
    headers["User-Agent"] = ua.random
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Error: {response.status_code} {response.text}")
        return None
    text = response.text
    data = json.loads(text)
    gname = data["group"]["name"]
    tasks = data["group"]["tasks"]
    tids = [task["tid"] for task in tasks]
    return gname, tids

def get_pid2tittle_and_endTime(tid, cookie, endTimes):
    """get problem id to title mapping and task end time"""
    time.sleep(random.random())
    url = task_url.format(tid)
    headers = base_headers.copy()
    headers["Cookie"] = cookie
    headers["User-Agent"] = ua.random
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Error: {response.status_code} {response.text}")
        return None
    text = response.text
    data = json.loads(text)
    pid2tittle = dict()
    problems = data["task"]["problems"]
    for problem in problems:
        pid = problem["id"]["pid"]
        pid2tittle[pid] = problem["title"]
    endTime = data["task"]["endTime"]
    endTime = datetime.strptime(endTime, time_format)
    endTime = endTime.replace(tzinfo=ZoneInfo("UTC")).astimezone(ZoneInfo("Asia/Shanghai"))
    endTimes[tid] = endTime
    return pid2tittle

def get_submission_list(gid, tid, cookie):
    """get submission list of a task in a group"""
    time.sleep(random.random())
    url = submission_url.format(tid, gid, 1)
    headers = base_headers.copy()
    headers["Cookie"] = cookie
    headers["User-Agent"] = ua.random
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Error: {response.status_code} {response.text}")
        return None
    text = response.text
    data = json.loads(text)
    submissionCount = data["submissionCount"]
    pageCount = (submissionCount + 14) // 15 # 15 submissions per page
    submissionList = data["submissionList"]
    for i in tqdm(iterable=range(2, pageCount+1), desc="Pages", leave=False):
        time.sleep(random.random())
        url = submission_url.format(tid, gid, i)
        headers["User-Agent"] = ua.random
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Error: {response.status_code} {response.text}")
            return None
        text = response.text
        data = json.loads(text)
    submissionList += data["submissionList"]
        
    return submissionList
