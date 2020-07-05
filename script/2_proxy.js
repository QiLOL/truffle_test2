const ProxyERC20 = artifacts.require('ProxyERC20');

module.exports = function(deployer) {
  deployer.deploy(ProxyERC20, '0x236B32a57a18018b1668f237FEfF4cB63905bb1E');
}