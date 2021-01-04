#!/bin/bash
rm list.txt last.txt
T=0
i=-1
while true; do
     N=`grep -m1 -ao '[0-1]' /dev/hwrng | sed s/10/0/ | head -n1`
     if [ $N == 1 ]; then
          T=$(( $T + 1  ))
     else
          T=$(( $T -1  ))
     fi
     let "i++"
     echo $i $T >> list.txt
     tail -100 list.txt > last.txt
done
