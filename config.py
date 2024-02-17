class Config:
    # 访问数文件存放目录
    VISIT_COUNT_DATA_DEST = 'static/visit_count.data'

    # API字典，api模块名称与中文名一一对应，用于前端Jinja2渲染与排序
    APIS = {
        "zhihu": "知乎",
        "weibo": "微博",
        "baidu": "百度",
        "tieba": "贴吧",

        "toutiao": "今日头条",
        "txnews": "腾讯新闻",
        "neteasenews": "网易新闻",
        "thepaper": "澎湃新闻",

        "csdn": "CSDN",
        "hupu": "虎扑",
        "smzdm": "什么值得买",
        "history": "历史上的今天",

        "krrenqi": "36氪人气榜",
        "sspai": "少数派",
        "ithome": "IT之家",
        "juejin": "稀土掘金",

        "douyin": "抖音热榜",
        "bilibiliday": "B站日榜",
        "bilibilihot": "B站热门",
        "acfun": "A站热榜",

        "ghbk": "果核剥壳",
        "wuai": "吾爱破解",
        "douban": " 豆瓣新片",
        "qqmusic": "QQ音乐",

        "weread": "微信读书",
    }