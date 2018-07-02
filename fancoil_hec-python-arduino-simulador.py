#coding: utf-8
#Criado por Rafael Requião em Janeiro/2018
#Usar Python3 ... hora de boas práticas


#simulador de Arduino Fancoil do HEC
#so preciso receber JSON, guardar e ficar enviando a cada 2 segundos

import os, sys, io, time, datetime, serial, string

#talvez eu n ache esse pacote no PIP
import serial.tools.list_ports

import simplejson as json

import random

porta		= ""
ser			= ""
lista       = []
connected   = []


lista_recebido = ""
texto_recebido = ""
texto_retornar = ""

p = 0


def entrar(texto):
	
	#if os.name=='nt':
	#	flush_in() 
	#
	#else:
	#	sys.stdin.flush()
		


	flush_in() 

	return input(texto)
	
	
def flush_in():

	#bug introduzido a esta função no quando mudei de:
	#Python 3.4 para Python 3.6.3
	
	#https://docs.python.org/3/library/termios.html	
	'''
	Set the tty attributes for file descriptor fd from the attributes, which is a list like the one returned by tcgetattr(). The when argument determines when the attributes are changed: 
	TCSANOW to change immediately, TCSADRAIN to change after transmitting all queued output, or TCSAFLUSH to change after transmitting all queued output and discarding all queued input.
	'''
	
	#https://linux.die.net/man/3/tcflush
	

	try:
		import msvcrt
		while msvcrt.kbhit():
			msvcrt.getch()
			
	except ImportError:
		import sys, termios, tty 			#inclui modulo "tty"
		#termios.tcflush(sys.stdin, termios.TCIOFLUSH) 	#TCIOFLUSH tá bugando?
		sys.stdin.flush()


		
		
		
def pegar_porta():

	global porta
	global lista
	global connected
	global ser

	try:

		porta = lista[int(entrar("\n\n  Digite a porta: "))]
		porta = str(porta).split()
		porta = str(porta[0])

	except:
		print("\n   Indice invalido... digite novamente.\n")
		time.sleep(1)
		



def menu_configurar() :

	global porta
	global lista
	global connected

	#limpar coisas
	clear_screen()
	porta = ""

	try:
		
		#global porta
				
		print("\n\n  Portas seriais disponiveis:\n")
		lista = serial.tools.list_ports.comports()
		connected = []

		for element in lista:
			connected.append(element.device)

		#print(str(connected))

		for a in range(0 , len(lista)) :
			print("   Porta " + str(a) + " = " + str(lista[a]) )

	 

		pegar_porta()


		global ser
		ser = serial.Serial(porta , 115200, timeout=0) 
		#baudrate pra o RFCOMM do Bluetooth, alterar pra 57600 caso necessário

		print("\n    Porta \"" + str(porta) + "\" selecionada\n\n")

		#teste_comm()


	except:
		print("\n   *** Portas seriais nao encontradas! *** \n")
		time.sleep(3)













def enviar(texto_enviado):
	ser.flush()
	ser.write(bytearray(texto_enviado + "", encoding="ascii"))
	time.sleep(1/4)
	print("> " + texto_enviado)
	


def receber():
	global texto_recebido
	global texto_retornar
	global lista_recebido
	
	texto_retornar = ser.read(size=256) #nao precisa de bytearray...
	
	time.sleep(1/4)	
	
	#implementei split em jsinho

	#if "{" and "}" in texto_recebido :
	#	lista_recebido = texto_recebido.split( texto_recebido.index("}") )

	#print("   lista_recebido: " + str(lista_recebido))


	#for a in range(0, len(lista_recebido)):
	
	#   if ( len(lista_recebido[a])  > 1) : texto_retornar = lista_recebido[a]


	ser.flush()
	
	return texto_retornar
	texto_recebido = ""

	
def sair() :

	clear_screen()
	print("\n\n sair \n\n")
	quit()

	
from platform import system as system_name # Returns the system/OS name
from os import system as system_call       # Execute a shell command

def clear_screen():
	os.system('cls' if os.name=='nt' else 'clear')
	
	
	
	
#------------------------------------------------------------------------------	
	


