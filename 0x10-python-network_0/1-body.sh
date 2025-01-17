#!/bin/bash
# Script to get the size of the response body in bytes
curl -s -o response.txt -w "%{http_code}" "$1" | grep -q "200" && cat response.txt
