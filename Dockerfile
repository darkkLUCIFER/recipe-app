FROM python:3.12-slim

MAINTAINER mdn1376@gmail.com

ENV PYTHONUNBUFFERED=1\
    PYTHONDONTWRITEBYTECODE=1\
    APP_HOME=/app

ARG REQUIREMENTS_FILE

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    rm -rf /var/lib/apt/lists/*

WORKDIR ${APP_HOME}

COPY requirements/ requirements/
COPY requirements.txt requirements_dev.txt ./

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r ${REQUIREMENTS_FILE}

COPY . ${APP_HOME}

RUN useradd -m user
USER user

