from brownie import FundMe, network
from web3 import Web3
from scripts.helpers import get_accounts, LOCAL_NETWORKS
from scripts.deploy import deploy_project
def fund():
    account = get_accounts()
    if network.show_active() in LOCAL_NETWORKS:
        fund_me = deploy_project()
    else:
        fund_me = FundMe[-1]
    print("Funding Contract ....")
    print(fund_me.getPrice({'from':account}))
    print(fund_me.getAggregatorVersion({'from':account}))
    tx = fund_me.fund({'from':account,'value':250000000000000000})
    tx.wait(1)
    
def withdraw():
    account = get_accounts()
    if network.show_active() in LOCAL_NETWORKS:
        fund_me = deploy_project()
    else:
        fund_me = FundMe[-1]
    print("Withdrawing from Contract")
    tx = fund_me.withdraw({'from':account})
    

def main():
    fund()
    withdraw()