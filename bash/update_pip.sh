#!/bin/bash

pip=pip${1:?Usage: $0 PY_VERSION}
requirements="$(mktemp)"
${pip} freeze | cut -d= -f 1 > ${requirements}

${pip} install -U -r ${requirements}

rm -f ${requirements}
