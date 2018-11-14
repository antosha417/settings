#!/bin/sh

SESSION=$(bash  $(pwd)/register_user.sh)

curl -d 'app_version=870&session='$SESSION'&key='$1 http://mobile.akovalkov.notkube.dev.ivi.ru/billing/v1/certificate/activate

