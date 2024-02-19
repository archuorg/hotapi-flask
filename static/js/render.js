function render(elem_name) {
    layui.use('flow', function () {
        let $ = layui.jquery;
        let flow = layui.flow;

        flow.load({
            elem: "#" + elem_name, // 指定列表容器
            end: "没有更多了",
            scrollElem: "#" + elem_name + "card", // 滚动条元素
            mb: 30,
            done: function (page, next) { // 到达临界点触发下一页
                let lis = [];
                // 使用 jQuery 的 Ajax 请求数据
                $.ajax({
                    url: '/api/'+ elem_name,
                    method: 'GET',
                    dataType: 'json',
                    success: function (res) {
                        layui.each(res.data, function (index, item) {
                        let num = index + 1;
                        if(num<=3){
                          let num_1 = "<span style='width:24px;height:24px;border-radius:4px;background:#ea444d;display:inline-block;text-align:center;line-height:24px;'><font color='white'>1</font></span>"
                          let num_2 = "<span style='width:24px;height:24px;border-radius:4px;background:#ed702d;display:inline-block;text-align:center;line-height:24px;'><font color='white'>2</font></span>"
                          let num_3 = "<span style='width:24px;height:24px;border-radius:4px;background:#eead3f;display:inline-block;text-align:center;line-height:24px;'><font color='white'>3</font></span>"
                          let str_left = '<li style="margin-bottom: 0.5rem!important;">'+"<a target='_blank' href='"+item.url+"'>";
                          let str_right = "    "+item.title+'</a></li>';
                          switch(num){
                            case 1:
                              lis.push(str_left+num_1+str_right);
                              break;
                            case 2:
                              lis.push(str_left+num_2+str_right);
                              break;
                            case 3:
                              lis.push(str_left+num_3+str_right);
                              break;
                        }
                       }else{
                            // 设置序号的格式 宽高背景颜色以及对齐方式
                            let strnum = "<span style='width:24px;height:24px;border-radius:4px;background:rgba(124,124,124,.3);display:inline-block;text-align:center;line-height:24px;'>" + num + "</span>";
                            let str_all = '<li style="margin-bottom: 0.5rem!important;"><a target="_blank" href="' + item.url + '">' + strnum + ' ' + item.title + '</a></li>';
                            lis.push(str_all);
                       }
                       // 渲染底栏更新时间
                       let footer = elem_name + 'footer'; // Assuming elem_name is a variable containing the element's name
                       let footer_content = '最后更新时间：' + res.update_time; // Assuming res.update_time contains the content to be updated
                       $('#' + footer).html(footer_content); // Update the content of the footer element

                      });

                    // 执行下一页渲染，第二参数为：满足“加载更多”的条件
                    next(lis.join(''), page < res.pages);

                    },
                });
            }
        });
    });
}