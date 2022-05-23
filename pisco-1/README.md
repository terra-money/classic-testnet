# Pisco-1

Testnet for Terra 2.0.

[core@v2.0.0-rc.0](https://github.com/terra-money/core/releases/v2.0.0-rc.0) should be used to run the testnet.

- The genesis event for Pisco-1 testnet will occur **2022-05-23T15:00:00Z (UTC)**


## How to Setup

```shell
$ git clone https://github.com/terra-money/core
$ git checkout v2.0.0-rc.0
$ make install

$ terrad version --long
name: terra
server_name: terrad
version: v2.0.0-rc.0
commit: e993d6d4fa1447b338d88914dee5d1bab6560e82
build_tags: netgo
go: go version go1.18.2 linux/amd64

$ terrad init [moniker] --chain-id pisco-1
$ wget https://raw.githubusercontent.com/terra-money/testnet/master/pisco-1/genesis.json
$ cp genesis.json ~/.terra/config/genesis.json
$ sed -i 's/minimum-gas-prices = "0uluna"/minimum-gas-prices = "0.15uluna"/g' ~/.terra/config/app.toml

# This will prevent continuous reconnection try
$ sed -i 's/external_address = ""/external_address = "[YOUR_EXTERNAL_IP_ADDRESS:PORT]"/g' ~/.terra/config/config.toml

$ terrad start
```

### Seed Nodes
```
c08d5b3d253bea18b24593a894a0aa6e168079d3@34.232.34.124:26656
```

### Known Peers
```
a4a8fbd7d26242263250a1d3ecb39f113832534b@52.73.183.21:26656
3a4c8f4d75781f39b558c3889157acfaa144a793@50.19.18.17:26656
```
