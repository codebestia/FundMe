from brownie import network, accounts, config, MockV3Aggregator
from web3 import Web3

LOCAL_NETWORKS = ['development']


def get_accounts(env_account = True):
    if network.show_active() == "development":
        account = accounts[0]
    else:
        if env_account:
            account = accounts.add(config['wallets']['from'])
        else:
            account = accounts.load("mainaddress")
    return account


def deploy_price_feed():
    if network.show_active() == "development":
        # if running on a dev blockchain like ganache or mainnet-fork
        if len(MockV3Aggregator) <= 0:
            print("Deploying MockAggregator")
            aggregator = MockV3Aggregator.deploy(8,200000000000,{'from':get_accounts()})
            print("Mock deployed at",aggregator.address)
            print("Mock Price:", aggregator.latestAnswer())
        else:
            aggregator = MockV3Aggregator[-1].address
        return aggregator.address
    else:
        # running on testnet or mainnet
        print("testnet or mainnet address")
        return config['networks'][network.show_active()]['eth_price_feed']



