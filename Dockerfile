FROM tensorflow/tensorflow:2.5.0

WORKDIR /app
COPY . .

EXPOSE 5000

RUN pip install -r requirements.txt

CMD ["python", "app.py"]