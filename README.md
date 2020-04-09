# 郑州大学健康状况上报平台自动打卡脚本

该脚本仅用于自动打卡郑州大学健康状况上报平台。

具体的说明介绍放在了[我的博客](https://mtics.top/auto-sign-zzu-jksb)中。

## 所需依赖
```
python==3.7
selenium
浏览器对应的驱动，如ChromeDriver
```

## 设置

需要用户自行新建`private_info.py`文件，并在里面设置如下参数：
```
UID = "学号"
PWD = "平台密码"

MAIL_USER = "通知邮箱"
MAIL_PWD = "通知邮箱授权码"
MAIL_TO = "接受通知的邮箱"
```

如果想要做成多账户的，需要通过`User(uid, pwd, email)`来定义并添加到`users`数组中

## 运行

`python auto_sign.py`

**现在，程序本身已经支持定时了！**

通过修改`auto_sign.py`中第72行代码中`==`后的数字就可以自定义时间了：

```python
if now.hour == 6 and now.minute == 0:
```

代价就是**程序必须一直运行着**。

作为补偿，我将编码修改为了GBK，这样可以运行在Linux服务器后台上了，通过以下命令即可：

```shell
nohup python auto_sign.py &
```