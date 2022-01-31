#!/bin/bash

date
echo

dig ns moneytech.mg @204.61.216.121 | fgrep time
ping -c 1 pch.nic.mg -O -D | fgrep time
echo

dig ns moneytech @196.192.32.2 | fgrep time
ping -c 1 ns.dts.mg -O -D | fgrep time
echo

dig ns moneytech @196.192.42.153 | fgrep time
ping -c 1 ns.nic.mg -O -D | fgrep time
echo