import requests
from lxml import html
import applications.utilis.helper as helper


def fetch_data():
    filename = "pubmed_data_*.data"
    file_content = helper.get_file_data(filename)
    if file_content is None:
        json_data = helper.init_json_data("PubMed趋势")
        headers = {
            "authority": "pubmed.ncbi.nlm.nih.gov",
            "user-agent": helper.random_user_agent(),
        }

        url1 = "https://pubmed.ncbi.nlm.nih.gov/trending/?page=1"
        url2 = "https://pubmed.ncbi.nlm.nih.gov/trending/?page=2"

        response1 = requests.get(url=url1, headers=headers).text
        response2 = requests.get(url=url2, headers=headers).text

        # Assuming that 'response.text' contains the HTML content
        html_content = response1 + response2

        # print(html_content)

        # Parse the HTML content
        tree = html.fromstring(html_content)

        # Use XPath to extract the desired value
        xpath_title = '//section/div[2]/div/article/div[2]/div[1]/a/text()'
        xpath_url = '//section/div[2]/div/article/div[2]/div[1]/a/@href'
        xpath_hot = '//section/div[2]/div/article/div[1]/label/span/text()'

        articles_title = tree.xpath(xpath_title)
        articles_url = tree.xpath(xpath_url)
        articles_hot = tree.xpath(xpath_hot)

        datas = [articles_title, articles_url, articles_hot]

        # 去除不需要的符号
        cleaned_data = [[string.strip() for string in sublist if string.strip()] for sublist in datas]

        data_list = helper.headle_html_data_list(cleaned_data, "https://pubmed.ncbi.nlm.nih.gov/", "rank")
        return helper.end_json_data(json_data, data_list, filename)
    else:
        return file_content