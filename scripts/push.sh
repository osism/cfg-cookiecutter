#!/usr/bin/env bash
set -x

# Available environment variables
#
# DOCKER_REGISTRY
# REPOSITORY
# VERSION

# Set default values

DOCKER_REGISTRY=${DOCKER_REGISTRY:-quay.io}
VERSION=${VERSION:-latest}

if [[ -n $DOCKER_REGISTRY ]]; then
    REPOSITORY="$DOCKER_REGISTRY/$REPOSITORY"
fi

buildah login --password $DOCKER_PASSWORD --username $DOCKER_USERNAME $DOCKER_REGISTRY

buildah tag "$(git rev-parse --short HEAD)" "$REPOSITORY:$VERSION"
buildah push "$REPOSITORY:$VERSION"
