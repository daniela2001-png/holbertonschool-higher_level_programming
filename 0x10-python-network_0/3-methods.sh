#!/bin/bash
# Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.
# I - Fetch the headers only! HTTP-servers feature the command HEAD which this uses to get nothing but the header of a document.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
