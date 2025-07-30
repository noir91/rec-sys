# app/Dockerfile

FROM python:3.10-slim

WORKDIR /app

COPY ./requirements.txt ./app/requirements.txt
RUN pip3 install --no-cache -r requirements.txt

COPY ./streamlit_app /app/streamlit_app

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

CMD ["streamlit", "run", "streamlit/st_app.py", "--server.port=8501", "--server.address=0.0.0.0"]