/ SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.0;
import "./Tokens/DToken.sol";
contract DTokenMarket 
{
    
    DToken dToken;
    uint public weiValue;
    constructor(address tokenAddress){
      dToken=DToken(tokenAddress);
      weiValue=500000000000000;
    }
    modifier areTokensAvailable(uint requiredTokens) 
  {
    require(dToken.balanceOf(address(this))>=requiredTokens,
    "The requested amount is not available");
    _;
  }
  
  modifier isEtherEnough(uint etherAmount, uint neededEther) 
  {
    require(etherAmount>=neededEther,
    "Insufficient amount of ether");
    _;
  }

    function buyTokens(uint amount) areTokensAvailable(amount) isEtherEnough(msg.value,weiValue*amount)  payable public returns (bool success){
        dToken.transfer(msg.sender,amount);
        return true;
    }
}