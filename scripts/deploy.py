from brownie import FundMe, network, config
from scripts.helpers import get_accounts, deploy_price_feed


def deploy_project():
    # Deploy the fund me contract to the blockchain.. whether dev, testnet or mainnet
    account = get_accounts()
    aggregator_address = deploy_price_feed()
    print("Deploying Contract")
    verify = config['networks'][network.show_active()].get('verfiy')
    fund_me = FundMe.deploy(aggregator_address,{'from':account}, publish_source = verify)
    print(f"Contract Address:",fund_me.address)
    return fund_me

    
    

def main():
    deploy_project()