/*用get到的数据来渲染前端*/

var site_list=new Array(
"zhihu","weibo","baidu","tieba",
"toutiao","txnews","neteasenews","thepaper",
"csdn","hupu","smzdm","history",
"krrenqi","sspai","ithome","juejin",
"douyin","bilibiliday","bilibilihot","acfun",
"ghbk","wuai","douban","qqmusic",
"weread","github",
);
//元素名字，同时也是参数后name的值,limit_num 也即每次请求多少条数据

//开始渲染
for (i = 0; i < site_list.length; i++) {
    render(site_list[i],15);
}