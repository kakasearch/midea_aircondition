# 思路
 直接在美的美居中抓包未能找到api，因此在小度app中绑定美的美居账号，通过小度实现控制空调打开与关闭
# 使用
 1. 需要对美的美居app中 `https://mp-prod.smartmidea.net:443/mas/v5/app/proxy`抓包获取设备Id、token和cookie
 2. 对小度app中`https://xiaodu.baidu.com/saiya/smarthome/directivesend?from=h5_control`抓包，获取cookie
 