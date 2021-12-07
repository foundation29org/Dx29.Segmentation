FROM python:3.7

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN python -m nltk.downloader popular

COPY . /app

EXPOSE 8080

WORKDIR /app
ENTRYPOINT ["python", "app.py"]
