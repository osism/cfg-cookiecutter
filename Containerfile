ARG PYTHON_VERSION=3.12
FROM python:${PYTHON_VERSION}-alpine

COPY --from=ghcr.io/astral-sh/uv:0.9.18 /uv /usr/local/bin/uv
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
    && uv pip install --no-cache --system -r /tmp/requirements.txt \
    && apk del .build-deps \
    && mkdir /output

COPY . /data

WORKDIR /data

VOLUME ["/output"]

ENTRYPOINT ["/data/entrypoint.sh"]

LABEL "org.opencontainers.image.documentation"="https://osism.tech/docs/" \
      "org.opencontainers.image.licenses"="ASL 2.0" \
      "org.opencontainers.image.source"="https://github.com/osism/cfg-cookiecutter" \
      "org.opencontainers.image.url"="https://quay.io/organization/osism" \
      "org.opencontainers.image.vendor"="OSISM GmbH" \
      "org.opencontainers.image.title"="cookiecutter"
