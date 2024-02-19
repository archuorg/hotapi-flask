from flask import Flask, render_template
import json
from config import Config
# 导入模块
import applications.utilis.helper as helper
from applications import api


app = Flask(__name__)

# 定义首页路由
@app.route('/test')
def test():
    sites = Config.APIS
    return render_template('test.html', sites=sites)

# 定义首页路由
@app.route('/')
def index():
    # 初始访问计数
    visit_count = helper.get_visit_count()
    visit_count += 1
    # 将新的访问计数写入文件
    helper.set_visit_count(visit_count)
    sites = Config.APIS
    return render_template('index.html',
                           visit_count=visit_count,
                           sites=sites)


@app.route('/api/<string:api_name>')
def api_data(api_name):
    module = getattr(api, api_name, None)
    if module is not None and hasattr(module, 'fetch_data'):
        try:
            data = module.fetch_data()  # 假设每个API模块都有一个fetch_data函数来获取数据
            response = json.loads(data)
            return response
        except Exception as e:
            print(f"Error fetching data for module {api_name}: {e}")
            return False


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)