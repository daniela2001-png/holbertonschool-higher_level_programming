#!/bin/bash
# NAME
#   run.sh - Run scripts in the test folder for Python projects at HolbertonSchool
# SYNOPSIS
#   ./run.sh [TASK-NUMBER]
# DESCRIPTION
#   This script include the current directry into the $PYTHONPATH and
#   run the ./test/[TASK-NUMBER]-main.py file
# EXAMPLE
#   ./run.sh 0
# INSTALLATION
#   go to the project folder and run this command
#   wget https://gist.github.com/Athesto/3b9d05d5e8b7f4cc2f8bd3ada1d34543/raw/run.sh
#   chmod u+x run.sh
# CREATOR
#   Gustavo Adolfo Mejia, Cohort:0x0C, twitter:@im_tavo, github:@Athesto

FILE="./test/$1-main.py"
CURPATH=$(pwd)

# Check PYTHONPATH
if [[ ":$PYTHONPATH:" != *"$CURPATH:"* ]]; then
    export PYTHONPATH+=$CURPATH
fi

# Check if file exist
if [[ -f ${FILE} ]]; then
        "${FILE}"
else
        echo "File not found"
fi