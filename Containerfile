ARG PYTHON_VERSION=3.11
FROM python:${PYTHON_VERSION}-alpine

COPY . /data

# hadolint ignore=DL3018
RUN apk add --no-cache \
      bash \
      git \
      openssh-keygen \
      pwgen \
    && apk add --no-cache --virtual .build-deps \
      build-base \
      cargo \
      libffi-dev \
      openssl-dev \
      python3-dev \
      rust \
    && pip3 --no-cache-dir install --upgrade 'pip==22.3.1' \
    && pip3 --no-cache-dir install -r /data/requirements.txt \
    && apk del .build-deps \
    && mkdir /output

WORKDIR /data

VOLUME ["/output"]
CMD ["cookiecutter", "-o", "/output", "/data"]

LABEL "org.opencontainers.image.documentation"="https://docs.osism.tech" \
      "org.opencontainers.image.licenses"="ASL 2.0" \
      "org.opencontainers.image.source"="https://github.com/osism/cfg-cookiecutter" \
      "org.opencontainers.image.url"="https://www.osism.tech" \
      "org.opencontainers.image.vendor"="OSISM GmbH" \
      "org.opencontainers.image.title"="cookiecutter"
