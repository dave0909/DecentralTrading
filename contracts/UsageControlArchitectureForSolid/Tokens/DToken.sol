// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.0;
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "../Libraries/Ownable.sol";

contract DToken is ERC20,Ownable {

    constructor() ERC20("DToken","DT") {}
    


    function mint(address account, uint256 amount) public onlyOwner returns (bool) 
    {
        _mint(account, amount);
        return true;
    }

    function burn(address account,uint256 amount) public onlyOwner virtual 
    {
        _burn(account, amount);
    }


    

}