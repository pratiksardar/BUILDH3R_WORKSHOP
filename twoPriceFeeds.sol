// SPDX-License-Identifier: MIT
pragma solidity 0.8.22;

import "@api3/contracts/api3-server-v1/proxies/interfaces/IProxy.sol";
import "@openzeppelin/contracts/access/Ownable.sol";


contract API3PriceFeed is Ownable {
    address public proxyAddress1;
    address public proxyAddress2;

    constructor() Ownable(msg.sender) {}

    // Securely update the proxy address for the first price feed
    function setProxyAddress1(address _proxyAddress) public onlyOwner {
        proxyAddress1 = _proxyAddress;
    }

    // Securely update the proxy address for the second price feed
    function setProxyAddress2(address _proxyAddress) public onlyOwner {
        proxyAddress2 = _proxyAddress;
    }

    // Retrieve the latest data from the first price feed
    function readDataFeed1() public view returns (uint256, uint256) {
        (int224 value, uint256 timestamp) = IProxy(proxyAddress1).read();
        uint256 price = uint224(value);
        return (price, timestamp);
    }

    // Retrieve the latest data from the second price feed
    function readDataFeed2() public view returns (uint256, uint256) {
        (int224 value, uint256 timestamp) = IProxy(proxyAddress2).read();
        uint256 price = uint224(value);
        return (price, timestamp);
    }
}
