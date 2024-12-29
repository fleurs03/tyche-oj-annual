import pandas as pd
from tqdm import tqdm

from crawl import get_gname_and_tids, get_pid2tittle_and_endTime, get_submission_list
from process import reorganize_submission_list, process_all, process_individual
from mail import reorganize_mailing_list, send_mail

if __name__ == "__main__":
    gid = None # Your Class
    cookie = "" # TA's cookie
    
    gname, tids = get_gname_and_tids(gid, cookie)
    print(f"Group name: {gname}")
    print(f"Total tasks: {len(tids)}")
    
    pid2tittle = dict()
    endTimes = dict()
    for tid in tids:
        pid2tittle.update(get_pid2tittle_and_endTime(tid, cookie, endTimes))
    print(f"Total problems: {len(pid2tittle)}")

    # recommend to run the following code once and comment out
    submissionList = []
    for tid in tqdm(iterable=tids, desc="Tasks", leave=True):
       submissionList += get_submission_list(gid, tid, cookie)
    df = pd.DataFrame(submissionList)
    df.to_csv(f"data/submission_list_{gid}.csv", index=False)
    
    # load from csv
    df = pd.read_csv(f"data/submission_list_{gid}.csv")
    submissionList = df.to_dict("records")
    
    totalSubmissions = len(submissionList)
    print(f"Total submissions: {totalSubmissions}")
    
    # organize the submissionList
    ids, submissions = reorganize_submission_list(submissionList)
    
    pre_body = process_all(gname, endTimes, pid2tittle, len(tids), submissionList)
    
    df = pd.read_csv("data/mailing_list.csv")
    mailing_list = df.to_dict("records")
    mailing_list = reorganize_mailing_list(mailing_list)
    for id, info in mailing_list.items():
        try:
            body = process_individual(info["name"], endTimes, pid2tittle, len(tids), totalSubmissions, submissions[id], pre_body)
            send_mail(info["name"], info["email"], body)
        except Exception as e:
            # probably because the student has not submitted any solution yet
            print(f"Error sending mail to {info['name']}: {e}")
