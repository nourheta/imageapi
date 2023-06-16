FROM python:3.9

COPY . /app/src
COPY ./requirements.txt /app

WORKDIR /app

RUN pip3 install -r requirements.txt

RUN apt update -y

RUN apt install libgl1-mesa-glx -y

RUN apt install zip -y

RUN cd src

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host=0.0.0.0", "--reload"]