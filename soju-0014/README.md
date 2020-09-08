## Core
You need go1.13 or later.

#### Download binary
* link: https://github.com/terra-project/core/releases/tag/v0.3.7

Put binaries into path. You should verify installation by executing ```terrad version --long```

#### Compile from the source
```
git clone https://github.com/terra-project/core
cd core
git checkout v0.3.7`
make install
```

## Genesis
- Initialize network by `terrad init` (`terrad unsafe-reset-all` for after initial init)

- Download genesis.json to ~/.terrad
```
wget -qO- https://raw.githubusercontent.com/terra-project/testnet/master/soju-0014/genesis.json
```

## Persistent Peers
Open $HOME/.terrad/config/config.toml and edit a line starting with `persistent_peers` as below.
```
persistent_peers = "1e1677e4ed9acf4e28de40b67ac01554aed1a29e@52.78.69.160:26656"
```
