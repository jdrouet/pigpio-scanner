FROM python:3-slim

WORKDIR /code
COPY requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

COPY vw.py /code/vw.py
COPY main.py /code/main.py

CMD ["python", "-u", "main.py"]
