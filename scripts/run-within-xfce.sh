#!/usr/bin/env bash

set -e

docker build -t schulstick-portal-xfce $(pwd)/dist/ || exit 1
x11docker --desktop schulstick-portal-xfce
