const TokenState = artifacts.require('TokenState');
const owner = '0x236B32a57a18018b1668f237FEfF4cB63905bb1E';
const deployerAccount = '0x236B32a57a18018b1668f237FEfF4cB63905bb1E';

module.exports = function(deployer) {
  deployer.deploy(TokenState, owner, deployerAccount);
}