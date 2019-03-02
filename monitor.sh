#!/bin/bash

BASEPATH=$(cd `dirname $0`; pwd)

COMMAND="./main.py"

while true; do
    proc_num=`ps -ef | grep ${COMMAND} | grep -v "grep" | wc -l`
    if [ ${proc_num} -eq 0 ]; then
        `nohup ${COMMAND} >/dev/null 2>&1 &`
        echo "[`date '+%Y-%m-%d %H:%M:%S'`] Restart Service" >> \
             ${BASEPATH}/monitor.log
    fi
    sleep 1
done
