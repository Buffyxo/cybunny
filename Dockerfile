FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

COPY templates/ ./templates/

COPY static/ ./static/

ENV APP_ENV=Production

ENV APP_VERSION=2.0

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5001", "app:app"]
