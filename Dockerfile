FROM python:3.6.12-buster
ARG WORKDIR="/mnt/action-py-script/"
RUN mkdir ${WORKDIR}
WORKDIR "${WORKDIR}"
RUN pip install typing-extensions==3.7.4.3
