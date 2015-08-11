#!/bin/bash

# Will hide errors, but print output

command 2> /dev/null || echo "fictive result"
