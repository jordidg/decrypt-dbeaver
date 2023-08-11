FROM python:3

WORKDIR /usr/src/decrypt_dbvis

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./decrypt_dbeaver.py .
CMD ["python", "decrypt_dbeaver.py", "/config"]
