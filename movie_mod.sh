#!/bin/bash

pavucontrol&
pulseaudio --start
pkill xautolock
echo 'connect 04:FE:A1:FB:64:B0' | bluetoothctl

