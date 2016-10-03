#!/bin/bash

echo "Rename each file *.gz to *-{CTIME}.gz"

for filename in *.gz
do
    mv -nv "${filename}" "${filename%.*.gz}-$(date -r "$filename" +"%Y%m%d").gz"
done
