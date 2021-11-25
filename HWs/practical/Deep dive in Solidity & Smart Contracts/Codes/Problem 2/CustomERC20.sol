pragma solidity ^0.5.1;

import "./SafeMath.sol";


contract ERC20Interface {
    
  function totalSupply() public view returns (uint256);
  function balanceOf(address who) public view returns (uint256);
  function transfer(address to, uint256 value) public returns (bool);
  function allowance(address owner, address spender) public view returns (uint256);
  function transferFrom(address from, address to, uint256 value) public returns (bool);
  function approve(address spender, uint256 value) public returns (bool);

  event Approval(address indexed owner, address indexed spender, uint256 value);
  event Transfer(address indexed from, address indexed to, uint256 value);
}

contract ERC20 is ERC20Interface {
    using SafeMath for uint256;

    // who owns how many tokens
    mapping(address => uint256) balances;
    // account "A" allows account "B" to extract "X" amount
    mapping(address => mapping(address => uint256)) internal allowed;
    // total amount of money.
    uint256 _totalSupply;

    constructor(uint256 total) public {
        _totalSupply = total;
        balances[msg.sender] = _totalSupply;
    }

    function totalSupply() public view returns (uint256) {
        return _totalSupply;
    }

    function balanceOf(address who) public view returns (uint256) {
        return balances[who];
    }

    function transfer(address to, uint256 value) public returns (bool) {
        // check to see if there is enough amount of money in sender's account.
        require(value <= balances[msg.sender]);
        // withdraw from sender's account 
        balances[msg.sender] = balances[msg.sender].sub(value);
        // deposit to receiver's account
        balances[to] = balances[to].add(value);
        // broadcast event.
        emit Transfer(msg.sender, to, value);
        return true;
    }

    function allowance(address owner, address spender) public view returns (uint256) {
        return allowed[owner][spender];
    }

    function transferFrom(address from, address to, uint256 value) public returns (bool) {
        // check to see if there is enough amount of money in sender's account.
        require(value <= balances[from]);
        require(value <= allowed[from][msg.sender]);

        // withdraw
        balances[from] = balances[from].sub(value);
        allowed[from][msg.sender] = allowed[from][msg.sender].sub(value);
        // deposit
        balances[to] = balances[to].add(value);
        emit Transfer(from, to, value);
        return true;
    }

    function approve(address spender, uint256 value) public returns (bool) {
        allowed[msg.sender][spender] = value;
        emit Approval(msg.sender, spender, value);
        return true;
    }
}
