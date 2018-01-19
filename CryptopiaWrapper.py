import requests as req
import time

#This class will handle all Cryptopia public API calls
class Public:

	#initialize Public class object
	def __init__(self):
		self.url = "https://www.cryptopia.co.nz/api/";

	#method for getting all information from Cryptopia API for every currency. 
	def getCurrencies(self):
		try:
			url = self.url + "GetCurrencies"
			currenciesInfo = req.get(url)

			return currenciesInfo.json()
		except:
			return f"Problems accessing {self.url}"

	#method for getting information from Cryptopia API for single currency
	def getCurrency(self, curr):
		try:
			url = self.url + "GetCurrencies"
			currenciesInfo = req.get(url);

			currencies = currenciesInfo.json()

			currencies = currencies['Data']

			currency = ''

			for currinfo in currencies:
				if currinfo['Symbol'] == curr:
					currency = currinfo

			if currency == '':
				return "Could not find currency."
			else:
				return currency
		except:
			return f"Problems accessing {self.url}"

	#method for getting information from Cryptopia API on Trade Pairs for all currencies
	def getTradePairs(self):
		url = self.url + "GetTradePairs";
		TradePairsInfo = req.get(url)

		return TradePairsInfo.json()

	#method for getting information from Cryptopia API on an individual Trade Pair
	def getTradePair(self, pair):
		try:
			url = self.url + "GetTradePairs";
			TradePairsInfo = req.get(url);

			TradePairs = TradePairsInfo.json()

			TradePairs = TradePairs['Label']

			TradePair = ''

			for pairinfo in TradePairs:
				if pairinfo['Symbol'] == pair:
					TradePair = pairinfo

			if TradePair == '':
				return "Could not find currency."
			else:
				return TradePair
		except:
			return f"Problems accessing {self.url}"

	#method for getting information from Cryptopia API on all market pairs.
	def getMarkets(self, basemarket=None, hours=24):
		if basemarket == None and hours == 24:
			url = self.url + "GetMarkets";
			MarketsInfo = req.get(url)

			return MarketsInfo.json()

		if basemarket != None and (hours <= 24 and hours > 0):
			url = self.url + "GetMarkets/" + basemarket
			MarketsInfo = req.get(url)

			return MarketsInfo.json()

		if basemarket == None and (hours <= 24 and hours > 0):
			url = self.url + "GetMarkets/" + str(hours)
			MarketsInfo = req.get(url)

			return MarketsInfo.json()

		if basemarket != None and (hours <= 24 and hours > 0):
			url = self.url + "GetMarkets/" + basemarket + "/" + str(hours)
			MarketsInfo = req.get(url)

			return MarketsInfo.json() 



