#!/bin/sh

EMAIL=$(python -c "from random import randint; print randint(1000, 100000)")@ivi.ru
EMAIL=$(python -c "import uuid; print uuid.uuid1()")@ivi.ru

SESSION=$(curl -d "app_version=870&email=$EMAIL&password=qwerty" api.akovalkov.notkube.dev.ivi.ru/mobileapi/user/register/v5/ |     python -c "import sys, json; print json.load(sys.stdin)[u'result'][u'session']")

echo $SESSION

