import smtplib
from email.mime.text import MIMEText
from email.header import Header


def push(title, htmlcontent, config):
    sender = config['sender']
    passwd = config['password']
    receiver = config['receiver']
    message = MIMEText(htmlcontent, 'html', 'utf-8')
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = Header(title, 'utf-8')
    try:
        smtp = smtplib.SMTP('smtp.qq.com',587)  # 使用SMTP_SSL创建一个SSL/TLS加密的连接
        smtp.starttls()
        smtp.login(sender, passwd)
        smtp.sendmail(sender, receiver, message.as_string())
        print("email推送成功！")
        smtp.quit()
    except Exception as e:
        print('email推送失败:', e)
