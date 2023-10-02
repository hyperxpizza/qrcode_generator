FROM python:3.6.9

WORKDIR /app 
COPY . .
RUN pip install -r requirements.txt

RUN ls -la .

EXPOSE 8080     

CMD ["python", "./app.py"]