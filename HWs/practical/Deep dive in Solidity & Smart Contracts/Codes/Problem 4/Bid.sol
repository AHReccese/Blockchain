pragma solidity ^ 0.5.1;

contract Bid {
    /// @notice This function generates the nonce and the hash needed in the Vickrey Auction.
    /// @param _bidValue is the desired bid.
    function generate(uint _bidValue) public view returns(uint, bytes32, bytes32) {
        
        uint value = _bidValue;
        bytes32 nonce = keccak256(abi.encodePacked(block.timestamp));
        bytes32 calculatedHash;
        calculatedHash = keccak256(abi.encodePacked(value,nonce));
        return (value, nonce, calculatedHash);
    }
}