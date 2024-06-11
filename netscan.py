#!/usr/bin/python3

import sys
import socket


print('Semplice Portscan in python. Inizia cercando tutte le interfaccie affacciate su una rete (esclusa quella della macchina stessa). In seguito effettua il portscan sulla macchina trovata.\n\nLimitazioni: usa solo le /24, prevede un solo host nella subnet')


print ('USAGE: python netscan.py <IP>')
