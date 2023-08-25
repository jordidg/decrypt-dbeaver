FROM --platform=${BUILDPLATFORM} python:3.11.4-alpine3.18

ARG BUILDPLATFORM

WORKDIR /usr/src/decrypt_dbvis

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./decrypt_dbeaver.py .
CMD ["python", "decrypt_dbeaver.py", "/config"]
