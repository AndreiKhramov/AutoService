FROM python:3.13

WORKDIR autoservice

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ src/

RUN chmod +x src/scripts/entrypoint.sh

CMD ["sh", "src/scripts/entrypoint.sh"]