#!/usr/bin/env bash
set -euo pipefail

DOCKER_CMD="docker"
ADDITIONAL_ARGS=""
IMAGE="debian:bookworm-slim"
if [ "${1:-}" = "-x" ]; then
  echo "using x11docker"
  DOCKER_CMD="x11docker"
  #ADDITIONAL_ARGS="--gpu yes"
  ADDITIONAL_ARGS=""
  IMAGE="x11docker/xfce"
fi

$DOCKER_CMD \
  ${ADDITIONAL_ARGS} \
  -v "$(pwd)/dist:/dist:ro" \
  ${IMAGE} \
  /bin/bash -c "apt-get update && apt-get install -y /dist/*.deb && bash"


