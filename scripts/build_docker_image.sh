#!/bin/bash

VERSION=$(python3 scripts/filehash.py)
DEPENDENCIES_IMAGE="github-container-registry-ci-dependencies:$VERSION"

if docker inspect $DEPENDENCIES_IMAGE &> /dev/null; then
    echo "Dependency image $DEPENDENCIES_IMAGE exists."
    echo "Not rebuilding."
else
    echo "Dependency images $DEPENDENCIES_IMAGE does not exist."
    echo "Building dependency image."
    docker build -t "github-container-registry-ci-dependencies:$VERSION" -f dependencies.dockerfile .
fi

docker build --build-arg DEPS_VERSION=${VERSION} -t "github-container-registry-ci:latest" .
