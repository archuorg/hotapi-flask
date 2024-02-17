import applications.utilis.helper as helper
from lxml import html
import requests

def fetch_data():
    filename = "douban_data_*.data"
    file_content = helper.get_file_data(filename)
    if file_content is None:
        json_data = helper.init_json_data("豆瓣新片榜")
        # 设置请求头，模拟浏览器访问
        headers = {
            # 'cookie': 'bid=7rofuH19PwI; _pk_id.100001.4cf6=09d81822fbd7b388.1706006396.; __utmc=30149280; __utmz=30149280.1706006397.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmc=223695111; __utmz=223695111.1706006397.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ll="118281"; _pk_ses.100001.4cf6=1; __utma=30149280.1733604764.1706006397.1706006397.1706016246.2; __utmb=30149280.0.10.1706016246; __utma=223695111.1185399663.1706006397.1706006397.1706016246.2; __utmb=223695111.0.10.1706016246; dbcl2="157830307:765sI5k/Gxs"; ck=Qzrv; push_noty_num=0; push_doumail_num=0',
            # "Referer": "https://open.weixin.qq.com/",
            "user-agent": helper.random_user_agent(),
        }

        # 目标网址
        url = "https://movie.douban.com/chart"

        # 发送GET请求，获取网页内容
        response = requests.get(url=url, headers=headers)

        # 获取网页内容的文本形式
        html_content = response.text

        # 使用html模块解析HTML
        tree = html.fromstring(html_content)

        # 提取电影标题信息
        articles_title = tree.xpath('//*[@id="content"]/div/div[1]/div/div/table/tr/td[1]/a/@title')

        # 提取电影链接信息
        articles_url = tree.xpath('//*[@id="content"]/div/div[1]/div/div/table/tr/td[2]/div/a/@href')

        # 提取电影热度信息
        articles_rating = tree.xpath('//*[@id="content"]/div/div[1]/div/div/table/tr/td[2]/div/div/span[2]/text()')


        # 遍历列表，将每对数据组合成一个字符串
        combined_titles = []

        # 使用zip函数将两个列表中的元素一一配对，然后循环遍历这些配对
        for title, rating in zip(articles_title, articles_rating):
            combined_title = f"【★{rating}分】 {title}"
            combined_titles.append(combined_title)

        datas = [combined_titles, articles_url, articles_rating]
        data_list = helper.headle_html_data_list(datas, "", "热度")
        return helper.end_json_data(json_data, data_list, filename)
    else:
        return file_content