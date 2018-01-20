from CryptopiaWrapper import Public

#This file is intended to test that the Public Cryptopia API wrapper is working

CryptoTest = Public();

# print(CryptoTest.getCurrencies());

# print(CryptoTest.getCurrency('LTC'));

# print(CryptoTest.getTradePairs());

# print(CryptoTest.url);

print(CryptoTest.getTradePair('DOGE/BTC'))