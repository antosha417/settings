#!/bin/bash
cd $(dirname "$0")
cat config.{1..4}.* > config
cat config.{5..6}.$(hostname -s)_* >> config
