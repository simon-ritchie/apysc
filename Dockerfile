FROM python:3.6.12-buster
ARG WORKDIR="/mnt/apysc/"
RUN mkdir ${WORKDIR}
WORKDIR "${WORKDIR}"
ADD requirements.txt ${WORKDIR}
RUN pip install -r requirements.txt
