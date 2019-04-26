#!/bin/bash
cd $(dirname "$0")
cat config.{1..5}.* > config
cat config.6.$(hostname -s)_* >> config
