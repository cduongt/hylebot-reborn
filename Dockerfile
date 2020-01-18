FROM python:alpine3.7
COPY . /app/
WORKDIR /app/
RUN pip install -e .
CMD python -u hylebot.py