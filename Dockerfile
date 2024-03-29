FROM python:3.11 as base

ARG PACKAGE_NAME="langchain-lamini"

# Install Ubuntu libraries
RUN apt-get -yq update

# Install python packages
WORKDIR /app/${PACKAGE_NAME}
COPY ./requirements.txt /app/${PACKAGE_NAME}/requirements.txt
RUN pip install -r requirements.txt

# Copy all files to the container
COPY ./scripts /app/${PACKAGE_NAME}/scripts
COPY ./lamini_langchain /app/${PACKAGE_NAME}/lamini_langchain

WORKDIR /app/${PACKAGE_NAME}

RUN chmod a+x /app/${PACKAGE_NAME}/scripts/start.sh

ENV PACKAGE_NAME=$PACKAGE_NAME

ENTRYPOINT ["/app/langchain-lamini/scripts/start.sh"]
