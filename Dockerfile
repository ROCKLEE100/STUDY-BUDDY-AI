FROM python:3.10-slim


ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1


WORKDIR /app

RUN apt-get update && apt-get install -y \
build-essential \
curl \
&& /var/lib/apt/list/*


COPY . . 


RUN apt-install --no-cache-dir -e .

EXPOSE 8501 

CMD ["streamlit", "run", "application.py", "--server.port=8501", "--server.address=0.0.0.0","--server.headless=true"]

