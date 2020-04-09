#!/bin/bash
#
# driver script for the whonix automated testing suite, see man page for details
#
#   Copyright (C) 2020  John Quinn, Cameron Dey, and Evan Tanner
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

# robust option-parsing process lovingly utilized from: 
# https://stackoverflow.com/questions/192249/how-do-i-parse-command-line-arguments-in-bash
#


# options
debug=true # enable debug mode, verbose output when applicable

# variables
declare -A paramarr #list of featureparams
opsflag=false
behavedebug=false

#defaults
SLEEPMULT=1

for i in "$@" #for each option in all options... 
do
case $i in
    -o=*|--output=*)
	FILE="${i#*=}"
	shift # past argument=value
	;;
    -s=*|--sleepmult=*)
	SLEEPMULT="${i#*=}"
	shift # past argument=value
	;;

    -p=*|--featureparam=*)
	FEATUREPAIR="${i#*=}"
	opsflag=true

	if [ $debug == true ]
	then
	    echo "FEATUREPAIR IS ${FEATUREPAIR}"
	fi

	for i in $FEATUREPAIR
	do
	    KEY=${i%,*}
	    VAL=${i#*,}
	    paramarr[$KEY]=$VAL
	    echo "KEY IS ${KEY}"
	    echo "VALUE IS ${VAL}"

	done
#	paramarr[$KEY]=$VAL
	shift # past argument=value
	;;
    --debug)
	behavedebug=true
	shift # past argument with no value
	;;
    *)
         # unknown option
         echo "unknown option supplied, try man whonix-ats-execute"
    ;;
esac
done

if [ $debug == true ]
then
echo "Supplied Filepath = ${FILE}"
echo "Captured Key,Value List:"
    for key in ${!paramarr[@]}; do
	echo ${key} ${paramarr[${key}]}
    done
fi

# Now, build the incoming options to be passed to behave

if [ $opsflag == true ]
then
    for key in ${!paramarr[@]}; do
	PARAMS="${PARAMS} -D ${key}=${paramarr[${key}]}"
    done
fi

if [ $behavedebug == true ]
then
    PARAMS="-D BEHAVE_DEBUG_ON_ERROR=yes ${PARAMS}"
fi

PARAMS="-D SLEEPMULT=${SLEEPMULT} ${PARAMS}"

if [ $debug == true ]
then
    echo "final parameter string for behave: ${PARAMS}"
fi

# Options have now been attained, now run behave
if [ -z $FILE ]
   then
       # just run behave normally
       behave $PARAMS
   else
       # a output file was supplied pipe itest
       behave $PARAMS > $FILE
fi
