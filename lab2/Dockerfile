#берем последний образ
FROM kalilinux/kali-rolling:latest
RUN  apt-get update &&  apt-get upgrade -y && apt-get install -y python3
RUN apt-get install -y exa
RUN apt-get install -y python3-pip
RUN pip3 install tqdm
RUN useradd -ms /bin/bash  casual
#автор - я
LABEL maintainer = "any441"
#выполнится на старте без судо, потому что я сразу рут
COPY main.py /home/
COPY install.py /home/
WORKDIR /home/
ENTRYPOINT python3 install.py && /bin/bash
# Запускаем инсталлер и подключаемся к башу
