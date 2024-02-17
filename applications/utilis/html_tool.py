# 组装html
def generate_html(res_data):
    html_result = []  # 用于存储HTML结果的列表

    res = res_data['data']

    for item in res:
        num = item['index']

        # 初始化图片标签
        img = ""

        if num <= 3:
            img_1 = "<img src='static/img/no1.png' width='32' height='18'>"
            img_2 = "<img src='static/img/no2.png' width='32' height='18'>"
            img_3 = "<img src='static/img/no3.png' width='32' height='18'>"
            str_left = f"<li style='margin-bottom: 0.5rem!important;'><a target='_blank' href='{item['url']}'>"

            str_right = f"    {item['title']} </a></li>"

            # 根据num3的值选择图片
            if num == 1:
                html_result.append(str_left + img_1 + str_right)
            elif num == 2:
                html_result.append(str_left + img_2 + str_right)
            elif num == 3:
                html_result.append(str_left + img_3 + str_right)
        else:
            # 设置序号的格式及样式
            strnum = f"<span style='width:32px;height:18px;border-radius:4px;background:rgba(124,124,124,.3);display:inline-block;text-align:center;line-height:18px;'>{str(num)}</span>"
            str_all = f"<li style='margin-bottom: 0.5rem!important;'><a target='_blank' href='{item['url']}'>{strnum} {item['title']}</a></li>"
            html_result.append(str_all)

    # 将HTML结果列表转换为字符串返回
    # return ''.join(html_result)
    return html_result
