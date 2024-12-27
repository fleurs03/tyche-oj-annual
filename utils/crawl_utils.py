# http://166.111.68.250/tyche/group/ShowGroup?gid={}
# http://166.111.68.250/tyche/task/ShowTask?tid={}
# http://166.111.68.250/tyche/task/Status?tid={}&gid={}&all=true&page={}

base_url = "http://166.111.68.250/tyche/"
group_url = base_url + "group/ShowGroup?gid={}"
task_url = base_url + "task/ShowTask?tid={}"
submission_url = base_url + "task/Status?tid={}&gid={}&all=true&page={}"

base_headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Cookie": None,
    "Connection": "keep-alive",
    "Referer": "http://166.111.68.250/tyche/",
    "Accept-Language": "zh-CN,zh-Hans;q=0.9",
    "User-Agent": None,
    "Accept-Encoding": "gzip, deflate",
    "Authorization": "Basic Y3M6dGh1Yysr", # base64 encoded "cs:thuc++"
    "X-Requested-With": "XMLHttpRequest",
    "Priority": "u=3, i"
}

time_format = "%Y-%m-%dT%H:%M:%S"

# example_submission = {
#     codeLength": 104,
#     "gid": 33,
#     "language": "CPP",
#     "memory": 4180,
#     "name": "20xxxxxxxx",
#     "outdated": False,
#     "pid": 2044,
#     "result": 2,
#     "score": 100,
#     "secret": False,
#     "sid": xxxxxx,
#     "submitedTime": "%Y-%m-%dT%H:%M:%S",
#     "tid": 1300,
#     "time": 0,
#     "uid": xxxx
# }