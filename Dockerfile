# 使用 Python 3.10 的轻量级镜像作为基础镜像
FROM python:3.10-slim

# 设置维护者信息
LABEL maintainer="admin@archu.org"

# 暴露容器的端口，这里映射到宿主机的5000端口
EXPOSE 5000

# 阻止 Python 生成 .pyc 文件
ENV PYTHONDONTWRITEBYTECODE=1

# 禁用 Python 的输出缓冲，便于在容器中查看日志
ENV PYTHONUNBUFFERED=1

# 复制当前目录下的 requirements.txt 文件到容器的根目录
COPY requirements.txt .

# 在容器中安装 Python 依赖包，使用清华大学的 pip 镜像源
RUN python -m pip install --no-cache-dir --upgrade -i https://pypi.tuna.tsinghua.edu.cn/simple/ -r requirements.txt

# 设置容器的工作目录为 /app
WORKDIR /app

# 复制当前目录下的所有文件到容器的 /app 目录
COPY . /app

# 定义容器启动时的默认命令，启动app.py，监听在 0.0.0.0 地址上的 5000 端口
CMD ["python", "app.py", "--host", "0.0.0.0"]
