import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

userMail='EMAIL ADDRESS'
#sender mail address


userPsw='PASSWORD'
#senders mail password


csv_file=open('PATH OF CSV FILE ON HARDWARE','r+')
#open file in append mode with r+


csv_reader=csv.reader(csv_file,delimiter=',')
#CSV.reader to read the file


next(csv_reader)
# skip the first collum of the file 


server=smtplib.SMTP('smtp.gmail.com',587)
#open gmail server with its port no.


server.ehlo()
server.starttls()
#take security measure and startTLS(Transfer Layer Security)
server.ehlo()


server.login(userMail,userPsw)
#login to the server through userMail(sender's mailId) and Password(sender's mail password)


for row in csv_reader:
    name, email, subject, massage=row
    msg=MIMEMultipart()
    #read every thing you require from csv file with csvReader on row
    msg['From']=userMail
    #massage to be send from
    msg['To']=email
    #msg to be sent TO
    msg['Subject']=subject
    #subject of the email
    msg['Body']=massage
    #Body of the Email
    msg.attach(MIMEText(massage,'plain'))
    # discribe type of mail if text only than Plain
    text=msg.as_string()
    #convert everything to String
    server.sendmail(userMail,email,text)
    #send email to the the given Recevers address in the csv
server.quit()

# quit the server