#	Esse é o objeto JSON que eu utilizo no Arduino,
#	Segundo climatizacao_rev14.ino
#
#        root["a"]   = data.Auto;
#        root["b"]   = data.Busy;
#        root["m"]   = prog.mask;
#        root["p"]   = data.Pres;
#        root["pd1"] = prog.pd1;
#        root["pd2"] = prog.pd2;
#        root["pl1"] = prog.pl1;
#        root["pl2"] = prog.pl2;
#        root["s"]   = data.Status;
#        root["t1"]  = data.tMin;
#        root["t2"]  = data.tAtual;
#        root["t3"]  = data.tMax;
#        root["tt"]  = data.tTrigger;

json_main = {
	"a":0, 
	"b":0, 
	"m":0, 
	"p":0, 
	"pd1":"1200", 
	"pd2":"1700", 
	"pl1":"0700", 
	"pl2":"1300", 
	"s":0, 
	"t1":20, 
	"t2":23, 
	"t3":25, 
	"tt":5 
}

recebido 	= ""
parsed_json = {}

#------------------------------------------------------------------------------	

#rotina principal	
	
menu_configurar()


loop    = True

while (loop) :


	try:
		 
		p = p + 1
		
		if (p == 3):
			json_main["p"] 	= 1
			
		if (p == 6):
			json_main["p"] 	= 0
			p = 0  #resetar
	
	except:
		print("falha na contagem de p - mudar estado presenca")
		time.sleep(3)
	
	
	try:
		json_main["t2"] = random.randint(10, 30)
	
	except:
		print("falha em gerar tAtual...")
		time.sleep(3)
		
		

	jsonTexto = "  " + str(json_main) + "  "
	enviar(jsonTexto)
	
	#corrigir erro de receber 2 JSONs ao mesmo tempo
	#raise JSONDecodeError("Extra data", s, end, len(s))

	ser.flush()
	recebido = receber()
	
	#tentar implementar error handler em caracter unicode invalido
	#caracter invalido 
	#.decode() estava sem argumentos, na versão anterior

	recebido_str = recebido.decode(errors="replace")
	
	
	#remover tudo depois de "}{" , no caso de apertar temps varias vezes
	#dentro do tempo de envio
	
	#no caso da programacao de horario... eu envio 4 jsons separados
	#vou reprogramar o app pra enviar os 4 de vez em um objeto so
		
	jsinho = recebido_str.split("\n")
	print("jsinho = " + str(jsinho))

	recebido_str = jsinho[len(jsinho)-1]
	print("recebido_str = " + recebido_str)
	
	if (len(recebido_str) > 4) :
	
		try: 
			
			parsed_json = json.loads(recebido_str)
			
			#sequencia de ifs... nao sei iterar sobre os itens em json_main
			#for (a in json_main) ? consigo acessar como em ECMAScript?
			
			if "a" in recebido_str :
				json_main["a"] 		= parsed_json["a"]
			
			if "b" in recebido_str :
				json_main["b"] 		= parsed_json["b"]
			
			if "m" in recebido_str :
				json_main["m"] 		= parsed_json["m"]
				
			#if "p" in recebido_str :
			#	json_main["p"] 		= parsed_json["p"]				
			
			if "pd1" in recebido_str :
				json_main["pd1"] 	= parsed_json["pd1"]
			
			if "pd2" in recebido_str :
				json_main["pd2"] 	= parsed_json["pd2"]
			
			if "pl1" in recebido_str :
				json_main["pl1"] 	= parsed_json["pl1"]
			
			if "pl2" in recebido_str :
				json_main["pl2"] 	= parsed_json["pl2"]
			
			if "s" in recebido_str :
				json_main["s"] 		= parsed_json["s"]
				
			if "t1" in recebido_str :
				json_main["t1"] 	= parsed_json["t1"]
			
			#if "t2" in recebido_str :
			#	json_main["t2"] 	= parsed_json["t2"]
			
			if "t3" in recebido_str :
				json_main["t3"] 	= parsed_json["t3"]
			
			if "tt" in recebido_str :
				json_main["tt"] 	= parsed_json["tt"]
			
			print("copiei os valores do recebido pra json_main")
			
		
		
		except :
			
			print("Erro na decodificacao do JSON recebido")
			time.sleep(5)
		
	
	else :
		print("len(recebido_str) <= 4")
	
	


			
	
	time.sleep(1/4)
	clear_screen()

