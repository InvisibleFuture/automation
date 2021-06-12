import re
import queue
import requests
from lxml import etree


class lanrentuku:
    def __init__(self):
        url = "https://www.lanrentuku.com/tag_muban/boke.html"
        self.q = queue.Queue()  # 爬取队列
        self.q.put(url)
        self.urls = [url]  # 记录爬取过的url
        self.result = []  # 储存阅读量数据

    def request(self, url):
        res = requests.get(url)
        et = etree.HTML(res.text)
        lst = et.xpath('//a[@target="_blank"]/@href')
        for i in lst:
            if re.search('https://www.lanrentuku.com/sucai/(.*?).html', i):
                # print(i)
                self.result.append(i)

        # 下一页
        next_page = re.search(
            '<a rel="nofollow" class="next" href="(.*?)">下一页</a>', res.text)
        if next_page:
            href = "https://www.lanrentuku.com/" + next_page.group().split(
                '&nbsp;')[-1].replace('<a rel="nofollow" class="next" href="', '').replace('">下一页</a>', '')
            if href not in self.urls:  # 确保之前没有爬过
                self.q.put(href)
                self.urls.append(href)
                # print(href)

    def get_url(self):
        if not self.q.empty():
            url = self.q.get()
            self.request(url)

    def main(self):
        while not self.q.empty():
            self.get_url()


print("开始预载地址..")
crawl = lanrentuku()
crawl.main()


# def getzip(self):
#     for href in self.result:
#         if href not in self.urls:  # 确保没有重复下载
#             self.urls.append(href)
#             self.q.put(href)
#             print(href)
#

print("开始下载zip..")
for url in crawl.result:
    res = requests.get(url)
    et = etree.HTML(res.text)
    lst = et.xpath('//a[@target="_blank"]/@href')
    for i in lst:
        if re.search('https://www.lanrentuku.com/sucai/(.*?).html', i):
            # print(i)
