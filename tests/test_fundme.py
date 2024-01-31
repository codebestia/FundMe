from scripts.deploy import deploy_project
from scripts.helpers import get_accounts, LOCAL_NETWORKS
from web3 import Web3
from brownie import exceptions, network
import pytest


def test_fund_min():
    """
    This test fails during local testing for unknown reasons
    """
    if network.show_active() not in LOCAL_NETWORKS:
        pytest.skip()
    # Arrange
    account = get_accounts()
    fund_me = deploy_project()
    # act and assert
    with pytest.raises(exceptions.VirtualMachineError):
        # conversion rate for mock: 2000
        # min eth = 50/2000 = 0.025 
        # try 40$ eth = 40/2000 = 0.02
        value = Web3.toWei(0.02,"ether")
        print(value)
        fund_me.fund({'from': account,'value':int(value)})


