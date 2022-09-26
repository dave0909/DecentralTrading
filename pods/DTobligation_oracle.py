from os import access
from web3 import Web3
from eth_account import Account
import secrets

import web3
class DTobligation_oracle:


    def __init__(self, *args, **kw):
        self.indexing_address=args[0]
        self.contract_abi='[{"inputs":[{"internalType":"int256","name":"idResource","type":"int256"},{"internalType":"uint256","name":"accessCounter","type":"uint256"}],"name":"addAccessCounterObligation","outputs":[{"components":[{"internalType":"int256","name":"idResource","type":"int256"},{"components":[{"internalType":"uint256","name":"accessCounter","type":"uint256"},{"internalType":"bool","name":"exists","type":"bool"}],"internalType":"structDTObligations.AccessCounterObligation","name":"acObligation","type":"tuple"},{"components":[{"internalType":"uint256","name":"countryCode","type":"uint256"},{"internalType":"bool","name":"exists","type":"bool"}],"internalType":"structDTObligations.CountryObligation","name":"countryObligation","type":"tuple"},{"components":[{"internalType":"uint256","name":"usageDuration","type":"uint256"},{"internalType":"bool","name":"exists","type":"bool"}],"internalType":"structDTObligations.TemporalObligation","name":"temporalObligation","type":"tuple"},{"components":[{"internalType":"enumDTObligations.DomainType","name":"domain","type":"uint8"},{"internalType":"bool","name":"exists","type":"bool"}],"internalType":"structDTObligations.DomainObligation","name":"domainObligation","type":"tuple"},{"internalType":"bool","name":"exists","type":"bool"}],"internalType":"structDTObligations.ObligationRules","name":"","type":"tuple"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"idResource","type":"int256"},{"internalType":"uint256","name":"country","type":"uint256"}],"name":"addCountryObligation","outputs":[{"components":[{"internalType":"int256","name":"idResource","type":"int256"},{"components":[{"internalType":"uint256","name":"accessCounter","type":"uint256"},{"internalType":"bool","name":"exists","type":"bool"}],"internalType":"structDTObligations.AccessCounterObligation","name":"acObligation","type":"tuple"},{"components":[{"internalType":"uint256","name":"countryCode","type":"uint256"},{"internalType":"bool","name":"exists","type":"bool"}],"internalType":"structDTObligations.CountryObligation","name":"countryObligation","type":"tuple"},{"components":[{"internalType":"uint256","name":"usageDuration","type":"uint256"},{"internalType":"bool","name":"exists","type":"bool"}],"internalType":"structDTObligations.TemporalObligation","name":"temporalObligation","type":"tuple"},{"components":[{"internalType":"enumDTObligations.DomainType","name":"domain","type":"uint8"},{"internalType":"bool","name":"exists","type":"bool"}],"internalType":"structDTObligations.DomainObligation","name":"domainObligation","type":"tuple"},{"internalType":"bool","name":"exists","type":"bool"}],"internalType":"structDTObligations.ObligationRules","name":"","type":"tuple"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"accessCounter","type":"uint256"}],"name":"addDefaultAccessCounterObligation","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"country","type":"uint256"}],"name":"addDefaultCountryObligation","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"temporalObligation","type":"uint256"}],"name":"addDefaultTemporalObligation","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"idResource","type":"int256"},{"internalType":"enumDTObligations.DomainType","name":"domain","type":"uint8"}],"name":"addDomainObligation","outputs":[{"components":[{"internalType":"int256","name":"idResource","type":"int256"},{"components":[{"internalType":"uint256","name":"accessCounter","type":"uint256"},{"internalType":"bool","name":"exists","type":"bool"}],"internalType":"structDTObligations.AccessCounterObligation","name":"acObligation","type":"tuple"},{"components":[{"internalType":"uint256","name":"countryCode","type":"uint256"},{"internalType":"bool","name":"exists","type":"bool"}],"internalType":"structDTObligations.CountryObligation","name":"countryObligation","type":"tuple"},{"components":[{"internalType":"uint256","name":"usageDuration","type":"uint256"},{"internalType":"bool","name":"exists","type":"bool"}],"internalType":"structDTObligations.TemporalObligation","name":"temporalObligation","type":"tuple"},{"components":[{"internalType":"enumDTObligations.DomainType","name":"domain","type":"uint8"},{"internalType":"bool","name":"exists","type":"bool"}],"internalType":"structDTObligations.DomainObligation","name":"domainObligation","type":"tuple"},{"internalType":"bool","name":"exists","type":"bool"}],"internalType":"structDTObligations.ObligationRules","name":"","type":"tuple"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"enumDTObligations.DomainType","name":"domain","type":"uint8"}],"name":"adDefaultDomainObligation","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"idResource","type":"int256"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"addTemporalObligation","outputs":[{"components":[{"internalType":"int256","name":"idResource","type":"int256"},{"components":[{"internalType":"uint256","name":"accessCounter","type":"uint256"},{"internalType":"bool","name":"exists","type":"bool"}],"internalType":"structDTObligations.AccessCounterObligation","name":"acObligation","type":"tuple"},{"components":[{"internalType":"uint256","name":"countryCode","type":"uint256"},{"internalType":"bool","name":"exists","type":"bool"}],"internalType":"structDTObligations.CountryObligation","name":"countryObligation","type":"tuple"},{"components":[{"internalType":"uint256","name":"usageDuration","type":"uint256"},{"internalType":"bool","name":"exists","type":"bool"}],"internalType":"structDTObligations.TemporalObligation","name":"temporalObligation","type":"tuple"},{"components":[{"internalType":"enumDTObligations.DomainType","name":"domain","type":"uint8"},{"internalType":"bool","name":"exists","type":"bool"}],"internalType":"structDTObligations.DomainObligation","name":"domainObligation","type":"tuple"},{"internalType":"bool","name":"exists","type":"bool"}],"internalType":"structDTObligations.ObligationRules","name":"","type":"tuple"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"idResource","type":"int256"}],"name":"removeAccessCounterObligation","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"idResource","type":"int256"}],"name":"removeCountryObligation","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"removeDefaultAccessCounterObligation","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"removeDefaultCountryObligation","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"removeDefaultDomainObligation","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"removeDefaultTemporalObligation","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"idResource","type":"int256"}],"name":"removeDomainObligation","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"idResource","type":"int256"}],"name":"removeTemporalObligation","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"dtInd","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"getDefaultObligationRules","outputs":[{"components":[{"internalType":"int256","name":"idResource","type":"int256"},{"components":[{"internalType":"uint256","name":"accessCounter","type":"uint256"},{"internalType":"bool","name":"exists","type":"bool"}],"internalType":"structDTObligations.AccessCounterObligation","name":"acObligation","type":"tuple"},{"components":[{"internalType":"uint256","name":"countryCode","type":"uint256"},{"internalType":"bool","name":"exists","type":"bool"}],"internalType":"structDTObligations.CountryObligation","name":"countryObligation","type":"tuple"},{"components":[{"internalType":"uint256","name":"usageDuration","type":"uint256"},{"internalType":"bool","name":"exists","type":"bool"}],"internalType":"structDTObligations.TemporalObligation","name":"temporalObligation","type":"tuple"},{"components":[{"internalType":"enumDTObligations.DomainType","name":"domain","type":"uint8"},{"internalType":"bool","name":"exists","type":"bool"}],"internalType":"structDTObligations.DomainObligation","name":"domainObligation","type":"tuple"},{"internalType":"bool","name":"exists","type":"bool"}],"internalType":"structDTObligations.ObligationRules","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int256","name":"idResource","type":"int256"}],"name":"getObligationRules","outputs":[{"components":[{"internalType":"int256","name":"idResource","type":"int256"},{"components":[{"internalType":"uint256","name":"accessCounter","type":"uint256"},{"internalType":"bool","name":"exists","type":"bool"}],"internalType":"structDTObligations.AccessCounterObligation","name":"acObligation","type":"tuple"},{"components":[{"internalType":"uint256","name":"countryCode","type":"uint256"},{"internalType":"bool","name":"exists","type":"bool"}],"internalType":"structDTObligations.CountryObligation","name":"countryObligation","type":"tuple"},{"components":[{"internalType":"uint256","name":"usageDuration","type":"uint256"},{"internalType":"bool","name":"exists","type":"bool"}],"internalType":"structDTObligations.TemporalObligation","name":"temporalObligation","type":"tuple"},{"components":[{"internalType":"enumDTObligations.DomainType","name":"domain","type":"uint8"},{"internalType":"bool","name":"exists","type":"bool"}],"internalType":"structDTObligations.DomainObligation","name":"domainObligation","type":"tuple"},{"internalType":"bool","name":"exists","type":"bool"}],"internalType":"structDTObligations.ObligationRules","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"isOwner","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int256","name":"idResource","type":"int256"}],"name":"withSpecificRules","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]'
        self.private_key=args[1]
        self.account= Account.from_key(self.private_key)
        self.provider=Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))
        self.contract_instance = self.provider.eth.contract(address=self.indexing_address, abi=self.contract_abi)
        print(self.provider.eth.accounts)
        
    def set_default_access_counter_obligation(self,access_counter):
        tx=self.contract_instance.functions.addDefaultAccessCounterObligation(access_counter).buildTransaction({'gasPrice': Web3.toWei(21, 'gwei'),'nonce': self.provider.eth.getTransactionCount(self.account.address)})
        signed_txn = self.provider.eth.account.sign_transaction(tx, private_key=self.private_key)
        tx=Web3.toHex(self.provider.eth.sendRawTransaction(signed_txn.rawTransaction))
        print(self.provider.eth.waitForTransactionReceipt(tx))
        

    def set_default_temporal_obligation(self,temporalObligation):
        tx=self.contract_instance.functions.addDefaultTemporalObligation(temporalObligation).buildTransaction({'gasPrice': Web3.toWei(21, 'gwei'),'nonce': self.provider.eth.getTransactionCount(self.account.address)})
        signed_txn = self.provider.eth.account.sign_transaction(tx, private_key=self.private_key)
        tx=Web3.toHex(self.provider.eth.sendRawTransaction(signed_txn.rawTransaction))
        print(self.provider.eth.waitForTransactionReceipt(tx))

    def deactivate_default_access_counter_obligation(self):
        tx=self.contract_instance.functions.removeDefaultAccessCounterObligation().buildTransaction({'gasPrice': Web3.toWei(21, 'gwei'),'nonce': self.provider.eth.getTransactionCount(self.account.address)})
        signed_txn = self.provider.eth.account.sign_transaction(tx, private_key=self.private_key)
        tx=Web3.toHex(self.provider.eth.sendRawTransaction(signed_txn.rawTransaction))
        print(self.provider.eth.waitForTransactionReceipt(tx))
    def deactivate_default_temporal_obligation(self):
        tx=self.contract_instance.functions.removeDefaultTemporalObligation().buildTransaction({'gasPrice': Web3.toWei(21, 'gwei'),'nonce': self.provider.eth.getTransactionCount(self.account.address)})
        signed_txn = self.provider.eth.account.sign_transaction(tx, private_key=self.private_key)
        tx=Web3.toHex(self.provider.eth.sendRawTransaction(signed_txn.rawTransaction))
        print(self.provider.eth.waitForTransactionReceipt(tx))
    def set_access_counter_obligation(self,id,access_counter):
        tx=self.contract_instance.functions.addAccessCounterObligation(id,access_counter).buildTransaction({'gasPrice': Web3.toWei(21, 'gwei'),'nonce': self.provider.eth.getTransactionCount(self.account.address)})
        signed_txn = self.provider.eth.account.sign_transaction(tx, private_key=self.private_key)
        tx=Web3.toHex(self.provider.eth.sendRawTransaction(signed_txn.rawTransaction))
        print(self.provider.eth.waitForTransactionReceipt(tx))

    def set_temporal_obligation(self,id,temporalObligation):
        tx=self.contract_instance.functions.addTemporalObligation(id,temporalObligation).buildTransaction({'gasPrice': Web3.toWei(21, 'gwei'),'nonce': self.provider.eth.getTransactionCount(self.account.address)})
        signed_txn = self.provider.eth.account.sign_transaction(tx, private_key=self.private_key)
        tx=Web3.toHex(self.provider.eth.sendRawTransaction(signed_txn.rawTransaction))
        print(self.provider.eth.waitForTransactionReceipt(tx))
    def deactivate_access_counter_obligation(self,id):
        tx=self.contract_instance.functions.removeAccessCounterObligation(id).buildTransaction({'gasPrice': Web3.toWei(21, 'gwei'),'nonce': self.provider.eth.getTransactionCount(self.account.address)})
        signed_txn = self.provider.eth.account.sign_transaction(tx, private_key=self.private_key)
        tx=Web3.toHex(self.provider.eth.sendRawTransaction(signed_txn.rawTransaction))
        print(self.provider.eth.waitForTransactionReceipt(tx))
    def deactivate_temporal_obligation(self,id):
        tx=self.contract_instance.functions.removeTemporalObligation(id).buildTransaction({'gasPrice': Web3.toWei(21, 'gwei'),'nonce': self.provider.eth.getTransactionCount(self.account.address)})
        signed_txn = self.provider.eth.account.sign_transaction(tx, private_key=self.private_key)
        tx=Web3.toHex(self.provider.eth.sendRawTransaction(signed_txn.rawTransaction))
        print(self.provider.eth.waitForTransactionReceipt(tx))
    def set_default_country_obligation(self,country):
        tx=self.contract_instance.functions.addDefaultCountryObligation(country).buildTransaction({'gasPrice': Web3.toWei(21, 'gwei'),'nonce': self.provider.eth.getTransactionCount(self.account.address)})
        signed_txn = self.provider.eth.account.sign_transaction(tx, private_key=self.private_key)
        tx=Web3.toHex(self.provider.eth.sendRawTransaction(signed_txn.rawTransaction))
        print(self.provider.eth.waitForTransactionReceipt(tx))        

    def set_country_obligation(self,id,country):
        tx=self.contract_instance.functions.addCountryObligation(id,country).buildTransaction({'gasPrice': Web3.toWei(21, 'gwei'),'nonce': self.provider.eth.getTransactionCount(self.account.address)})
        signed_txn = self.provider.eth.account.sign_transaction(tx, private_key=self.private_key)
        tx=Web3.toHex(self.provider.eth.sendRawTransaction(signed_txn.rawTransaction))
        print(self.provider.eth.waitForTransactionReceipt(tx))    
    
    def set_domain_obligation(self,id,domain):
        tx=self.contract_instance.functions.addDomainObligation(id,domain).buildTransaction({'gasPrice': Web3.toWei(21, 'gwei'),'nonce': self.provider.eth.getTransactionCount(self.account.address)})
        signed_txn = self.provider.eth.account.sign_transaction(tx, private_key=self.private_key)
        tx=Web3.toHex(self.provider.eth.sendRawTransaction(signed_txn.rawTransaction))
        print(self.provider.eth.waitForTransactionReceipt(tx))    
    def set_default_domain_obligation(self,domain):
        tx=self.contract_instance.functions.adDefaultDomainObligation(domain).buildTransaction({'gasPrice': Web3.toWei(21, 'gwei'),'nonce': self.provider.eth.getTransactionCount(self.account.address)})
        signed_txn = self.provider.eth.account.sign_transaction(tx, private_key=self.private_key)
        tx=Web3.toHex(self.provider.eth.sendRawTransaction(signed_txn.rawTransaction))
        print(self.provider.eth.waitForTransactionReceipt(tx))
    
    def deactivate_domain_obligation(self,id):
        tx=self.contract_instance.functions.removeDomainObligation(id).buildTransaction({'gasPrice': Web3.toWei(21, 'gwei'),'nonce': self.provider.eth.getTransactionCount(self.account.address)})
        signed_txn = self.provider.eth.account.sign_transaction(tx, private_key=self.private_key)
        tx=Web3.toHex(self.provider.eth.sendRawTransaction(signed_txn.rawTransaction))
        print(self.provider.eth.waitForTransactionReceipt(tx))
    
    def deactivate_default_domain_obligation(self):
        tx=self.contract_instance.functions.removeDefaultDomainObligation().buildTransaction({'gasPrice': Web3.toWei(21, 'gwei'),'nonce': self.provider.eth.getTransactionCount(self.account.address)})
        signed_txn = self.provider.eth.account.sign_transaction(tx, private_key=self.private_key)
        tx=Web3.toHex(self.provider.eth.sendRawTransaction(signed_txn.rawTransaction))
        print(self.provider.eth.waitForTransactionReceipt(tx))

    def deactivate_default_country_obligation(self):
        tx=self.contract_instance.functions.removeDefaultCountryObligation().buildTransaction({'gasPrice': Web3.toWei(21, 'gwei'),'nonce': self.provider.eth.getTransactionCount(self.account.address)})
        signed_txn = self.provider.eth.account.sign_transaction(tx, private_key=self.private_key)
        tx=Web3.toHex(self.provider.eth.sendRawTransaction(signed_txn.rawTransaction))
        print(self.provider.eth.waitForTransactionReceipt(tx))
    def deactivate_country_obligation(self,id):
        tx=self.contract_instance.functions.removeCountryObligation(id).buildTransaction({'gasPrice': Web3.toWei(21, 'gwei'),'nonce': self.provider.eth.getTransactionCount(self.account.address)})
        signed_txn = self.provider.eth.account.sign_transaction(tx, private_key=self.private_key)
        tx=Web3.toHex(self.provider.eth.sendRawTransaction(signed_txn.rawTransaction))
        print(self.provider.eth.waitForTransactionReceipt(tx))


