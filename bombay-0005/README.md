# Bombay-0005

Testnet for Columbus-5.

[core@v0.5.0-beta1](https://github.com/terra-project/core/releases/v0.5.0-beta1) is used to run the testnet.

- The genesis is forked from the Tequila-0004 network at height #4095000.
- The genesis event for Bombay testnet will occur **Wednesday 10PM KST**

## Export Genesis
Export requires at least 16GB memory
```shell
$ terrad export --height 4095000 > exported-genesis.json
$ shasum ./exported-genesis.json
cf3f9761e54cf87e3b69ddbc4aa9dddfa0a539c6  ./exported-genesis.json
```

## Migrate Genesis
```shell
$ terrad migrate ./exported-genesis.json --chain-id=bombay-0005 --initial-height=4095001 --genesis-time=2021-05-26T13:00:00Z --replacement-cons-keys ./pubkey-replace.json > new-genesis.json
$ shasum ./new-genesis.json
9c5383c67edd0fc472ebbacbf675af0d3126a754  ./new-genesis.json
```

## How to Setup
**The validators who are not submit the pubkey replacement, should copy the node keys from the tequila node.**

```shell
$ git clone https://github.com/terra-project/core
$ git checkout v0.5.0-beta1
$ make install

$ terrad version --long
name: terra
server_name: terrad
version: 0.5.0-beta1
commit: 5ac5439e1d3ba17da0216181af9c09ca1155e63f
build_tags: netgo,ledger
go: go version go1.16.4 linux/amd64

$ terrad init
$ wget https://github.com/terra-project/testnet/blob/master/bombay-0005/genesis.json
$ cp genesis.json ~/.terra/config/genesis.json
# Set minium-gas-prices = "0.15uluna,0.1018usdr,0.15uusd,178.05ukrw,431.6259umnt,0.125ueur,0.97ucny,16ujpy,0.11ugbp,11uinr,0.19ucad,0.13uchf,0.19uaud,0.2usgd,4.62uthb,1.25usek"
$ nano ~/.terra/config/app.toml
$ terrad start
```
