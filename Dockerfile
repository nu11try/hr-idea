FROM python:3

WORKDIR /srv

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./ .

CMD ["python", "./main.py"]
