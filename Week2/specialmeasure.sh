#!/bin/bash
port=$(shuf -i 5200-5210 -n 1)

date
echo
iperf3 -c ok1.iperf.comnet-student.eu -p $port -t 10
iperf3 -c ok1.iperf.comnet-student.eu -p $port -t 10 -R
echo