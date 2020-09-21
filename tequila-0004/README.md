# Public Testnet for Columbus-4
 
## Timelines

* September 3, 2020 06:00 KST, Collect Genesis Addresses
* September 3, 2020 09:00 KST, Release penultimate genesis
* September 4, 2020 00:00 KST, Collect Genesis Transactions
* September 4, 2020 00:30 KST, Release genesis and seed node address
* September 4, 2020 15:00 KST, Launch Tequila-0004 network


## How to submit Genesis Address
Add your address line on the last part of [address.json](address.json) via Pull Request.

## How to generate Genesis Transaction
Download the `penultimate-genesis.json`, which will be released after we gather all Genesis Accounts, and place that file to `~/.terrad/config/genesis.json` and execute following command. 
```
terrad gentx --name my_account --amount 10000000000uluna
```

The file will be store in `~/.terrad/config/gentx/gentx-xxxx.json`. Please upload `gentx-xxxx.json` file to [gentx](gentx) folder via Pull Request.

## Configuration
### Minimum Gas Prices
We recommend you to define gas prices in ~/.terrad/config/app.toml as below
```
minimum-gas-prices = "0.15uluna,0.15uusd,0.1018usdr,178.05ukrw,431.6259umnt"
```

### Seed Node
Define seeds in ~/.terrad/config/config.toml
```
seeds = "b8d00ea1a68092f2963f8bfb8bf3dd7010e688f8@public-seed2.terra.dev:36656"
```

### Persistent Peer
Only specify it when the seed node is not working well
```
persistent_peers = "9ab68536fdaed15ea4377e8d9b2c56cb67057287@15.164.0.235.26656"
```
