// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.19;

abstract contract ArrayStorage {
    uint256[] private array;

    function collide() external virtual;

    function getArray() external view returns (uint256[] memory) {
        return array;
    }
}

contract StorageCollider is ArrayStorage {
    address private _address;

    constructor(address address_){
        _address = address_;
    }

    function collide() external override {
        (bool success,) = _address.delegatecall(abi.encodeWithSignature("makeArray()"));
        require(success, "Failed to cause a delegate call");
    }
}

contract Overrider {
    uint256[] private array;

    function makeArray() public {
        for(uint256 i = 1; i < 16; i++) {
            array.push(i);
        }
    }
}