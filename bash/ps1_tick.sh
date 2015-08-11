#!/bin/bash

days=${1:?usage: $0 days}

timestamp=$(date -v-${days}d +%s)

ticks=$((timestamp * 10000000 + 621355968000000000))

echo $ticks
