FROM ubuntu:latest
WORKDIR /app 
RUN apt update && apt upgrade -y && apt install python3-pip -y && apt clean all && apt autoremove -y
RUN useradd -ms /bin/bash -d /home/developer developer && chown developer:developer /app
USER developer
RUN pip3 install flask boto3 PyYAML pandas --user
COPY Consumer.py /app
CMD while true; do python3 Consumer.py; done