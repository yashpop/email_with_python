# Import smtplib for the actual sending function
import smtplib
import ctypes, sys

# Import the email modules we'll need
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def _sendEmail_():
    # Open a plain text file for reading.  For this example, assume that
    # the text file contains only ASCII characters.
    #fp = open(textfile, 'rb')
    fp = open('<file>,'rb')
    url_file = MIMEText(fp.read(),'<file_type>') # file_type could be text, html, javascript, pdf
    
    # Create a text/plain message
    #msg = MIMEText(fp.read()) # for text file
    msg = MIMEMultipart()
    fp.close()
    print "in else"
    #print url_file
    notes = MIMEText('Notes: <custom message in the body>','plain')
    #content="""\Test message"""

    # me == the sender's email address
    # you == the recipient's email address
    sender = 'xxx@xxxx.com'
    to  = 'test1@gmail.com;test2@gmail.com;test3@yahoo.com;test4@outlook.com'
    msg['Subject'] = 'test file using python'
    msg['From'] = sender 
    msg['To'] = to
    #msg['Cc'] = cc
    msg.attach(notes)
    msg.attach(url_file)
    print('To:', msg['to'])
    print('From:', msg['from'])
    print('Subject:', msg['subject'])

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
#'''
    server = 'smtp.it.<org>.com' #"email server"
    port  = 25
    s = smtplib.SMTP(server,port)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login('<email_id>', '<password>')
    s.sendmail(sender, to,  msg.get_content_maintype())
    s.quit()
#    '''

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    # Code of your program here
    print("admin rights available.")
    _sendEmail_()

else:
    # Re-run the program with admin rights
    print("admin rights not available for user, yet trying!")
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, "", None, 1)
    _sendEmail_()
