# Decrypt DBeaver

Decrypt DBeaver config,
based on <https://gist.github.com/felipou/50b60309f99b70b1e28f6d22da5d8e61>

## Run decrypter using Docker

`docker run --rm --mount type=bind,source=$HOME/Library/DBeaverData/workspace6/General/.dbeaver/,target=/config,readonly ghcr.io/jordidg/decrypt_dbeaver`
