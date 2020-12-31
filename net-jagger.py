#!/usr/bin/python 
from os import *
import subprocess
from termcolor import colored

ports=[[7,"echo"],[19,"Chargen"],[20,"FTP"],[21,"FTP"],[25,"smtp"],
[22,"ssh/SCP"],[23,"telnet"],[42,"Wins Replication"],[43,"Whois"],
[49,"TACAS"],[53,"DNS"],[67,"DHCP/BOOTP"],[68,"DHCP/BOOOTP"],[69,"TFTP"],
[70,"Gopher"],[79,"Finger"],
[80,"http"],[88,"kerberos"],[102,"MS Exchange"],
[110,"POP3"],[113,"Indet"],[23,"telnet"],[119,"NNTP"],
[123,"NTP"],[135,"Microsoft RPC"],[137,"NETBIOS"],[139,"NETBIOS"],
[143,"IMAP4"],[161,"SNMP"],[162,"SNMP"],[177,"XDMCP"],[179,"BGP"],
[201,"Apple Talk"],[264,"BGMP"],[318,"TSP"],[318,"HP OpenWebview"],
[383,"HP OpenWebview"],[389,"LDAP"],[411,"DirectConnect"],
[413,"DirectConnect"],[443,"https"],[445,"MicrosoftDS"],[464,"kerberos"],
[23,"SMTP Over SSL"],[497,"RETROSPECKT"],[500,"ISAKMP"],[512,"rexec"],[513,"rlogin"],
[514,"syslog"],[515,"LPD/LPR"],[520,"RIP"],[521,"RPING ipv6"],
[540,"UUCP"],[631,"Internet Pronting"]]

def getPort(port_input):
	for port in ports:
		if(int(port[0]) == int(port_input.replace("'",""))):
			return port[1]
	return port_input

print("\n\t Executing netstat ----\n")
p = subprocess.Popen(['netstat', '-putona'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print("\t"+"Protocol \t\t Local Address \t\t Remote Address \t\t Process \t\t Service")
while True:
  line = p.stdout.readline()
  if not line:
    break
  #the real code does filtering here
  #print(line.rstrip())
  line=line.rstrip()
  count=0
  for data in line.split():
  	try:
  		if(count == 3):
  			count2=0
  			for num in str(data).split(":"):
  				if count2 == 0:
  					ip=num
  					#print("IP: %s "% ip.replace("b'",""))
  				if count2 == 1:
  					port=num
  					final_port=getPort(port)
  					#print("FInal Port: %s "% final_port)
  				count2= count2 +1
  		if(count == 0):
  			protocol =str(data).replace("'b","")
  		if(count == 4):
  			remote = str(data).replace("'b","")
  		if(count == 5): 
  			status =str(data).replace("'b","")
  		if(count == 6):
  			process = str(data).replace("'b","")
  		count= count+1
  	except:
  		pass
  try:		
  	line_out=""+protocol.replace("b'","").replace("'","")+ "		"+ip.replace("b'","").replace("'","")+":"+port.replace("b'","").replace("'","")+"		"+remote.replace("b'","").replace("'","")+"		"+status.replace("b'","").replace("'","")+"		"+process.replace("b'","").replace("'","")+"	[service]"+final_port.replace("b'","").replace("'","")+"[service]"
  	print("\t"+colored(line_out,'red'))
  except:
  	pass	
print("\n\t .........End Execution............... \n")
