FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY pixelforge.py .

RUN useradd --create-home --uid 10001 pixelforge

USER pixelforge

CMD ["python", "-u", "pixelforge.py"]