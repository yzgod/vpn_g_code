## **自动计算谷歌验证码MFA 并填充**

#### 依赖python3, expect shell
    需要配置好vpn的ssh key

#### 编辑 vpn.sh 

    user="你的vpn账号"
    token="你的谷歌验证token 16位字符串,jumpserver个人信息重置MFA可查看"
    jump_server="jumpserver.com"
    
#### 获取MFA 
    python3 ${SH_HOME}/g_code3.py ${token}

#### 运行 ./vpn.sh
