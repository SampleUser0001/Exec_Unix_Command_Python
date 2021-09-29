# 任意のイメージを取得
FROM node:latest

RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

RUN apt update && apt -y upgrade
RUN apt install -y python3
# RUN alias python="python3"
# RUN python --version
# RUN python3 --version

WORKDIR /tmp
RUN curl -O https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py 

RUN python3 -m pip install --upgrade pip
RUN pip install python-dotenv

WORKDIR /opt/app

COPY app /opt/app

RUN chmod 755 /opt/app/start.sh

RUN python3 --version

RUN npm search aws-sdk


# ENTRYPOINT [ "/opt/app/start.sh" ]
