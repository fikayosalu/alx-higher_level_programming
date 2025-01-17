#!/bin/bash
# Script to get the size of the response body in bytes
"$(curl -s -w "%{http_code}" "$1")" -eq 200
