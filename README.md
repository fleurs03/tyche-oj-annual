<div align="center">
	<h1>Tyche OJ Annual</h1>
</div>



本项目用于生成和分发 [Tyche OJ](http://166.111.68.250) 的定制化年度报告，供其他使用该 OJ 的课程助教参考。

## 准备工作

1. 通过 [清华大学网络学堂](https://learn.tsinghua.edu.cn) 下载学生信息：

   + 导航至“学生信息”，导出 `.xls` 文件；
   + 将导出的文件放置在项目根目录下的 `./data` 文件夹中。

2. 运行以下命令提取数据：

   ```sh
   python extract.py
   ```

3. 配置项目：

   + 修改 `./main.py` 中的 `gid` 和 `cookie`。
   + 在 `./utils/mail_utils.py` 中填写以下内容：
     + `smpt_user` 和 `smpt_password`；
     + `sender_name` 和 `sender_email`；
     + 根据需要调整 `./utils/mail_utils.py` 中 `body`。

## 生成与分发

执行以下命令生成并通过邮件分发定制化报告：

```sh
python main.py
```



*创意参考：清华大学电子系“数据与算法”课程组*

