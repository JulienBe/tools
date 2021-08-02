#!/bin/bash

repo=$1
job_nubmer=$2

echo "Trying to dl logs for job $job_nomber of $repo"

curl --connect-timeout 5 \
     --max-time 10 \
     --retry 5 \
     --retry-delay 0 \
     --retry-max-time 40 \
     -u 'julien:token' \
     -k "https://jenkins.corp:1234/job/$repo/$job_number/consoleText" \
     -o "$repo.$job_number"
