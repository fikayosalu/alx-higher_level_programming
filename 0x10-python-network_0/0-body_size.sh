#!/usr/bin/env bash
# Script to get the size of the response body in bytes

curl -s "$1" | wc -c
