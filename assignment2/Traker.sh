#!/bin/bash

if [ "$1" != "start" ]; then
  echo "Type START inorder the program to start running"
fi

if [ "$1" == "start" ]; then
  start=$(date)
  echo $start
  while true;
  do
    read -p " status or stop " "input"
    if [ $input == "status" ]; then
      echo "THIS IS" "$2"
    fi

    if [ $input == "stop" ]; then
      stop=$(date)
      echo  "started at" "$start"
      echo  "finished at" "$stop"
      echo $start|awk '{print $4}'
      echo $stop|awk '{print $4}'

      break
    fi

    done
  fi
echo "start : $start
task : $2
end : $stop
           " >> mylog.txt
export LOGFILE=mylog.txt
