// SPDX-License-Identifier: UNLICENSED
pragma solidity 0.8.19;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Address.sol";

interface IWhitelist {
    function addToWhitelist(address candidate) external;

    function removeFromWhitelist(address candidate) external;
}

abstract contract BaseToken is IWhitelist, ERC20 {
    mapping(address => bool) internal _whitelist;

    uint8 private _decimals;

    constructor(string memory name, string memory symbol, uint8 decimals) ERC20(name, symbol) {
        _decimals = decimals;
    }

    function mintTo(address account, uint256 amount) external virtual {}

    function addToWhitelist(address candidate) external virtual override {}

    function removeFromWhitelist(address candidate) external virtual override {}

    function isMember(address account) public view returns (bool) {
        return _whitelist[account];
    }

    function decimals() public view override returns (uint8) {
        return _decimals;
    }

    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal virtual override {}
}

contract MyToken is BaseToken, Ownable {
    constructor(
        string memory name,
        string memory symbol,
        uint8 decimals
    ) BaseToken(name, symbol, decimals) {}

    function mintTo(address account, uint256 amount) external override onlyOwner{
        _mint(account, amount);
    }

    function addToWhitelist(address candidate) external override onlyOwner{
            _whitelist[candidate] = true;
    }

    function removeFromWhitelist(address candidate) external override onlyOwner{
            _whitelist[candidate] = false;
    }

    function _beforeTokenTransfer(address from, address to, uint256 amount) internal virtual override {
        super._beforeTokenTransfer(from, to, amount);

        if (from != address(0)){
            require(!Address.isContract(to) || isMember(to), "The address is not whitelisted");
        }
    }
}
