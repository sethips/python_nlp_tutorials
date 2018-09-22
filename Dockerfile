FROM python:alpine

COPY ./requirements.txt .
RUN pip install -r requirements.txt

ENV APP_HOME /workspace
RUN mkdir $APP_HOME
ENV NLTK_DATA /usr/local/share/nltk_data
RUN mkdir $NLTK_DATA
WORKDIR $APP_HOME

COPY . .

CMD sh
