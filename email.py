
import email,smtplib,getpass
                                                                        
HOST = “smtp.gmail.com”                                                                                     
PORT = 465
username = “maxamresh@gmail.com”                                                                             
password = getpass.getpass(“Amresh@123“)

server = smtplib.SMTP_SSL(HOST, PORT)


 server.login(username, password)                               
 (235, b’2.7.0 Accepted’)
 server.sendmail(
    “from@domain.com”,       
    “to@domain.com”,
    “An email from Python!”,
     )
 {}
 server.quit()                          
(221, b’2.0.0 closing connection s1sm24313728ljc.3 - gsmtp’)