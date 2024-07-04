// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.19;

struct Point {
    uint256 x;
    uint256 y;
}

contract UintStorage {
    uint256 private one;
    mapping(uint256 => Point) private pointMap;

    constructor() {
        one = 1;
        pointMap[12] = Point(12, 12);
    }

    function setNewValues(uint256 first, Point calldata point) external virtual {}

    function getStorageValuesSum() external view returns (uint256) {
        return one + pointMap[12].x + pointMap[12].y;
    }

    function getMapValue(uint256 key) external view returns (Point memory) {
        return pointMap[key];
    }
}

contract StrangeCalculator is UintStorage {
    function setNewValues(uint256 first, Point calldata point) external override {
        
        uint256 x = point.x;
        uint256 y = point.y;
        bytes32 slot_x =  keccak256(abi.encode(12, 1));
        bytes32 slot_y = bytes32(uint256(keccak256(abi.encode(12, 1))) + 1);

        assembly {
            sstore(0, first)
            sstore(slot_x, x)
            sstore(slot_y, y)   
        }
    }
}
