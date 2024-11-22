FROM python:3.13-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "--workers=2", "-b", "0.0.0.0:8000", "--access-logfile", "-", "echoserver:create_app()"]
