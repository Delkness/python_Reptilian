#encoding: utf-8
#多线程版本
import requests
import threading
import urllib
from bs4 import BeautifulSoup
PAGE_URL_LIST = []
#表情包链接列表
BESE_PAGE_URL = "https://www.doutula.com/photo/list/?page="
for x in range(1,1500):
    url = BESE_PAGE_URL + str(x)
    PAGE_URL_LIST.append(url)

#初始化锁
gLock = threading.Lock()

#生产者，负责从每个页面中提取表情的url
class Producer(threading.Thread):
    def run(self):
        while len(PAGE_URL_LIST) > 0:

            #在访问PAGE_URL_LIST中要使用锁机制
            gLock.acquire()
            page_url = 
for page_url in PAGE_URL_LIST:
    #url请求
    response = requests.get(page_url)
    #使用返回的数据构建ｂｅｓｕ对象

    #requests对象中　response.content返回的是二进制的数值，
    # response.text返回的是Unicode型的数据
    # 也就是说，如果你想获取文本，可以通过.text
    # 如果你想获取图片，文件可以通过　.content
    soup = BeautifulSoup(response.content,'lxml')
    #获取所有的标签
    img_list = soup.find('div',class_ = 'page-content').find_all('img',class_ = 'img-responsive lazy image_dta')
    for img in img_list:
        title = img['alt']
        src = img['data-original']
        print(title)
        print(src)
        #获取图片名称
        filename = title
        #拼接路径下载
        #path = os.path.join("image2",filename)
        path = 'images2'+ '/' +title.strip().replace('?','')
        urllib.urlretrieve(src,path)