#!/bin/bash

VERSION=$(python3 scripts/filehash.py)

docker build -t "github-container-registry-ci-dependencies:$VERSION" -f dependencies.dockerfile .

docker build --build-arg DEPS_VERSION=${VERSION} -t "github-container-registry-ci:latest" .
