# hotapi-flask
## 热点api集合
 [示例页面](http://hot.archu.org)

## docker配置
```angular2html
# 拉取源码
git clone https://github.com/archuorg/hotapi-flask.git

# 进入源码文件夹
cd hotapi-flask

# 构建镜像
docker build -t hotapi-flask .

# 启动docker
docker run -d --restart=always -v /root/hotapi-flask:/app -p 5000:5000 --name hotapi-flask hotapi-flask:latest
```

## 直接拉取镜像运行
```angular2html
# 拉取源码
git clone https://github.com/archuorg/hotapi-flask.git

# 启动docker
docker run -d --restart=always -v /root/hotapi-flask:/app -p 5000:5000 --name hotapi-flask trueway/hotapi:1.0
```