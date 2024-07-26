FROM python:3.10

WORKDIR /usr/src

COPY /src .
COPY requirements.txt .

RUN apt-get update && apt-get install -y ffmpeg

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["bash"]
