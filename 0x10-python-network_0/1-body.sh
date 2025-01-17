#!/bin/bash
# Script to get the size of the response body in bytes
[ "$(curl -s -o response.txt -w "%{http_code}" "$1")" -eq 200 ] && cat response.txt
