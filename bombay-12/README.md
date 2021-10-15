# Bombay-12

Testnet for Columbus-5.

[core@v0.5.5](https://github.com/terra-money/core/releases/v0.5.5) will be used.

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
# terrad@v0.5.5
$ terrad migrate ./exported-genesis.json --chain-id=bombay-12 --initial-height=5900001 --genesis-time=2021-09-28T09:00:00Z --replacement-cons-keys ./pubkey-replace.json > new-genesis.json
$ jq -S -c -M "" ./new-genesis.json | shasum -a 256
50d450bc48bbec790de670e9d2195f04feef15bc3341ef143085c1b5ac0111fc ./new-genesis.json
```

## How to Setup
**The validators who did not submit the pubkey replacement, should copy the node keys from the tequila node.**

```shell
$ git clone https://github.com/terra-money/core
# validators please use v0.5.5-oracle tag
$ git checkout v0.5.5
$ make install

$ terrad version --long
name: terra
server_name: terrad
version: 0.5.5
commit: d8e277626e74f9d6417dcd598574686882f0274c
build_tags: netgo,ledger
go: go version go1.16.5 darwin/amd64

$ terrad init [moniker] --chain-id bombay-12
$ wget https://raw.githubusercontent.com/terra-money/testnet/master/bombay-12/genesis.json
$ cp genesis.json ~/.terra/config/genesis.json
$ sed -i 's/minimum-gas-prices = "0uluna"/minimum-gas-prices = "0.15uluna,0.1018usdr,0.15uusd,178.05ukrw,431.6259umnt,0.125ueur,0.97ucny,16.0ujpy,0.11ugbp,11.0uinr,0.19ucad,0.13uchf,0.19uaud,0.2usgd,4.62uthb,1.25usek,1.164uhkd,0.9udkk,1.25unok,2180.0uidr,7.6uphp"/g' ~/.terra/config/app.toml
$ terrad start
```

### Download the Address Book

[addrbook.json](addrbook.json)

After the file is downloaded, put it in the the `~/.terra/config` directory.

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
