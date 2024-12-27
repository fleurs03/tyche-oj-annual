date_format = "%m月%d日"
datetime_format = "%m月%d日%H:%M:%S"

smpt_server = "mails.tsinghua.edu.cn"
smpt_port = 465
smpt_user = "sender@mails.tsinghua.edu.cn"
smpt_password = ""

sender_name = "sender"
sender_email = "sender@mails.tsinghua.edu.cn"
sender = f"{sender_name} <{sender_email}>"

# receiver_name = 'receiver'
# receiver_email = 'receiver@mails.tsinghua.edu.cn'
# receiver = f"{receiver_name} <{receiver_email}>"

subject = "Tyche OJ 年度报告 - {}"

# body = """
# {{}}同学，你好！

# 感谢你选修计算机系“程序设计基础”课程！随着2024年接近尾声，我们一同回顾这一年在“程序设计基础”课程中与Tyche OJ平台共同书写的篇章。让我们翻开记忆的扉页，追溯到学期伊始：你与OJ的故事始于{{}}，对于多数同学来说，这也是接触编程的开始。在{{}}个日夜里，时间如同一幅画卷，记录着你的辛勤与努力。

# 今年，我们布置了{}次作业，总计有{}道题目，共有{}名同学参与提交。你共向OJ提交了{{}}次评测，这一数字占到了所有同学总提交次数({}次)的{{:.2f}}%。其中，你遇到的最多的两个错误类型是{{}}（{{}}次）和{{}}（{{}}次），每一次思考与尝试，都是你成长的见证。在所有同学的提交中，提交最多的一位共提交了{}次，占据了总提交次数的{:.2f}%。

# 特别值得一提的是{{}}，你在这一天提交了{{}}次作业，显示出了非凡的专注与努力。纵观所有同学的提交记录，提交次数最多的前五名日期分别是{}、{}、{}、{}和{}，这些日期的提交量占到了总提交次数的{:.2f}%。

# 以早上5:00为界，你最早的一次提交是{{}}，最晚的一次提交是{{}}。你的提交习惯显示，你偏好在{{}}点至{{}}点之间提交作业，在这个时间段内，你共提交了{{}}次。从班级整体来看，有{:.2f}%的提交发生在{}点至{}点，{:.2f}%的提交发生在{}点至{}点，{:.2f}%的提交发生在{}点至{}点。

# 值得注意的是，你有{{}}次作业是在截止日期当天完成的，而在截止时间的最后一小时内，你共有{{}}次提交。就全体同学来说，在截止日期当天，共有{}次提交，占总提交次数的{:.2f}%，在截止时间的最后一小时内，共有{}次提交，占总提交次数的{:.2f}%。希望在未来，大家能够更好地规划时间，避免临近截止日期的紧张冲刺。

# 题目“{{}}”、“{{}}”和“{{}}”一定给你留下了深刻的印象，因为它们是你提交次数最多的三道题，分别为{{}}次、{{}}次和{{}}次，占你总提交次数的{{:.2f}}%。从OJ所有同学的总提交中看，同学们提交次数最多的前5道题目分别为：“{}”({}次)、“{}”({}次)、“{}”({}次)、“{}”({}次)和“{}”({}次)，占总提交次数的{:.2f}%。

# 随着元旦临近，“程序设计基础”课程的OJ作业告一段落。但平台仍为你准备了其他课程的作业与往年考题，供你自由练习，不断提升。

# 我们衷心祝你元旦快乐，学业有成！你即将完成在清华大学计算机系的第一门专业课的学习，我们也期待你在2025年1月4日的期末考试中取得优异的成绩！

# 注：以上统计数据截至2024年12月27日23:59，OJ平台在“{}”中共计收到{}次提交。

# 2024年12月28日
# “程序设计基础”课程组
# """

