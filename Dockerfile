FROM python:alpine3.21
COPY . /app/
WORKDIR /app/
RUN pip install -e .
CMD python -u hylebot.py