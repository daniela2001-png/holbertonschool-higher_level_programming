#!/bin/bash
# -i --include this give me the response! vs -I --head include just the header not response!
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
