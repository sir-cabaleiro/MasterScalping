import websocket, json, pprint, talib, numpy
import config
from binance.client import Client
from binance.enums import *
from os import system, name 


def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear')


SOCKET = "wss://stream.binance.com:9443/ws/thetausdt@kline_1m"
TRADE_SYMBOL = 'THETAUSDT'
RSI_PERIOD = 14
vela = []
last_rsi = 1

client = Client(config.API_KEY, config.API_SECRET, tld='com')


def on_open(ws):
    print('conexión abierta')

def on_close(ws):
    print('conexión cerrada')

def on_message(ws, message):
	global vela, last_rsi

	json_message = json.loads(message)
	contenido_mensaje = json_message['k']
	cierre = contenido_mensaje['c']
	vela_cerrada = contenido_mensaje['x']
	clear()
	print('Precio actual {}'.format(cierre))
	print("Precio velas 1 minuto: ")
	print(vela)
	print("RSI: ")
	print(last_rsi)
	

	if vela_cerrada :
		print('Vela cerrada en {}'.format(cierre))
		vela.append(float(cierre))
		print("Precio velas 1 minuto: ")
		print(vela)
		
		if len(vela) > RSI_PERIOD :
			np_vela = numpy.array(vela)
			rsi = talib.RSI(np_vela, RSI_PERIOD)
			print('Calculando RSI')
			print(rsi)
			last_rsi = int(rsi[-1])
			print("el RSI esta en  {}".format(last_rsi))
			fastk, fastd = talib.STOCHRSI(close, timeperiod=14, fastk_period=7, fastd_period=10)
			pprint(fastk)
			pprint(fastd)

		


ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()
