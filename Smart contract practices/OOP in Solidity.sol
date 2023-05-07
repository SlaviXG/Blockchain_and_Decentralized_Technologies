// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.19;

contract A {
    uint256 public a = 1;
    uint256 private deposited;

    constructor() {
        possibleRevert();
    }

    function deposit(uint256 amount) public virtual {
        require(amount > 0, "Amount is zero");

        deposited = amount;
    }

    function getDeposited() external view returns (uint256) {
        return deposited;
    }

    function possibleRevert() public pure virtual {
        revert("Oops");
    }
}

contract B is A {
    uint256 private b = a += 10;

    function deposit(uint256) public virtual override {
        revert("Deposit is blocked");
    }
}

contract C is A {
    uint256 private c = a *= 2;

    function deposit(uint256 amount) public virtual override {
        super.deposit(amount);
    }

    function getC() external view returns (uint256) {
        return c;
    }
}

contract D is C, B {

    function deposit(uint256 amount) public override(B, C) {
        
        A.deposit(amount);
    }

    function possibleRevert( ) public pure override {
        return;
    }
}
