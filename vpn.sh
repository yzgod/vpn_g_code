#!/bin/sh

user="你的vpn账号"
token="你的谷歌验证token 16位字符串,jumpserver个人信息重置MFA可查看"
jump_server="jumpserver.com"
SH_HOME=$(cd "$(dirname $0)";pwd)

for (( i = 0; i <= 10; ++i )); do
    if [[ $i > 0 ]]; then
       echo "重试第${i}次"
    fi
    expect ${SH_HOME}/vpn_expect ${SH_HOME} ${token} ${user} ${jump_server}
    if [[ $? = 0 ]]; then
        exit
    fi
    sleep 1s
done

