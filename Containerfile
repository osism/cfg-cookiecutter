ARG PYTHON_VERSION=3.10
FROM python:${PYTHON_VERSION}-alpine

COPY requirements.txt /tmp/requirements.txt

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
    && pip3 --no-cache-dir install --upgrade 'pip==24.0' \
    && pip3 --no-cache-dir install -r /tmp/requirements.txt \
    && apk del .build-deps \
    && mkdir /output

COPY . /data

WORKDIR /data

VOLUME ["/output"]

ENTRYPOINT ["/data/entrypoint.sh"]

LABEL "org.opencontainers.image.documentation"="https://osism.github.io/docs/intro" \
      "org.opencontainers.image.licenses"="ASL 2.0" \
      "org.opencontainers.image.source"="https://github.com/osism/cfg-cookiecutter" \
      "org.opencontainers.image.url"="https://quay.io/organization/osism" \
      "org.opencontainers.image.vendor"="OSISM GmbH" \
      "org.opencontainers.image.title"="cookiecutter"
