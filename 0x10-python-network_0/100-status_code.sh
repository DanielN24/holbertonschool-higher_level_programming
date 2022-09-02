#!/bin/bash
# displays only the status code
curl --write-out "%{http_code}" --silent --output /dev/null "$1"
