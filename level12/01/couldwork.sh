#!/usr/bin/sh
exec 3<>/dev/tcp/services.cyberprotection.agency/9999
start=`date +%s.%N`
out="$(head -3 <&3)"
out2="$out"
array=($out2)
var=$((array[0]*array[1]/array[2]))
echo $var >&3
end=`date +%s.%N`
slowtime=$( echo "$end - $start - 0.1" | bc -l )
echo "$slowtime too slow"

