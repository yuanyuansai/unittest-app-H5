# coding=utf-8
from email.mime.text import MIMEText
import time
import smtplib
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import email
import os

class sendEmail:
    global send_user
    global email_host
    global password
    email_host = "smtp.126.com"
    send_user = "xiaoyuan870@126.com"
    password = "USFRFESMSMNTPRGL"
    def sendmain(file_path, mail_to='383112433@qq.com'):
        mail_from = 'xiaoyuan870@126.com'  # 发送邮件账号
        f = open(file_path, 'rb')
        mail_body = f.read()
        f.close()

        # msg = email.MIMEMultipart.MIMEMultipart()
        msg = MIMEMultipart()

        # 构造MIMEBase对象做为文件附件内容并附加到根容器
        contype = 'application/octet-stream'
        maintype, subtype = contype.split('/', 1)

        ## 读入文件内容并格式化
        data = open(file_path, 'rb')
        file_msg = MIMEBase(maintype, subtype)
        file_msg.set_payload(data.read())
        data.close()
        encoders.encode_base64(file_msg)

        ## 设置附件头
        basename = os.path.basename(file_path)
        file_msg.add_header('Content-Disposition',
                            'attachment', filename=basename)
        msg.attach(file_msg)
        print(u'msg 附件添加成功')

        msg1 = MIMEText(mail_body, _subtype='html', _charset='utf-8')
        msg.attach(msg1)

        if isinstance(mail_to, str):
            msg['To'] = mail_to
        else:
            msg['To'] = ','.join(mail_to)
        msg['From'] = mail_from
        msg['Subject'] = u'接口自动化测试报告'
        msg['date'] = time.strftime('%Y-%m-%d-%H_%M_%S')
        print(msg['date'])

        smtp = smtplib.SMTP()
        smtp.connect(email_host)
        smtp.login(send_user, password)  # 发送邮件账号密码
        smtp.sendmail(mail_from, mail_to, msg.as_string())
        smtp.quit()
        print('email has send out !')


if __name__ == '__main__':
    sendEmail.sendmain(r'D:\unittest\report\1.html')
