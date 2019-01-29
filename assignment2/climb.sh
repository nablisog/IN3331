#!/bin/bash

function climb(){
	declare -i counter
	counter=0
	if [ $# -eq 0 ]; then
		cd */
	else
		while [ $counter -ne $1 ]; do
			cd */
			((counter++))
		done
	fi
}
