# -*- coding:utf-8 -*-
__author__ = 'Lakisha'

import urllib.request
import urllib.parse
from html.parser import HTMLParser

class BlogHTMLParser(HTMLParser):
    data = []
    data_key = ""

    def __init__(self):
        HTMLParser.__init__(self)
        self.is_a = False

    def handle_starttag(self, tag, attrs):
        # 处理开始为a的标签
        if tag == "a":
            self.is_a = True
            for name, value in attrs:
                if name == "href":
                    self.data_kay = value

    def handle_data(self, data):
        #处理结束为a的标签
        if self.is_a and self.lasttag == "a":
            # 将a标签的href属性值作为key， a的文本作为data构建字典
            self.data.append({self.data_key : data})

    def handle_endtag(self, tag):
        # 处理a结束标签
        if self.is_a and self.lasttag == "a":
            self.is_a == False

    def get_data(self):
        # 返回所有从a中提取到的数据
        return self.data


if __name__ == "__main__":
    print("urllib爬取博客园首页实例演示说明")

    url = "https://www.cnblogs.com/"

    # 访问首页
    response = urllib.request.urlopen(url)
    # 获取首页的html
    data = response.read().decode(encoding="utf-8")

    # 提取所有的链接
    blogHtmlParser = BlogHTMLParser()
    blogHtmlParser.feed(data)
    links = blogHtmlParser.get_data()
    print(links)