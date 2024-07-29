#!/bin/sh
num_dns=`sed -n 's/^! Total count: //p' dns.txt`

time=$(TZ=UTC-8 date +'%Y-%m-%d %H:%M:%S')
sed -i "s/^更新时间:.*/更新时间: $time （北京时间） /g" README.md
sed -i 's/^DNS拦截规则数量.*/DNS拦截规则数量: '$num_dns' /g' README.md

exit
