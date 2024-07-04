// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.9;

interface IDataTypesPractice {
    function getInt256() external view returns (int256);

    function getUint256() external view returns (uint256);

    function getInt8() external view returns (int8);

    function getUint8() external view returns (uint8);

    function getBool() external view returns (bool);

    function getAddress() external view returns (address);

    function getBytes32() external view returns (bytes32);

    function getArrayUint5() external view returns (uint256[5] memory);

    function getArrayUint() external view returns (uint256[] memory);

    function getString() external view returns (string memory);

    function getBigUint() external pure returns (uint256);
}

contract DataTypesPractice is IDataTypesPractice{

    int256 private Int256;
    uint256 private Uint256;
    int8 private Int8;
    uint8 private Uint8;
    bool private Bool;
    address private Address;
    bytes32 private Bytes32;
    uint256[5] private ArrayUint5;
    uint256[] private ArrayUint;
    string private String;

    constructor(){
        Int256 = -314;
        Uint256 = 314;
        Int8 = -1;
        Uint8 = 255;
        Bool = true;
        Address = address(0x1234567890123456789012345678901234567890);
        Bytes32 = 0x1234567890123456789012345678901234567890123456789012345678901234;

        uint256[5] memory arr;
        arr[0] = 1;
        arr[1] = 2;
        arr[2] = 3;
        arr[3] = 4;
        arr[4] = 5;
        ArrayUint5 = arr;

        uint256[] memory ar = new uint256[](3);
        ar[0] = 1;
        ar[1] = 2;
        ar[2] = 3;
        ArrayUint = ar;

        string memory str = "Hello World!";
        String = str;
    }

    function getInt256() external view returns (int256){
        return Int256;
    }

    function getUint256() external view returns (uint256){
        return Uint256;
    }

    function getInt8() external view returns (int8){
        return Int8;
    }

    function getUint8() external view returns (uint8){
        return Uint8;
    }

    function getBool() external view returns (bool){
        return Bool;
    }

    function getAddress() external view returns (address){
        return Address;
    }

    function getBytes32() external view returns (bytes32){
        return Bytes32;
    }

    function getArrayUint5() external view returns (uint256[5] memory){
        return ArrayUint5;
    }

    function getArrayUint() external view returns (uint256[] memory){
        return ArrayUint;
    }

    function getString() external view returns (string memory){
        return String;
    }

    function getBigUint() external pure returns (uint256){
        uint256 v1 = 1;
        uint256 v2 = 2;

        return ~v2;
    }
}