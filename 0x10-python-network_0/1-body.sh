#!/bin/bash
# Script that sends GET request and only display body response of 200 status code
[ "$(curl -s -o response.txt -w "%{http_code}" "$1")" -eq 200 ] && cat response.txt
