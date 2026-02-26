FROM python:3.12
WORKDIR /code
COPY requirements.txt .
ENV PYTHONUNBUFFERED=1
RUN pip install -r requirements.txt
COPY test.py .
CMD [ "python", "./test.py" ]