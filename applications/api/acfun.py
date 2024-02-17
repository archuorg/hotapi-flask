import json

import applications.utilis.helper as helper
from flask import Flask, render_template, request, jsonify


def fetch_data():
    filename = "acfun_data_*.data"
    file_content = helper.get_file_data(filename)
    if file_content is None:
        json_data = helper.init_json_data("acfun热榜")
        request = helper.get_html(
            "https://www.acfun.cn/rest/pc-direct/rank/channel?channelId=&subChannelId=&rankLimit=30&rankPeriod=DAY",
            None, "dict")
        num = 1
        data_list = []
        for key in request["rankList"]:
            data_list.append({"index": num, "title": key["title"], "url": key["shareUrl"], "hot": key["viewCountShow"]})
            num += 1
        res = helper.end_json_data(json_data, data_list, filename)
        return res
    else:
        return file_content