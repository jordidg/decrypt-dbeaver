# Decrypt DBeaver

Decrypt DBeaver config,
based on <https://gist.github.com/felipou/50b60309f99b70b1e28f6d22da5d8e61>

## Run Decrypter using Docker

1. Build: `docker build -t decrypt_dbeaver .`
2. Run: `docker run --mount type=bind,source=$HOME/Library/DBeaverData/workspace6/General/.dbeaver/,target=/config,readonly decrypt_dbeaver`
