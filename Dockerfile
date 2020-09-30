FROM python:3.6.9

WORKDIR /app
COPY . /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8080

CMD ["python3", "app.py"]