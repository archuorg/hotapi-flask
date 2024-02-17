import os
import glob

# 获取当前文件夹下所有以 .py 结尾的文件路径
modules = glob.glob(os.path.dirname(__file__) + "/*.py")

# 导入所有模块
for module_file in modules:
    # 排除 __init__.py 文件本身
    if os.path.basename(module_file) != "__init__.py":
        module_name = os.path.basename(module_file)[:-3]  # 去掉文件后缀 .py
        __import__(f"applications.api.{module_name}", locals(), globals())
