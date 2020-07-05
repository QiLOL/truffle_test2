const PublicEST = artifacts.require('PublicEST');
const proxy_addr = "0x7565B6Bcaa94d52Ac4C2B700B3d0B15e4bDb5106";
const tokenState_addr = "0x63bec50139b822C0F244785cF39Ff53e79b87626";
const name = "AA";
const symbol = "BB";
const totalSupply= 1e8;
const owner = '0x236B32a57a18018b1668f237FEfF4cB63905bb1E';


module.exports = function(deployer) {
  deployer.deploy(PublicEST, proxy_addr, tokenState_addr,name, symbol,totalSupply,owner);
}