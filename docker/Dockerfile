FROM python:3.8

WORKDIR /app 
COPY . .

RUN pip install - requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]