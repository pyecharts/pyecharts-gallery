#!/usr/bin/env python
# coding=utf-8
import random
import datetime
import pyecharts.options as opts
from pyecharts.charts import Calendar

"""
Gallery 使用 pyecharts 1.0.0
参考地址: https://echarts.baidu.com/examples/editor.html?c=calendar-lunar

目前无法实现的功能:

1、暂时无法设置 legend
"""

begin = datetime.date(2017, 1, 1)
end = datetime.date(2017, 12, 31)
data = [
    [str(begin + datetime.timedelta(days=i)), random.randint(1000, 25000)]
    for i in range((end - begin).days + 1)
]

(
    Calendar(init_opts=opts.InitOpts(width="1600px", height="1000px"))
    .add(
        series_name="",
        yaxis_data=data,
        calendar_opts=opts.CalendarOpts(
            pos_top="120",
            pos_left="30",
            pos_right="30",
            range_="2017",
            yearlabel_opts=opts.LabelOpts(is_show=False),
        ),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(pos_top="30", pos_left="center", title="2017年步数情况"),
        visualmap_opts=opts.VisualMapOpts(
            max_=20000, min_=500, orient="horizontal", is_piecewise=False
        ),
    )
    .render("calendar_heatmap.html")
)
