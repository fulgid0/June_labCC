#!/usr/bin/python3

import sys,os
import socket
import re
import time

print('Semplice Portscan in python. Inizia cercando tutte le interfaccie affacciate su una rete (esclusa quella della macchina stessa e altri Ip forniti via riga di comando). In seguito effettua il portscan sulla macchina trovata.\n\nLimitazioni: usa solo le /24, prevede un solo host nella subnet')


print ('USAGE: python netscan.py <IP>/24')

subnet_model = re.compile(r'^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])/24$')
ip_model = re.compile("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$")
MAX_Port = 65535
My_IP=str(os.popen('hostname -I').read()) #Acquisisco l'IP della macchina su cui gira il python
exception_list = []
exception_list.append(My_IP.split(' ')[0]) #aggiungo il mio IP come eccezione
TARGET = ""
open_ports = []


def test_port (IP, port):
 time.sleep(1)

def ip_check(ip_test,i): #controllo se gli ip forniti sono accettabili
 ck=str(i-1)
 if not ip_model.search(ip_test):
  print ("\n\n\nl'indirizzo messo come eccezione #"+ck+" non e' corretto")
  sys.exit() 
 else:
  exception_list.append(ip_test)
  print("eccezione #"+ck+" acquisita ["+ip_test+"]")
 
def ip_exception (): #scorrimento delle eventuali eccezioni per verifica di conformita'
 time.sleep(1)
 if len(sys.argv) > 1:
  for i, ip_test in enumerate(sys.argv[2:], start=2):
    ip_check(ip_test,i)

def run_ping(sample):
 response = os.system('ping -c 1 -w 1 '+sample)
 if response == 0:
  time.sleep(5)
  return(sample)
 else:
  return(0)

def PING_sweep(subnet_root):
 i = 0
 while i in range (255):
  sample=subnet_root+str(i)
  if sample not in exception_list:  #controllo se l'ip e tra quelli esclusi
    result=run_ping(sample) #testo via ping
    if result != 0:
     return result
  else:
   print(sample+" skippato come da input CLI")
  i = i+1

try:
 subnet = sys.argv[1] #controllo se mi e' stato fornito almeno un argomento via CLI
except:
 print ('\n\n\nNessun parametro fornito via cli')
 sys.exit() 
if not subnet_model.search(subnet): #Controllo se la stringa fornita e' un valido ip /24
 print('Fornisci una subnet valida')
 sys.exit()
else:
 print('CIDR corretto')
 
print ("Il mio IP e': "+My_IP)
ip_exception()

'''INIZIO SCANSIONE DELLA RETE'''

subnet_root = ".".join(subnet.split('.')[:-1])+'.' # ritorna la parte della subnet nel formato 192.168.1. in modo da poter fare il for in maniera semplice
TARGET = PING_sweep(subnet_root)
print("TROVATO TARGET ALL'IP: "+TARGET)

'''INIZIO PORT SCAN'''

print("\n\n\n-----------------")
print("-PORT SCAN SU TARGET "+TARGET+"-")


for port in range(0, MAX_Port):
    try:
     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.settimeout(0.3)
      s.connect((TARGET, port))
      open_ports.append(port)
      print ("OPEN PORT FOUND ["+str(port)+"]")
    except:
     pass
     #print (str(port)+ " CHIUSA")
