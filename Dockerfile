FROM --platform=${BUILDPLATFORM} python:3.12.0-alpine3.18

ARG BUILDPLATFORM

LABEL org.opencontainers.image.title "Decrypt DBeaver"
LABEL org.opencontainers.image.description "Retrieve connection properties from DBeaver configuration files"

WORKDIR /usr/src/decrypt_dbvis

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./decrypt_dbeaver.py .
CMD ["python", "decrypt_dbeaver.py", "/config"]
