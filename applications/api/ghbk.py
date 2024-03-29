import applications.utilis.helper as helper


def fetch_data():
    filename = "ghbk_data_*.data"
    file_content = helper.get_file_data(filename)
    if file_content is None:
        json_data = helper.init_json_data("果核剥壳最新数据")
        request = helper.get_html("https://www.ghxi.com/ghapi?type=query&n=new", None, "dict")
        data_list = []
        num = 1
        for key in request["data"]["list"]:
            data_dict = {"index": num,
                         "title": key["title"],
                         "url": key["url"],
                         "hot": ""}
            num += 1
            data_list.append(data_dict)
        return helper.end_json_data(json_data, data_list, filename)
    else:
        return file_content