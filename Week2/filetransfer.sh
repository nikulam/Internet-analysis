#!/bin/bash

port=$(shuf -i 5200-5210 -n 1)

date
echo
curl -o /dev/null -m 10 http://blr1.iperf.comnet-student.eu -p $port -w "%{speed_download}\\n" -s
echo
curl -o /dev/null -m 10 http://ok1.iperf.comnet-student.eu -p $port -w "%{speed_download}\\n" -s
echo