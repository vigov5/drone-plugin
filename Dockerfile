FROM ubuntu:14.04
MAINTAINER euclid1990

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    apt-utils \
    apt-transport-https \
    ca-certificates \
    software-properties-common \
    net-tools \
    openssh-server \
    python-simplejson \
    python-pip \
    zip \
    vim

RUN apt-add-repository ppa:ansible/ansible
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends ansible

RUN mkdir /var/run/sshd && mkdir /root/.ssh/ && touch /root/.ssh/authorized_keys

COPY ./laravel /
COPY ./drone.py /scripts/drone.py

EXPOSE 22

ENTRYPOINT ["python", "/scripts/drone.py"]