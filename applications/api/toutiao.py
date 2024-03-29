import applications.utilis.helper as helper


def fetch_data():
    filename = "toutiao_data_*.data"
    file_content = helper.get_file_data(filename)
    if file_content is None:
        json_data = helper.init_json_data("今日头条")
        request = helper.get_html("https://www.toutiao.com/hot-event/hot-board/?origin=toutiao_pc", None, "dict")
        data_list = []
        num = 1
        for key in request["data"]:
            data_dict = {"index": num,
                         "title": key["Title"],
                         "url": key["Url"],
                         "hot": key["HotValue"]}
            num += 1
            data_list.append(data_dict)
        return helper.end_json_data(json_data, data_list, filename)
    else:
        return file_content