body = """
<html>
<head></head>
<body>
    <p>{{}}同学，你好！</p>
    
    <p>感谢你选修计算机系“程序设计基础”课程！随着2024年接近尾声，我们一同回顾这一年在“程序设计基础”课程中与Tyche OJ平台共同书写的篇章。让我们翻开记忆的扉页，追溯到学期伊始：你与OJ的故事始于<span style="color:FireBrick;">{{}}</span>，对于多数同学来说，这也是接触编程的开始。在<span style="color:FireBrick;">{{}}</span>个日夜里，时间如同一幅画卷，记录着你的辛勤与努力。</p>
    
    <p>今年，我们布置了<span style="color:FireBrick;">{}</span>次作业，总计有<span style="color:FireBrick;">{}</span>道题目，共有<span style="color:FireBrick;">{}</span>名同学参与提交。你共向OJ提交了<span style="color:FireBrick;">{{}}</span>次评测，这一数字占到了所有同学总提交次数(<span style="color:FireBrick;">{}</span>次)的<span style="color:FireBrick;">{{:.2f}}%</span>。其中，你遇到的最多的两个错误类型是<span style="color:FireBrick;">{{}}</span>（<span style="color:FireBrick;">{{}}</span>次）和<span style="color:FireBrick;">{{}}</span>（<span style="color:FireBrick;">{{}}</span>次），每一次思考与尝试，都是你成长的见证。在所有同学的提交中，提交最多的一位共提交了<span style="color:FireBrick;">{}</span>次，占据了总提交次数的<span style="color:FireBrick;">{:.2f}%</span>。</p>
    
    <p>特别值得一提的是<span style="color:FireBrick;">{{}}</span>，你在这一天提交了<span style="color:FireBrick;">{{}}</span>次作业，显示出了非凡的专注与努力。纵观所有同学的提交记录，提交次数最多的前五名日期分别是<span style="color:FireBrick;">{}</span>、<span style="color:FireBrick;">{}</span>、<span style="color:FireBrick;">{}</span>、<span style="color:FireBrick;">{}</span>和<span style="color:FireBrick;">{}</span>，这些日期的提交量占到了总提交次数的<span style="color:FireBrick;">{:.2f}%</span>。</p>
    
    <p>以早上5:00为界，你最早的一次提交是<span style="color:FireBrick;">{{}}</span>，最晚的一次提交是<span style="color:FireBrick;">{{}}</span>。你的提交习惯显示，你偏好在<span style="color:FireBrick;">{{}}</span>点至<span style="color:FireBrick;">{{}}</span>点之间提交作业，在这个时间段内，你共提交了<span style="color:FireBrick;">{{}}</span>次。从班级整体来看，有<span style="color:FireBrick;">{:.2f}%</span>的提交发生在<span style="color:FireBrick;">{}</span>点至<span style="color:FireBrick;">{}</span>点，<span style="color:FireBrick;">{:.2f}%</span>的提交发生在<span style="color:FireBrick;">{}</span>点至<span style="color:FireBrick;">{}</span>点，<span style="color:FireBrick;">{:.2f}%</span>的提交发生在<span style="color:FireBrick;">{}</span>点至<span style="color:FireBrick;">{}</span>点。</p>
    
    <p>值得注意的是，你有<span style="color:FireBrick;">{{}}</span>次作业是在截止日期当天完成的，而在截止时间的最后一小时内，你共有<span style="color:FireBrick;">{{}}</span>次提交。就全体同学来说，在截止日期当天，共有<span style="color:FireBrick;">{}</span>次提交，占总提交次数的<span style="color:FireBrick;">{:.2f}%</span>，在截止时间的最后一小时内，共有<span style="color:FireBrick;">{}</span>次提交，占总提交次数的<span style="color:FireBrick;">{:.2f}%</span>。希望在未来，大家能够更好地规划时间，避免临近截止日期的紧张冲刺。</p>
    
    <p>题目“<span style="color:FireBrick;">{{}}</span>”、“<span style="color:FireBrick;">{{}}</span>”和“<span style="color:FireBrick;">{{}}</span>”一定给你留下了深刻的印象，因为它们是你提交次数最多的三道题，分别为<span style="color:FireBrick;">{{}}</span>次、<span style="color:FireBrick;">{{}}</span>次和<span style="color:FireBrick;">{{}}</span>次，占你总提交次数的<span style="color:FireBrick;">{{:.2f}}%</span>。从OJ所有同学的总提交中看，同学们提交次数最多的前5道题目分别为：“<span style="color:FireBrick;">{}</span>”(<span style="color:FireBrick;">{}</span>次)、“<span style="color:FireBrick;">{}</span>”(<span style="color:FireBrick;">{}</span>次)、“<span style="color:FireBrick;">{}</span>”(<span style="color:FireBrick;">{}</span>次)、“<span style="color:FireBrick;">{}</span>”(<span style="color:FireBrick;">{}</span>次)和“<span style="color:FireBrick;">{}</span>”(<span style="color:FireBrick;">{}</span>次)，占总提交次数的<span style="color:FireBrick;">{:.2f}%</span>。</p>

    <p>随着元旦临近，“程序设计基础”课程的OJ作业告一段落。但平台仍为你准备了其他课程的作业与往年考题，供你自由练习，不断提升。</p>
    
    <p>我们衷心祝你<span style="color:FireBrick;">元旦快乐，学业有成</span>！你即将完成在清华大学计算机系的<span style="color:FireBrick;">第一门专业课</span>的学习，我们也期待你在2025年1月4日的期末考试中取得优异的成绩！</p>
    
    <p><i>注：以上统计数据截至2024年12月27日23:59，OJ平台在“{}”中共计收到{}次提交。</i></p>
    
    <p span style="text-align: right;">2024年12月28日<br>“程序设计基础”课程组</p>
    
</body>
</html>    
"""