#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

import pyecharts.options as opts
from pyecharts.charts import Parallel

"""
Gallery 使用 Pyecharts 1.0.0
参考地址: https://echarts.baidu.com/examples/editor.html?c=parallel-simple

目前无法实现的功能:

1、
"""

parallel_axis = [
    {"dim": 0, "name": "Price"},
    {"dim": 1, "name": "Net Weight"},
    {"dim": 2, "name": "Amount"},
    {
        "dim": 3,
        "name": "Score",
        "type": "category",
        "data": ["Excellent", "Good", "OK", "Bad"],
    },
]

data = [[12.99, 100, 82, "Good"], [9.99, 80, 77, "OK"], [20, 120, 60, "Excellent"]]


(
    Parallel(init_opts=opts.InitOpts(width="1400px", height="800px"))
    .add_schema(schema=parallel_axis)
    .add(
        series_name="",
        data=data,
        linestyle_opts=opts.LineStyleOpts(width=4, opacity=0.5),
    )
    .render("basic_parallel.html")
)
