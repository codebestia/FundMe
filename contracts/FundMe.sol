// SPDX-License-Identifier: MIT
pragma solidity ^0.6.6;

// import "./interfaces/AggregatorV3Interface.sol";
// import "./vendors/SafeMathChainlink.sol";
import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";
import "@chainlink/contracts/src/v0.6/vendor/SafeMathChainlink.sol";


contract FundMe{
    using SafeMathChainlink for uint256;

    mapping(address => uint256) fundAccounts;
    address[] public fundAccountsArray;
    address public owner;
    AggregatorV3Interface aggregator;
    

    constructor(address _aggregatorAddress) public{
        owner = msg.sender;
        aggregator = AggregatorV3Interface(_aggregatorAddress);

    }
    function fund() public payable {
        uint256 minimumFundAmount = 50 * (10**18);
        require(getConversionRate(msg.value) >= minimumFundAmount,"You need to spend $50 work of eth");
        fundAccounts[msg.sender] += msg.value;
        fundAccountsArray.push(msg.sender);

    }
    function getConversionRate(uint256 ethAmount) public view returns(uint256){
        uint256 price = getPrice();
        uint256 converted_price = (price * ethAmount)/(10**18);
        return converted_price;
    }
    function getAggregatorVersion() public view returns(uint256){
        
        return aggregator.version();
    }
    function getAddressFundInUSD (address accountAddress) public view returns(uint256){
        return getPrice() * fundAccounts[accountAddress];
    }
    function getPrice() public view returns(uint256){
        (,int256 answer,,,) = aggregator.latestRoundData();

        return uint256(answer) * 10**10;
    }
    modifier ownerOnly(){
        require(owner == msg.sender,"Invalid Contract sender");
        _;
    }
    function withdraw() public ownerOnly {
        
        msg.sender.transfer(address(this).balance);
        // Set all address balance to 0
        for(uint256 idx = 0; idx < fundAccountsArray.length; idx++){
            fundAccounts[fundAccountsArray[idx]] = 0;
        }
        fundAccountsArray = new address[](0);
    }
}