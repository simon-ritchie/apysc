FROM python:3.6.12-buster
ARG WORKDIR="/mnt/apysc/"
RUN mkdir ${WORKDIR}
WORKDIR "${WORKDIR}"
RUN pip install -r requirements.txt
