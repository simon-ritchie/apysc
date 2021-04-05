# Please don't bundle each RUN command for the sake of shorten build time.
FROM python:3.6.12-buster
ARG WORKDIR="/mnt/apysc/"
RUN mkdir ${WORKDIR}
WORKDIR "${WORKDIR}"
RUN pip install typing-extensions==3.7.4.3
RUN pip install pytest==6.2.2
RUN pip install twine==3.2.0
RUN pip install pytest-cov==2.11.1
RUN pip install pytest-parallel==0.1.0
RUN pip install retrying==1.3.3
RUN pip install future-annotations==1.0.0
RUN pip install autoflake==1.4
RUN pip install isort==5.7.0
RUN pip install autopep8==1.5.5
RUN pip install flake8==3.8.4
RUN pip install numdoclint==0.1.6
RUN pip install mypy==0.800
RUN pip install html-minifier==0.0.4
