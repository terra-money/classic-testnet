# Terra Networks
![banner](./terra-networks.png)

This repo collects the genesis and configuration files for the various Terra testnets. 
It exists so the [Core repository](https://github.com/terra-project/core) does not get bogged down with large genesis files and status updates.

## Persistent Peers
Open $HOME/.terrad/config/config.toml and edit a line starting with `persistent_peers` as below.

**soju persistent peers**
```
persistent_peers = "1e1677e4ed9acf4e28de40b67ac01554aed1a29e@52.78.69.160:26656"
```
- terra 0.3.0-rc* based

**vodka persistent peers**
```
persistent_peers = "207b11829ba087f920c96ab11ec70f17b63e67ac@15.164.0.235:26656"
```
- terra 0.2.3 based

## Getting Started

To get started with the latest testnet, see the
[docs](https://docs.terra.money/guide/deploy-testnet).

## Testnet Status

### *Nov 18, 2019 17:50 UTC*
- soju-0010 live

### *Aug 19, 2019
- soju-0009 retired

### *July 26, 2019 05:20 UTC*
- vodka started

### *April 22, 2019 15:46 UTC* - Soju-0008
- terra 0.1.1 based

### *April 19, 2019 07:00 UTC* - Columbus-drill (retired)

- `columbus-drill` Launching Columbus-drill
- cosmos 0.34.0 based
- terra 0.1.0-rc0 based

### *April 11, 2019 04:00 UTC* - Soju-0007 (retired)

- `soju--0007` Launching Soju-0007
- cosmos 0.33.0 based
- terra 0.0.7 based


### *April 4, 2019 04:00 UTC* - Soju-0006 (retired)

- `soju--0006` Launching Soju-0006
- cosmos 0.32.0 based

### *January 8, 2018 04:00 UTC* - Soju-0005 (retired)

- `soju--0005` Launching Soju-0005
- cosmos 0.32.0 based

### *January 8, 2018 04:00 UTC* - Soju-0004 (retired)

- `soju--0004` Launching Soju-0004
- market module added
- fauset account added

### *January 7, 2018 08:00 UTC* - Soju-0003 (retired)

- `soju--0003` Launching Soju-0003
- oracle, subsidy, treasury included

### *December 18, 2018 03:00 UTC* - Soju-0002 (retired)

- `soju--0002` Launching Soju-0002

### *December 5, 2018 11:40 UTC* - Terra-0001 (retired)

- `terra--0001` Launching Terra-0001

### *November 28, 2018 23:00 UTC* - Terra-0000 (retired)

- `terra--0000` Launching Terra-0000

