FROM python:3
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

CMD [ "python", "./main.py" ]



# $ docker build -t bot .
# $ docker run --rm --name bot -d bot
# $ dcoker stop bot