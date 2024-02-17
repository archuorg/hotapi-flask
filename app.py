from flask import Flask, render_template
from config import Config
import json

# 导入模块
import applications.utilis.helper as helper
import applications.utilis.html_tool as html

from applications import api
from collections import OrderedDict

app = Flask(__name__)




# 定义首页路由
@app.route('/')
def index():
    # 初始访问计数
    visit_count = helper.get_visit_count()
    visit_count += 1
    # 将新的访问计数写入文件
    helper.set_visit_count(visit_count)

    # 保存所有API数据的有序字典，按照指定顺序分组
    all_api_data = OrderedDict()
    # 遍历所有模块，调用对应的函数获取数据 api文件夹内的__init__.py需要正确导入
    for api_name, chinese_name in Config.APIS.items():
        module = getattr(api, api_name, None)
        if module is not None and hasattr(module, 'fetch_data'):
            try:
                data = module.fetch_data()  # 假设每个API模块都有一个fetch_data函数来获取数据
                response = json.loads(data)
                res = html.generate_html(response)
                all_api_data[api_name] = res
            except Exception as e:
                print(f"Error fetching data for module {api_name}: {e}")

    return render_template('index.html',
                           data=all_api_data,
                           dict=Config.APIS,
                           visit_count=visit_count)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)