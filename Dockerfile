FROM python:3.6.12-buster
ARG WORKDIR="/mnt/action-py-script/"
RUN mkdir ${WORKDIR}
WORKDIR "${WORKDIR}"
RUN pip install typing-extensions==3.7.4.3
RUN pip install pytest==6.2.2
RUN pip install twine==3.2.0
RUN pip install pytest-cov==2.11.1
