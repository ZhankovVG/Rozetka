FROM python

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/src/Rozetka

WORKDIR /usr/src/Rozetka

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["./entrypoint.sh"]