#!/bin/bash

# patterns.list: each pattern in single line
# huge_file: TSV
# $8 - number of column in csv,which compared with patterns

awk -F '\t' '{ if (FNR==NR) { ip[$0]=1 }
               else if (ip[$8]==1) { print $0 }
     }' patterns.list huge_file >> result.txt
