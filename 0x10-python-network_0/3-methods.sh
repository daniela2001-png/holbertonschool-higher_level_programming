#!/bin/bash
# Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.
# use grep cuz con tail y head seme complicaba la cosa
curl -si "$1" | grep "Allow" | cut -d " " -f 2-
