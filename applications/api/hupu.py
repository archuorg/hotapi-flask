import applications.utilis.helper as helper


def fetch_data():
    filename = "hupu_data_*.data"
    file_content = helper.get_file_data(filename)
    if file_content is None:
        json_data = helper.init_json_data("虎扑步行街热榜")
        data_list = []
        request = helper.get_html("https://bbs.hupu.com/all-gambia", None, "html")
        articles_title = request.xpath(
            '//*[@id="container"]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[1]/a/span/text()')
        articles_url = request.xpath(
            '//*[@id="container"]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[1]/a/@href')
        articles_hot = request.xpath(
            '//*[@id="container"]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[1]/span[1]/text()')
        datas = [articles_title, articles_url, articles_hot]
        data_list = helper.headle_html_data_list(datas, "https://bbs.hupu.com/")
        return helper.end_json_data(json_data, data_list, filename)
    else:
        return file_content