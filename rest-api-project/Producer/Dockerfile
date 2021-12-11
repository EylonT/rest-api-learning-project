FROM ubuntu:latest
WORKDIR /app 
RUN apt update && apt upgrade -y && apt install python3-pip -y && apt clean all && apt autoremove -y
RUN useradd -ms /bin/bash -d /home/developer developer && chown developer:developer /app
USER developer
RUN pip3 install flask boto3 --user
ENV FLASK_APP=app
ENV FLASK_ENV=development
EXPOSE 5000
COPY Producer.py /app
CMD python3 Producer.py