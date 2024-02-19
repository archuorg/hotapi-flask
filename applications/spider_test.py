import requests
from lxml import html

headers = {
            "authority": "pubmed.ncbi.nlm.nih.gov",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        }

url1 = "https://pubmed.ncbi.nlm.nih.gov/trending/?page=1"
url2 = "https://pubmed.ncbi.nlm.nih.gov/trending/?page=2"

response1 = requests.get(url=url1, headers=headers).text
response2 = requests.get(url=url2, headers=headers).text

# Assuming that 'response.text' contains the HTML content
html_content = response1 + response2

# Parse the HTML content
tree = html.fromstring(html_content)

# Use XPath to extract the desired value
# Use XPath to extract the desired value
xpath_title = '//section/div[2]/div/article/div[2]/div[1]/a/text()'
xpath_url = '//section/div[2]/div/article/div[2]/div[1]/a/@href'
xpath_hot = '//section/div[2]/div/article/div[1]/label/span/text()'

title = tree.xpath(xpath_title)
url = tree.xpath(xpath_url)
hot = tree.xpath(xpath_hot)

datas = [title, url, hot]

# 去除不需要的符号
cleaned_data = [[string.strip() for string in sublist if string.strip()] for sublist in datas]

# Print the extracted value
if datas:
    print("Extracted value:", cleaned_data)
else:
    print("Value not found.")
