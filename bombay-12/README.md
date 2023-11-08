# Bombay-12

Testnet for Columbus-5.

[core@v0.5.9](https://github.com/terra-money/core/releases/v0.5.9) will be used.

- The genesis is forked from the tequila-0004 network at height `#5,900,000`.
- The genesis event for bombay-12 testnet will occur **2021-09-28T09:00:00Z (UTC)**

## Export Genesis
Export requires at least 32 GB memory
```shell
# terrad@v0.4.6
$ terrad export --height 5900000 > exported-genesis.json
$ jq -S -c -M "" ./exported-genesis.json| shasum -a 256
afa5a8077272f377e8e71b55b24409ea5469fc2ee5ab8c593c032f257f8b7f08 ./exported-genesis.json
```

## Migrate Genesis
```shell
# terrad@v0.5.9
$ terrad migrate ./exported-genesis.json --chain-id=bombay-12 --initial-height=5900001 --genesis-time=2021-09-28T09:00:00Z --replacement-cons-keys ./pubkey-replace.json > new-genesis.json
$ jq -S -c -M "" ./new-genesis.json | shasum -a 256
50d450bc48bbec790de670e9d2195f04feef15bc3341ef143085c1b5ac0111fc ./new-genesis.json
```

## How to Setup
**The validators who did not submit the pubkey replacement, should copy the node keys from the tequila node.**

```shell
$ git clone https://github.com/terra-money/core
# validators please use v0.5.9-oracle tag
$ git checkout v0.5.9
$ make install

$ terrad version --long
name: terra
server_name: terrad
version: 0.5.9
commit: 6235f92a101d203fddd26abc6c64799c546f7716
build_tags: netgo,ledger
go: go version go1.16.5 darwin/amd64

$ terrad init [moniker] --chain-id bombay-12
$ wget https://raw.githubusercontent.com/terra-money/testnet/master/bombay-12/genesis.json
$ cp genesis.json ~/.terra/config/genesis.json
$ sed -i 's/minimum-gas-prices = "0uluna"/minimum-gas-prices = "0.01133uluna,0.15uusd,0.104938usdr,169.77ukrw,428.571umnt,0.125ueur,0.98ucny,16.37ujpy,0.11ugbp,10.88uinr,0.19ucad,0.14uchf,0.19uaud,0.2usgd,4.62uthb,1.25usek,1.25unok,0.9udkk,2180.0uidr,7.6uphp,1.17uhkd"/g' ~/.terra/config/app.toml
$ terrad start
```

### Download the Address Book

[addrbook.json](addrbook.json)

After the file is downloaded, put it in the the `~/.terra/config` directory.

### Seed Nodes
```
e14dcea40de9b7cc31ea3e843c25bcdd8d91c36d@solarsys.noip.me:38656
7261b247dc05b8f8aca7a74529e5caf9c51d5379@162.55.132.48:15635
347e81ce9380e10b2c9838eb92a4f35b1ff5eb7a@162.55.131.238:15635
2b7150ff60df7b8bc1aa50ab586c18c7d9550171@3.130.148.2:26656
d61ee248c1b53a55cf93c60af4f4e9f7dd48b57b@seed.terra-testnet.everstake.one:26656
349aa6d91c5c072c0ae9d8f5412e3920ada71732@65.21.134.243:26656
d89ce884e0b431984fc8848efa9ecea8855ca070@terra-testnet.0base.vc:26656
1fffb76a7f6bcc0c8e1e25ec8e73171b38208522@laguz.coinbevy.com:26656
b583acaf6612b78cc0927614f2f60292bc58f6fc@35.81.139.246:26656
b2cfcfaefae15d7c8b6ee28a991b20be4126db21@terra-testnet-seed.larry.coffee:26656
3da66974005f1fc284e5a9aef869e45ee51ba0c0@terra-seed-testnet.blockngine.io:36676
4577101e210aa6389f075cdcd6c377f98ef57a84@bombay.inotel.ro:26656
bdc57c5a7f11040bed560fceb7d9b17c117e3423@seed-bombay.terra.01node.com:26656
41a6a0e9918a0f3976c81dda8991bd37b8d7ae31@tnet-seed.terra.nitawa.systems:27656
e455f2a0920414959e4620098d2a6068c720fcac@3.238.127.6:26656
f52c69954570f6f0cef7732009ad028d483b253a@bombay-seed01.stakers.finance:29656
b172ede8d2a6b1804d41819f0b61100a73a4aa0c@162.55.92.217:26656
344199da2be16adc58e7c7cf85607ee6d65f1eb4@seed.terra-testnet.lunarnode.org:26656
1c22d46f2ce87f2d8f7ee633cc67232590ca1b4b@seed01.autismcapital.xyz:3333
5be38e13bdfea97f500cdb5cde7ad40fd119c2fa@3.36.113.204:26656
0d544651127abf15cd8c1e3992757267018223c0@54.180.139.156:26656
4dd8633fb5a88c0e3c45dc2b5e173080d1ae64d3@148.251.14.48:26662
5baf0f86787b066acfc94122057026294d12c59e@bombay-seed.onestar.ee:26656
eb324ed42daf928a28db1c19aa9834968c5db26c@seed-testnet.moonshot.army:26656
c7fdeca4135e56149f5f5d84462c9eb9f059edb8@seed.terra.testnet.btcsecure.io:26656
2e5ee839dd7d42071399a7f09064afe49492b771@bombay2.aurastake.com:27656
778aee349324ef3b5b862f4f094a91f26e1c8ded@seed.terradactyl.io:40003
5f080fdec10663bf578ae6d0bff8aaf3a4ea49c0@63.35.218.188:20000
4bfcc9d65f21fadb84a4177c112a498a0dc86462@seed.leviathan.monster:26600
30faf19067be3660c1a24f8d7e40ede889251628@20.79.223.3:50000
7660dc2b1bc1dd688d703eaeb11456f0f90eb44d@20.79.222.189:26646
9628b2f8903e18dfa208527b3a74b4f76aaf2fb9@seed.terra.testnet.stakewith.us:47756
edfa33ed283ea40b7e6ef3683b2ccbf4b7a77d4f@seed.bombay.synergynodes.com:26656
c4e695a19e81989e96468475cffabfd81d669408@35.228.229.136:26650
5928ecce7e3ee70b4fd171b5b0141914ad947a0b@35.189.155.44:25656
b140f8847169a7bd852a214eb74eb52f0e628393@138.91.27.245:26856
05bf2a0786c34f07452f21a0d4fc00061224b59f@seed.terra.testnet.staker.space:26656
458edd0d8f93dd221cc8a7df7f7eaed9303da0f6@seed.bombay.terra.setten.io:26656
070f643051da07b84586794c13dcaf13d5ce8efd@139.59.181.204:26656
c23709c65da9446ad5c3e9b4e4613c2262cda989@95.216.241.103:26656
eb13d18465e9b8387b6dc3b73fc414032fc23fab@bombay.mcontrol.ml:36656
5e71188b711b65f8ef5a18fd08413bb7cf30c7d4@seed.terra-bombay.sabai.finance:26656
0ac871becd561e931f71825b50dc6d4a069dd80c@35.240.133.1:26680
12a7b4d0adfc6a6ccefe8d010578793cbbddb742@terra-testnet-seed-1.stakin-nodes.com:26656
1ac151ec5d0b29ebc893c907631849ae76eb2f93@terrabombay.stakely.io:26688
8ffc890f24985035857bc63e5ff13eaac1f77683@bombay-seed.terra.kkvalidator.com:26656
2308feb62147331889f13aef01417a91362c79f8@34.152.3.90:26670
c68bf400ab04b87563f8176b0246b5b68b809cd6@testnet.seed.terraindia.info:36656
22a020147ab5caaaf69654fa78bbcd3207cf8620@65.21.229.28:26656
af9758b222023e8e4013154de1c23cf755564be5@167.172.166.36:26656
0cc9fff2c57e5b3d2fcf2c91bba1e8b8cf1590ca@seed.terra-testnet.cosmicvalidator.com:26656
eb6fb5b290adc146e23453dbe9eb5c9b924775c1@20.199.97.106:36656
745a631ab71716d5eaf74c63b9c0c11f4be1d668@167.99.91.224:26656
0f9135a7e5ad341b1cee42bc5a79d4f5122ff638@34.79.212.227:27656
e260ab51f62a1cbf6d04b23192e665edd4f1176d@seed-testnet.terra.lunastations.online:36656
848466e05b6b64a87bfc23df6cb06771e07b1b4c@seed-testnet.terra.genesislab.net:26656
87c943b197d0ee9162eafc31a8664aa27cd6ad19@terra-testnet.bi23.com:21656
6958c0a62d72dd062a4e034b47b1586458ff8169@52.196.61.226:26666
8ac91044bb88781a6b90290ea0e47e43dfb9b43a@terra-testnet-seed.orbitalcommandvalidator.com:26312
02a99227cc192d423500ea753e3c05dc991da569@ec2-18-144-37-246.us-west-1.compute.amazonaws.com:26656
cc87ff83f9e35094df3f71de51a792e8ecf2efa0@terra-bombay-seed.blockstake.xyz:26656
37ffe148ecf6645d2e21e1703145c7828c22a268@13.234.69.239:26656
7c0d84fde67ebf7084ddf7a467e879d5d6442b57@194.163.162.199:26656
3abc165052e80746e543f4863d7d2bf6d00b528b@bombay-seed.blockscape.network:26656
9762192a79f88f37419d32f164a88e05ce024aec@168.119.150.243:26656
3aa011fc424956aa78015ec7372bfed213233e8c@95.168.165.205:26656
67f83663158a908b1a0784e642eafde880dd2929@terra.test.seed.forbole.com:26656
9e4110344ab9ae7864b0c102b77b68d003b85289@85.118.207.62:26656
```

### Known Peers
```
eb4168239744007adcce028a397fc2addf4b2520@54.150.118.40:36656
2e13408cbe993a291caf02946e902753f7f95a71@3.34.120.243:26656
67f83663158a908b1a0784e642eafde880dd2929@65.21.157.38:26656
f9cb325f1ca9296c2853c2f416991e34927e23f7@207.180.213.123:26656
c7fdeca4135e56149f5f5d84462c9eb9f059edb8@52.78.140.220:26656
bdc57c5a7f11040bed560fceb7d9b17c117e3423@193.239.85.118:26656
05bf2a0786c34f07452f21a0d4fc00061224b59f@138.201.60.238:26656
e6be82b4a659964fad27ee14f844c222fe9abadf@104.197.21.152:26656
2c7a1c74c793456209188a59fc01d9c7f139f5be@34.136.129.123:26656
9762192a79f88f37419d32f164a88e05ce024aec@168.119.150.243:26656
```

### Key Changes for Validator Setup
* `~/.terrad` home changed to `~/.terra`
* `$ terracli rest-server` removed, instead you can activate rest-server on `~/.terra/config/app.toml` by setting `enable = true` on `[api]` section.
* Swagger url changed to `:1317/swagger-ui/` to `:1317/swagger/`
* Please use `bombay` branch ecosystem tools
   - oracle feeder https://github.com/terra-money/oracle-feeder/releases/tag/v2.0.0
   - terra.js (`$ npm i -S @terra-money/terra.js@^2`)


Except these, you can also check changed configurations a lot, please check the changes and be familiar before Columbus-5 launching!


### Frequently Asked Questions
* **Error: invalid character 'e' in literal true (expecting 'r')**

   `$ terrad tendermint show-validator [--home]` command does not show bech32 encoded `terraconsvalpub` address, but show `'{"@type":"/cosmos.crypto.ed25519.PubKey","key":"bwVWtrsVrhimkACyF6lwLogwgWTtHUSnjVTl/20DLrw="}'` protobuf style interface JSON. so `$ terrad tx staking create-valdiator --pubkey` now receive this pubkey interface JSON string.
   ```
   $ terrad tx staking create-validator \
       --pubkey '{"@type":"/cosmos.crypto.ed25519.PubKey","key":"bwVWtrsVrhimkACyF6lwLogwgWTtHUSnjVTl/20DLrw="}' \
       ...
   ```
