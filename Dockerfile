FROM python:3.12-slim

MAINTAINER mdn1376@gmail.com

ENV PYTHONUNBUFFERED=1\
    PYTHONDONTWRITEBYTECODE=1\
    APP_HOME=/app

ARG REQUIREMENTS_FILE

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    apt-get install libpq-dev postgresql-client -y && \
#    apt-get install jpeg-dev musl-dev zlib zlib-dev && \
    rm -rf /var/lib/apt/lists/*

WORKDIR ${APP_HOME}

COPY requirements/ requirements/
COPY requirements.txt requirements_dev.txt ./

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r ${REQUIREMENTS_FILE}

COPY . ${APP_HOME}

RUN mkdir -p "/vol/web/media/"
RUN mkdir -p "/vol/web/static"
RUN useradd -m user
RUN chown -R user:user /vol/
RUN chown -R 755 /vol/
USER user

