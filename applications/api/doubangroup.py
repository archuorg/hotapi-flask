import requests
from lxml import html
import applications.utilis.helper as helper


def fetch_data():
    filename = "doubangroup_data_*.data"
    file_content = helper.get_file_data(filename)
    if file_content is None:
        json_data = helper.init_json_data("豆瓣小组")
        headers = {
            "referer": "https://www.douban.com/group/topic/301923009/?_i=8332028b75By24",
            "user-agent": helper.random_user_agent(),
        }

        url = "https://www.douban.com/group/explore"

        response = requests.get(url=url, headers=headers)

        # Assuming that 'response.text' contains the HTML content
        html_content = response.text

        # print(html_content)

        # Parse the HTML content
        tree = html.fromstring(html_content)

        # Use XPath to extract the desired value
        xpath_title = '//div[3]/div[1]/div/div[1]/div[1]/div/div[2]/h3/a/text()'
        xpath_url = '//div[3]/div[1]/div/div[1]/div[1]/div/div[2]/h3/a/@href'
        xpath_hot = '//*[@id="content"]/div/div[1]/div[1]/div/div[1]/text()[1]'

        articles_title = tree.xpath(xpath_title)
        articles_url = tree.xpath(xpath_url)
        articles_hot = tree.xpath(xpath_hot)

        datas = [articles_title, articles_url, articles_hot]

        # 去除不需要的符号
        cleaned_data = [[string.strip() for string in sublist if string.strip()] for sublist in datas]

        data_list = helper.headle_html_data_list(cleaned_data, "", "喜欢")
        return helper.end_json_data(json_data, data_list, filename)
    else:
        return file_content