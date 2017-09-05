import smtplib
import email.mime.multipart
import email.mime.text
import os

command = 'df -h '
#command = 'python -V '
r = os.popen(command)
info = r.readlines()
# content = ''.join(info)
content = ''
for line in info:

    print( line)
    content +='<br>'
    content += line

msg = email.mime.multipart.MIMEMultipart()
msg['from'] = '****@163.com'
msg['to'] = '****@qq.com,****@qq.com,****@qq.com,****@163.com,*****@qq.com'
msg['subject'] = '***服务器硬盘情况'

txt = email.mime.text.MIMEText(content,_subtype='html',_charset='gb2312')
msg.attach(txt)

smtp = smtplib
smtp = smtplib.SMTP()
smtp.connect('smtp.163.com', '25')
smtp.login('*******@163.com', '****')
#one
smtp.sendmail('*******@163.com', '*******@qq.com', str(msg))
#two
smtp.sendmail('*******@163.com', '*******@qq.com', str(msg))
#three
smtp.sendmail('*******@163.com', '*******@163.com', str(msg))
#four
smtp.sendmail('*******@163.com', '*******@qq.com', str(msg))
#five
smtp.sendmail('*******@qq.com', '*******@qq.com', str(msg))
smtp.quit()