FROM python:3.7

WORKDIR /project

RUN apt-get upgrade && apt-get update
RUN python -m pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY main.py settings.py ./
RUN ls

CMD ["python", "main.py"]
