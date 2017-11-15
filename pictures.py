import requests
import os
url = "http://image.nationalgeographic.com.cn/2015/0122/20150122062728497.jpg"
root = "D://pics//"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
       os.mkdir(root)
       # 检验是否存在目录，不存在的话创建目录
    if not os.path.exists(path):
       r = requests.get(url)
       # 检验是否存在文件，不存在的话读取url
       with open(path, 'wb') as f:
       	   f.write(r.content)
       	   f.close()
       	   print("文件保存成功")
    else:
    	print("文件已存在")
except:
 	print("爬取失败")