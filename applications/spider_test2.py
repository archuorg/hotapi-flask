import requests
from lxml import html

headers = {
            "authority": "github.com",
            "referer": "https://github.com/explore",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        }

url = "https://github.com/trending"

response = requests.get(url=url, headers=headers)

# Assuming that 'response.text' contains the HTML content
html_content = response.text

# Parse the HTML content
tree = html.fromstring(html_content)

# Use XPath to extract the desired value
xpath_name = '//main/div[3]/div/div[2]/article/h2/a/span/text()'
xpath_title = '//main/div[3]/div/div[2]/article/h2/a/text()'
xpath_url = '//main/div[3]/div/div[2]/article/h2/a/@href'
# xpath_hot = '//main/div[3]/div/div[2]/article/div[2]/span[3]/text()'

names = tree.xpath(xpath_name)
titles = tree.xpath(xpath_title)
url = tree.xpath(xpath_url)
# hot = tree.xpath(xpath_hot)

new_names = []
for name in names:
    cleaned_sublist = name.strip()
    new_names.append(cleaned_sublist)
print(len(new_names))
new_titles = []
for title in titles:
    if title.strip():
        cleaned_sublist = title.strip()
        new_titles.append(cleaned_sublist)
print(len(new_titles))
# print(len(hot))
# 遍历列表，将每对数据组合成一个字符串
combined_titles = []
# 使用zip函数将两个列表中的元素一一配对，然后循环遍历这些配对
for name, title in zip(new_names, new_titles):
    combined_title = name + ' ' + title
    combined_titles.append(combined_title)


datas = [combined_titles, url, new_titles]

# 语法：string.strip([chars])； 如果不提供 chars 参数，strip() 方法会默认去除字符串两端的空格字符、制表符（\t）、换行符（\n）等空白字符。
cleaned_data = []
for sublist in datas:
    cleaned_sublist = [item.strip() for item in sublist if item.strip()]
    cleaned_data.append(cleaned_sublist)

# 处理数据
num = 1
data_list = []
for title, url, hot in zip(cleaned_data[0], cleaned_data[1], cleaned_data[2]):
    data_dict = {"index": num, "title": title, "url": "https://github.com" + url}
    num += 1
    data_dict["hot"] = hot
    data_list.append(data_dict)
# Print the extracted value
if datas:
    print("Extracted value:", data_list)
else:
    print("Value not found.")
