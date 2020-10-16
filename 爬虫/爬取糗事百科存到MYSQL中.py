import requests
from lxml import etree
from fake_useragent import UserAgent
import pymysql
# 判断列表是否为空（Determines if the list is  empty ）
def getDataFormList(temp_list):
    if len(temp_list) > 0:
        return temp_list[0].strip()
    else:
        return ''

# url接口
base_url = 'https://www.qiushibaike.com/hot/page/%d/'
# 网络请求
for page in range(1, 3, 1):
    # url = 'https://www.qiushibaike.com/hot/page/%d/'%(page)
    url = base_url % (page)
    headers = {
        'User-Agent': UserAgent().random
    }

    response = requests.request('get', url=url, headers=headers, verify=False)
    with open('qiushi.html', 'w', encoding=response.encoding) as fp:
        fp.write(response.text)

    # 数据提取
    tree = etree.HTML(response.text)


    # 先定位到文章列表
    article_list = tree.xpath('//div[contains(@id,"qiushi_tag_")]')
    for article in article_list:
        # 作者
        author_list = article.xpath('./div/a/h2/text()')
        author = getDataFormList(author_list).strip()
        #print('作者:',author)

        # 好笑数
        funny_number_list = article.xpath('.//i[@class="number"]/text()')
        funny_number = getDataFormList(funny_number_list)
        #print('好笑数:',funny_number)

        # 评论数
        comment_list = article.xpath('.//a[@class="qiushi_comments"]/i/text()')
        comment = getDataFormList(comment_list).strip()
        #print('评论数:',comment)

        # 段子内容
        content_list = article.xpath('.//div[@class="content"]/span/text()')
        content = getDataFormList(content_list).strip()
        # print('段子内容:',content)
        print(author, content, comment, funny_number, )

        # 数据存储
        # 注意此处存储数据时，要和插入mysql表中的mysql语句中的字段相对应，否则会报错。
        # data = (author, funny_number, comment, content)

        # 建立数据库连接（mysql connect）
        conn = pymysql.connect(host="192.168.43.128", port=3306, user='root', password='root', db='xh',
                               charset='utf8')
        cursor = conn.cursor()

        data = (author, funny_number, comment, content)
        sql = 'insert into qiushi(author,funny_num,comment_num,content) values(%s,%s,%s,%s) '
        try:
            cursor.execute(sql, data)
            conn.commit()
        except Exception as e:
            print('插入数据失败', e)
            conn.rollback()  # 回滚

cursor.close()
conn.close()
