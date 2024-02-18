import requests
from lxml import html
import applications.utilis.helper as helper


def fetch_data():
    filename = "github_data_*.data"
    file_content = helper.get_file_data(filename)
    if file_content is None:
        json_data = helper.init_json_data("GitHub趋势")
        headers = {
            "authority": "github.com",
            "referer": "https://github.com/explore",
            "user-agent": helper.random_user_agent(),
        }

        url = "https://github.com/trending"

        response = requests.get(url=url, headers=headers)

        # Assuming that 'response.text' contains the HTML content
        html_content = response.text

        # print(html_content)

        # Parse the HTML content
        tree = html.fromstring(html_content)

        # Use XPath to extract the desired value
        xpath_title = '//main/div[3]/div/div[2]/article/h2/a/text()'
        xpath_url = '//main/div[3]/div/div[2]/article/h2/a/@href'
        xpath_hot = '//main/div[3]/div/div[2]/article/div[2]/span[3]/text()'

        articles_title = tree.xpath(xpath_title)
        articles_url = tree.xpath(xpath_url)
        articles_hot = tree.xpath(xpath_hot)

        datas = [articles_title, articles_url, articles_hot]

        # 去除不需要的符号
        cleaned_data = [[string.strip() for string in sublist if string.strip()] for sublist in datas]

        data_list = helper.headle_html_data_list(cleaned_data, "https://github.com", "Stars")
        return helper.end_json_data(json_data, data_list, filename)
    else:
        return file_content