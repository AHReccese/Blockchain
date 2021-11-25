pragma solidity ^ 0.5.1;

import "./Auction.sol";

contract CustomAuction is Auction {

    enum Phase { Pending, Commitment, Opening, Finished }
    
    Phase public phase;

    uint startPhaseBlock;
    uint startOpeningBlock;

    uint commitment_len;
    uint opening_len;

    address payable lowestBidder;
    uint lowestBid;
    uint ReserveFund;

    bool firstOpen = true;

    struct Bid {
        bytes32 FileAddress;
        uint value;
        bytes32 calculatedHash;
        bytes32 nonce;
        bool exists;
    }

    mapping(address => Bid) bids;
    
    // address of accounts admin choose in Opening phase
    mapping(address => bool) chooses;

    event openingStarted();
    
    constructor(address payable _admin,uint _commitment_len,uint _opening_len) public payable {
        
        require( _admin > address(0) );
        // adding thresholding.
        commitment_len = _commitment_len;
        opening_len = _opening_len;
        phase = Phase.Pending;

        description.startBlock = block.number;
        
        description.admin = _admin;
        ReserveFund = msg.value;
   
    }

    /// @dev This modifier allow to invoke the function olny during the Commitment phase.
    modifier duringCommitment {
        require(phase == Phase.Commitment);
        _;
    }

    /// @dev This modifier allow to invoke the function olny during the Opening phase.
    modifier duringOpening {
        require(phase == Phase.Opening);
        _;
    }
    
    function getReserveFund() public view returns (uint256) {
        return ReserveFund;
    }
    
    function getFile( address add ) public view returns ( bytes32 fileAdd) {
        // check if there is a bid with this address 
        require(bids[add].exists);
        return bids[add].FileAddress;
    }
    
    /// @notice This function will activate the auction.
    function activateAuction() public onlyAdmin {
        require(phase == Phase.Pending);
        phase = Phase.Commitment;
        startPhaseBlock = block.number;
        emit auctionStarted();
    }

    ///@notice This function allow people to make bid.
    ///@notice Note that a bid will be taken into account if the value sent is >= the minimum deposit.
    ///@dev This function can be invoked only during the commitment phase.
    ///@param _bidHash this is the hash of the tuple <value,nonce>. See `GenerateBid` contract for more info.
    function bid(bytes32 _bidHash, bytes32 _FileAddress) public duringCommitment payable {

        require( (block.number - startPhaseBlock) <= commitment_len );
        
        // The bidder should not be able to send another bid.   
        //require(!bids[msg.sender].exists);

        Bid memory bid_create = Bid(
            _FileAddress,
            0,
            _bidHash,
            0,
            true
        );

        bids[msg.sender] = bid_create;

    }

 
    ///@notice This function activate the Opening phase
    function startOpening(address add1, address add2, address add3) public onlyAdmin {
        
        require(firstOpen == true);
        require(bids[add1].exists);
        require(bids[add2].exists);
        require(bids[add3].exists);
        
        firstOpen = false;
        
        chooses[add1] = true;
        chooses[add2] = true;
        chooses[add3] = true;
        
        startOpeningBlock = block.number;
        phase = Phase.Opening;
        
        emit openingStarted();

    }

    ///@notice This function allow people to open their bid.
    function open( uint value, bytes32 _nonce) public duringOpening {
        
        if((block.number - startOpeningBlock) <= opening_len ){
            // is this fund possible :)?
            require(value <= ReserveFund); 

            // Control the correctness of the bid
            Bid memory bid_open = bids[msg.sender];
            bytes32 thisNonceHash =  keccak256(abi.encodePacked(value,_nonce));
            require(thisNonceHash == bid_open.calculatedHash ); 

            // Update the bid status
            bid_open.value = value;
            bid_open.nonce = _nonce;

            // existance among chooses 
            if(/* existance check */ chooses[msg.sender] ){
                if( lowestBid!= 0 ){
                    if(lowestBid >= value){
                        lowestBid = value;
                        lowestBidder = msg.sender;
                    }
                }else{
                    lowestBid = value;
                    lowestBidder = msg.sender;
                }
            }

        }else{
                // semi auto finalize :) .
                phase = Phase.Finished;
                finalize();
        }

    }


    ///@notice This function finalize and close the contract.
    function finalize() public adminOrAutomaticTimeOutFinalize {

        // emergency Admin Finalizing...
        if(phase != Phase.Finished){
            phase = Phase.Finished;
        }

        description.winnerAddress = lowestBidder;
        description.winnerBid = lowestBid;
        lowestBidder.transfer(lowestBid);
        description.admin.transfer(ReserveFund - lowestBid);
        emit auctionFinished(lowestBidder,lowestBid);
        selfdestruct(description.admin); 

    }


    modifier adminOrAutomaticTimeOutFinalize() { 
        if(msg.sender == description.admin){
            require((block.number - startOpeningBlock) >= opening_len );
        }else{
            require(phase == Phase.Finished);
        }
        _;
    }

}
