#!/bin/bash
if [ "$1" != "start" ]; then
  echo "Type START inorder the program to start running"
fi

if [ $1 == "start" ]; then
  start=$(date +"%s")
  echo $start
  while true;
  do
    read -p " status or stop " "input"
    if [ $input == "status" ]; then
      echo "THIS IS" "$2"
    fi
    if [ $input == "stop" ]; then
      stop=$(date +"%s")
      echo $stop

      elapsed="$(($stop-$start))"
      #echo $elapsed
      echo " $((elapsed/60))h $((elapsed/60))m $((elapsed%60))s"

      break
    fi
    done
  fi
  echo "start : $start
  task : $2
  end : $stop
             " >> mylog.txt
  export LOGFILE=mylog.txt
