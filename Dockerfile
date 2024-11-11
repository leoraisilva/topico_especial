FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app/python/services/projeto.json /app/python/services/projeto.json

COPY . .

EXPOSE 5000

CMD ["python", "app/__init__.py"]
