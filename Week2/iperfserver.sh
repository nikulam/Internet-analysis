#!/bin/bash

port=$(shuf -i 5200-5210 -n 1)

date
echo
ping -c 5 blr1.iperf.comnet-student.eu -p $port
curl -o /dev/null -m 5 http://blr1.iperf.comnet-student.eu/1K.bin -p $port -w "%{time_total}\\n" -s
echo
ping -c 5 ok1.iperf.comnet-student.eu -p $port
curl -o /dev/null -m 5 http://ok1.iperf.comnet-student.eu/1K.bin -p $port -w "%{time_total}\\n" -s
echo