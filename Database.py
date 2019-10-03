import pymongo
import csv
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText


myclient = pymongo.MongoClient('mongodb+srv://dexleow96:n4rCiTMMl5t7eeuN@cluster0-c8rcy.gcp.mongodb.net/test()')
mydb = myclient['CZ3002']
mycol = mydb['Students']

#for test only
def showDB():
    cursor = mycol.find({})
    for student in cursor: 
        print(student)

#for test only
def delStud(name):
    name = name.upper()
    student = { 'Name': name }
    mycol.delete_one(student)

def regStud(name, studId):
    studId = studId.upper()
    name = name.upper()
    newStud = { '_id': studId, 'Name': name, 'Attended': 'Yes'}
    insertStud = mycol.insert_one(newStud)

def takeAttendance(name):
    name = name.upper()
    myquery = { 'Name': name }
    newValues = { '$set': { 'Attended': 'Yes'}}
    updateValues = mycol.update_one(myquery, newValues)

def newClass():
    myquery = { 'Attended': 'Yes'}
    newValues = { '$set' : { 'Attended': 'No'}}
    updateValues = mycol.update_many(myquery, newValues)

def export():
    allStud = mycol.find()
    allStud = list(allStud)
    with open('CZ3002 Attendance List.csv', 'w', newline = '') as outfile:   
        fields = ['_id', 'Name', 'Attended']
        write = csv.DictWriter(outfile, fieldnames=fields)
        write.writeheader()
        for stud in allStud: 
            write.writerow(stud)

def email():
    # user details
    emailfrom = "cz3002bitspls@gmail.com"
    emailto = "dexterleow96@gmail.com"
    fileToSend = "CZ3002 Attendance List.csv"
    username = "cz3002bitspls@gmail.com"
    password = "cz3002bp"

    # email details
    msg = MIMEMultipart()
    msg["From"] = emailfrom
    msg["To"] = emailto
    msg["Subject"] = "CZ3002 Attendance"
    msg.preamble = "CZ3002 Attendance"

    # text of email
    body = "This is the attendance list for the class today."
    msg.attach(MIMEText(body, 'plain'))

    # attachment
    ctype, encoding = mimetypes.guess_type(fileToSend)
    if ctype is None or encoding is not None:
        ctype = "application/octet-stream"
    maintype, subtype = ctype.split("/", 1)
    fp = open(fileToSend, "rb")
    attachment = MIMEBase(maintype, subtype)
    attachment.set_payload(fp.read())
    fp.close()
    encoders.encode_base64(attachment)
    attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
    msg.attach(attachment)

    #sending email
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login(username,password)
    server.sendmail(emailfrom, emailto, msg.as_string())
    server.quit()

