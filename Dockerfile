FROM python:3.11-slim-bookworm

WORKDIR /portfolio-service

COPY ./src/ .

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libc-dev \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && apt-get purge -y --auto-remove gcc libc-dev \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 5001

CMD ["python", "./__main__.py"]