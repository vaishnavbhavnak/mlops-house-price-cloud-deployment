FROM python:3.12-slim

WORKDIR /src 
COPY requirements.txt . 

RUN pip install --no-cache-dir -r requirements.txt 
COPY src ./src 
COPY models ./models 
EXPOSE 8001 
CMD ["sh","-c","uvicorn src.main:app --host 0.0.0.0 --port ${PORT:-8001}"]