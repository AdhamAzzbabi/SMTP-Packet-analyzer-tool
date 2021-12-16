import socket 
import smtplib 
from uuid import getnode as get_mac 
from email.message import EmailMessage


# socket.AF_INET represents the IPv4 , and socket.SOCK_STREAM shows the connection type which is TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Rather than binding in this line the code will connect
s.connect((socket.gethostname(), 1234))
print('Application started')
print('socket is connected to %s:%d' % s.getpeername())
#Getting the ip address of the client
ipAddress = socket.gethostbyname(socket.gethostname())

#This is used to make the interface easier for the user to read
print("---------------------------------------------------")
#Getting the mac address of the client and displaying it 
mac=get_mac()
macString=":".join(("%012X" % mac) [i:i+2] for i in range (0,12,2))


print("SMTP Packet details:")
#Message that will recieve 220- Service Ready 
msg = s.recv(1024) 
print(msg.decode("utf-8"))

#sending EHALO command to the server
print("sending EHLO command")
HELO = str('hello')
s.send(HELO.encode())

#Message that will recieve 220- Service Ready from the server
msg2 = s.recv(1024) 
print(msg2.decode("utf-8"))

print("sending 250 command")
Ok = '250'
s.send(Ok.encode())
#This will send the Mac address of the client to the server 
print("Sending Client Mac Address")
Mac = (macString)
s.send(Mac.encode())

#This will send the IP Address of the client to the server
print("sending CLient IP Address")
ip = (ipAddress)
s.send(ip.encode())


print("Sending DATA")
data = ("DATA")
s.send(data.encode())
#s.recv(1024) is the buffer size
msg3 = s.recv(1024) 
print(msg3.decode("utf-8"))

print("---------------------------------------------------")

#This block will get the mac address ,and then send it over the email as an SMTP Packet
msg=EmailMessage()
msg['Subject']= ("Smtp Packet" )
msg['From']='Python'
msg['To']= input("please enter the destination that you want to send the email(smtp packet) to: ")
msg.set_content("TCP Socket Has been created:" "\n Client mac addres is:" "[" + macString + "]"  "\n\n socket is connected to: %s:%d" % s.getsockname() )

#Logain credentials to send the email from
#Smtp server and port number
server=smtplib.SMTP_SSL('smtp.gmail.com',465)
server.login("smtptest928@gmail.com", "smtp0000")
print("Smtp packet information:" "\n \n From:smtptest928@gmail.com" "\n To:",msg['To'])


print("\n Smtp packet has been sent sucessfully!!")
#This will send message to the server saying to quit
print("Quitting")
data = ("Quit")
s.send(data.encode())
#Quitting server
server.send_message(msg)
server.quit()

