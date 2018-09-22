FROM python:alpine

COPY ./requirements.txt .
RUN pip install -r requirements.txt

ENV APP_HOME /workspace
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

COPY . .

CMD sh
