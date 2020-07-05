let Web3 = require("web3");
//const Tx = require('ethereumjs-tx')
var fs = require('fs');


const my_address = '0x8c3267038d70a793ad76feb8afc7d62f698276d7'
const privKey = 'F77407D035DEFAA676DBD8F4A8D3D9F0CAAD3282AC2034AEA4C5028755F65C1F' 

const token_json = fs.readFileSync('build/contracts/DemoToken.json', 'utf8');
const token_abi = JSON.parse(token_json)['abi'];
const proxy_json = fs.readFileSync('build/contracts/ProxyERC20.json', 'utf8');
const proxy_abi = JSON.parse(proxy_json)['abi'];

const token_address = '0xD66C3393FeD52Eec9E662E967C57070aAcF1cf59';
const proxy_address = '0xdee0e92AA2bD1Be10F865CA07170Dc647767A236';
const token_contract = new web3.eth.Contract(token_abi, token_address);
const proxy_contract = new web3.eth.Contract(proxy_abi, proxy_address);

// token_contract.methods.initializetoken(proxy_address).send({
//     from: my_address,
// }).then(() => {
//     token_contract.methods.proxyTemplate().call((err, result) => {
//         console.log(`\n\nSuccessfully initialized Uniswap token with template: ${result}`);
//     });
// }).catch(console.log);

const token1_address = '0x6B38b46aB309fEA5373553ab2779DA9810ba505D';
token_contract.methods.createproxy(token1_address).send({
    from: my_address,
}).then(() => {
  token_contract.methods.getproxy(token1_address).call((err, result) => {
      console.log(`Successfully created a new proxy for token1 at ${result}`);
  });
})

const token2_address = '0x6B38b46aB309fEA5373553ab2779DA9810ba505D';
token_contract.methods.createproxy(token2_address).send({
    from: my_address,
}).then(() => {
  token_contract.methods.getproxy(token2_address).call((err, result) => {
      console.log(`Successfully created a new proxy for token2 at ${result}`);
  });
})



