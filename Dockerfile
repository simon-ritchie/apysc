FROM python:3.7.13-buster
ARG WORKDIR="/mnt/apysc/"
RUN mkdir ${WORKDIR}
WORKDIR "${WORKDIR}"
ADD requirements.txt ${WORKDIR}
RUN pip install -r requirements.txt
RUN playwright install chromium