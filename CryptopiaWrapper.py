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



	#method for getting information from Cryptopia API on an individual market pair
	def getMarket(self, basepair=None, hours=24):

		if type(hours) != int:
			return "This is not an integer."

		if hours < 0 or hours > 24:
			return "You entered an invalid hour format."

		if basepair != None and hours == 24:
			url = self.url + "GetMarket/" + str(basepair) + "/"
			MarketInfo = req.get(url)

			if MarketInfo.json() != None:
				return MarketInfo.json()
			else:
				return "It appears that you did not enter a proper pair."

		if basepair != None and (hours < 24 and hours > 0):
			url = self.url + "GetMarket/" + str(basepair) + "/" + str(hours)
			MarketInfo = req.get(url)

			if MarketInfo.json() != None:
				return MarketInfo.json()
			else:
				return "It appears that you did not enter a proper pair."

	#method for getting market history from Cryptopia API on an individual market pair.
	def getMarketHistory(self, basepair=None, hours=24):

		if type(hours) != int:
			return "This is not an integer."

		if hours < 0:
			return "You entered an invalid hour format."

		if basepair != None and hours == 24:
			url = self.url + "GetMarketHistory/" + str(basepair)
			MarketHistoryInfo = req.get(url)

			if MarketHistoryInfo.json() != None:
				return MarketHistoryInfo.json()
			else:
				return "It appears that you did not enter a proper pair."

		if basepair != None and hours != 24:
			url = self.url + "GetMarketHistory/" + str(base) + "/" + str(hours)
			MarketHistoryInfo = req.get(url)

			if MarketHistoryInfo.json() != None:
				return marketHistoryInfo.json()
			else:
				return "It appears that you did not enter a proper pair."

	#method for getting order list from Cryptopia API on an individual pair.
	def getMarketOrders(self, basepair=None, orders=100):
		if type(orders) != int:
			return "This is not an integer."

		if orders < 0:
			return "You entered an invalid amount of orders."

		if basepair != None and orders == 100:
			url = self.url + "GetMarketHistory/" + str(basepair)
			MarketOrdersInfo = req.get(url)

			if MarketOrdersInfo.json() != None:
				return MarketHistoryInfo.json()
			else:
				return "It appears that you did not enter a proper pair."

		if basepair != None and hours != 100:
			url = self.url + "GetMarketHistory/" + str(base) + "/" + str(orders)
			MarketOrdersInfo = req.get(url)

			if MarketOrdersInfo.json() != None:
				return marketHistoryInfo.json()
			else:
				return "It appears that you did not enter a proper pair."

	#method for getting open orders from a variety of markets via Cryptopia API
	def GetMarketOrderGroups(self, base=None, groups=[], orders=100):
		#purpose of check is to see if an int pairing was received or non-int pair.
		check = False;

		if type(groups) != list:
			return "Your groups are required to be submitted in list format."

		# print(groups[1])
		if type(groups[1]) == int:
			grouporder = "-".join(str(pair) for pair in groups)
			check = True
		else:
			grouporder = "_".join(pair for pair in groups)


		if orders < 0:
			return "You entered an invalid amount of orders."

		# print(grouporder)

		if base == None and orders == 100 and check == True:
			url = self.url + "GetMarketOrderGroups/" + grouporder
			MarketOrderGroupsInfo = req.get(url)

			return MarketOrderGroupsInfo.json()

		if base != None and orders == 100 and check == False:
			url = self.url + "GetMarketOrderGroups/" + base + "_" + grouporder + "_" + "UNO"
			MarketOrderGroupsInfo = req.get(url)

			return MarketOrderGroupsInfo.json()


		if base == None and orders != 100 and check == True:
			url = self.url + "GetMarketOrderGroups/" + grouporder + "/" + str(orders)
			MarketOrderGroupsInfo = req.get(url)

			return MarketOrderGroupsInfo.json()

		if base != None and orders != 100 and check == False:
			url = self.url + "GetMarketOrderGroups/" + base + "_" + grouporder + "_" + "UNO/" + str(orders)
			MarketOrderGroupsInfo = req.get(url)

			return MarketOrderGroupsInfo.json()


