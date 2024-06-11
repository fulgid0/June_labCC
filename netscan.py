import time

print('Semplice Portscan in python. Inizia cercando tutte le interfaccie affacciate su una rete (esclusa quella della macchina stessa). In seguito effettua il portscan sulla macchina trovata.\n\nLimitazioni: usa solo le /24, prevede un solo host nella subnet')


print ('USAGE: python netscan.py <IP>/24')

ip_model = re.compile(r'^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])/24$')
MAX_Port = 65535

def test_port (IP, port):
 time.sleep(1)

try:
 subnet = sys.argv[1] #controllo se mi e' stato fornito un argomento via CLI
except:
 print ('\n\n\nNessun parametro fornito via cli')
 sys.exit() 
if not ip_model.search(subnet): #Controllo se la stringa fornita e' un valido ip /24
 print('Fornisci una subnet valida')
 sys.exit()
else:
 print('CIDR corretto')
