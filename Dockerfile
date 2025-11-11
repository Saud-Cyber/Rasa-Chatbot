FROM python:3.7-slim

RUN python -m pip install --upgrade pip
RUN python -m pip install rasa
WORKDIR /app
COPY . .

RUN rasa train
USER 1001

EXPOSE 5005
ENTRYPOINT [ "rasa" ]
CMD ["run", "--enable-api", "--cors", "*", "--debug"]
