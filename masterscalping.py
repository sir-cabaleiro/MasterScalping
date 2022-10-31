import config, numpy, talib
from os import system, name
from binance.client import Client
from binance.enums import *
import time


i = 0
velas_open = []
velas_high = []
velas_low = []
velas_close = []

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear')

def calculos():
	rsi = talib.RSI(np_velas_close, 14)
	williams = talib.WILLR(np_velas_high, np_velas_low, np_velas_close, timeperiod=14)
	last_rsi = rsi[-1]
	print("Precio actual: {}".format(np_velas_close[-1]))
	print("El RSI está en  {}".format(last_rsi))
	print("Minimo últimos 30 mins  {}".format(numpy.amin(velas_low)))
	print("Williams %R")
	print(williams[-1])
	time.sleep(1)


# ///////      k0D€    \\\\\\\

while True :
	
	client = Client(config.API_KEY, config.API_SECRET, tld='com')
	velas = client.get_historical_klines("THETAUSDT", Client.KLINE_INTERVAL_1MINUTE, "30 minutes ago UTC")


	while i < len(velas):

		i = i + 1

	np_velas_open = numpy.array(velas_open)
	np_velas_high = numpy.array(velas_high)
	np_velas_low = numpy.array(velas_low)
	np_velas_close = numpy.array(velas_close)
	np_vela = numpy.array(velas[i])
# print(np_vela[1] + " Open")
		velas_open.append(float(np_vela[1]))
# print(np_vela[2] + " High")
		velas_high.append(float(np_vela[2]))
# print(np_vela[3] + " Low")
		velas_low.append(float(np_vela[3]))
# print(np_vela[4] + " Close")
		velas_close.append(float(np_vela[4]))

# print("OPENs:")
# print(np_velas_open)
# print("LOWs:")
# print(np_velas_low)
# print("HIGHs:")
# print(np_velas_high)
# print("CLOSEs:")
# print(np_velas_close)

	calculos()











# fastk, fastd = talib.STOCHRSI(np_velas_close, timeperiod=14, fastk_period=7, fastd_period=10, fastd_matype=0)
# fastk, fastd = talib.STOCH(np_velas_high, np_velas_low, np_velas_close, fastk_period=7, slowk_period=7, slowk_matype=0, slowd_period=10, slowd_matype=0)
# fastk, fastd = talib.STOCHF(np_velas_high, np_velas_low, np_velas_close, fastk_period=7, fastd_period=10, fastd_matype=0)
# last_fastk = fastk[-1]
# last_fastd = fastd[-1]
# print(last_fastk)
# print(last_fastd)





