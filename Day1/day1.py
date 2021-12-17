# 初识requests
import requests
from lxml import etree

# get 方法, 以及请求后的常见输出
url = 'http://123.meibp.com/tag/每日热点关键词.html'
# data = data
r = requests.get(url=url)
print(r.url)  # url
print(r.encoding)  # 编码情况
print(r.status_code)  # 响应状态码
print(r.text)  # 解码来自服务器的内容,显示乱码，可能是编码问题
# 设置编码后，再输出，即可正常显示
r.encoding = 'utf-8'
print(r.text)
# 通过etree格式化
r = etree.HTML(r.text)  # 修正，格式化，注意此刻的数据类型
print(type(r))  #
print(r)
r = etree.tostring(r)
# print(r.decode('utf-8'))
print(r)