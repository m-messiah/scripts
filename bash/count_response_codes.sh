#!/usr/local/bin/bash
if [ -z $1 ] || [ -z $2 ]; then
    >&2 echo "Usage: ./codes.sh <position_of_\$status> <nginx.access.log.0.gz>"
    exit 1
fi

command="zcat -f"
$command $2 | awk -F '\t' -v k=$1 '{c[$k]++;} END {for (key in c) {print key, c[key];}}' | sort -n
