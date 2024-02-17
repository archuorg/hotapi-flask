import applications.utilis.helper as helper


def fetch_data():
    filename = "tieba_data_*.data"
    file_content = helper.get_file_data(filename)
    if file_content is None:
        json_data = helper.init_json_data("百度贴吧热议榜")
        data_list = []
        request = helper.get_html("https://tieba.baidu.com/hottopic/browse/topicList?res_type=1", None, "html")
        articles_title = request.xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[1]/ul/li/div/div/a/text()')
        articles_url = request.xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[1]/ul/li/div/div/a/@href')
        articles_hot = request.xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[1]/ul/li/div/div/span[2]/text()')
        datas = [articles_title, articles_url, articles_hot]
        data_list = helper.headle_html_data_list(datas, "", "实时讨论")
        return helper.end_json_data(json_data, data_list, filename)
    else:
        return file_content