// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "./token/ABaseNFT.sol";

// Implemented SBT 
contract SimpleNFT is ABaseNFT {
    mapping(uint256 => address) private soulboundTokens;

    constructor(string memory name, string memory symbol) ABaseNFT(name, symbol) {}

    function mintTo(
        address receiver,
        uint256 tokenId,
        string calldata tokenURI
    ) external override onlyOwner {
        _mint(receiver, tokenId);
        _setTokenURI(tokenId, tokenURI);
    }

    function getUserTokens(address user) external view returns (uint256[] memory) {
        uint256 balance = balanceOf(user);

        uint256[] memory tokens = new uint256[](balance);

        for (uint256 i = 0; i < balance; i++) {
            tokens[i] = tokenOfOwnerByIndex(user, i);
        }

        return tokens;
    }

    function getSoulboundTokenOwner(uint256 tokenId) external view returns (address) {
        return soulboundTokens[tokenId];
    }

    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId,
        uint256 batchSize
    ) internal override(ABaseNFT) {
        super._beforeTokenTransfer(from, to, tokenId, batchSize);

        if (from != address(0) && to != address(0) && from != to) {

            _soulbind(tokenId, from, to);
        }
    }

    function _soulbind(
        uint256 tokenId,
        address from,
        address to
    ) internal {
        
        require(!_isSoulbound(tokenId), "SimpleNFT: token is already soulbound");
        require(ownerOf(tokenId) == from, "SimpleNFT: token not owned by sender");

        soulboundTokens[tokenId] = to;
    }

    function _isSoulbound(uint256 tokenId) internal view returns (bool) {
        
        return soulboundTokens[tokenId] != address(0);
    }
}