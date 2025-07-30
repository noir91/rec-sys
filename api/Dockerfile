FROM python:3.10-slim

WORKDIR /app

COPY ./api/requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ./api /app/api

CMD ["python", "-m", "uvicorn", "api.app:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]

