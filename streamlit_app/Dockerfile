# app/Dockerfile

FROM python:3.10-slim

WORKDIR /app

COPY ./streamlit_app/requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

COPY ./streamlit_app /app/streamlit_app

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

CMD ["streamlit", "run", "streamlit_app/st_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
