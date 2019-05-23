import pyecharts.options as opts
from pyecharts.charts import Candlestick

"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://echarts.baidu.com/examples/editor.html?c=candlestick-simple

目前无法实现的功能:

1、暂无
"""

x_data = ["2017-10-24", "2017-10-25", "2017-10-26", "2017-10-27"]
y_data = [[20, 30, 10, 35], [40, 35, 30, 55], [33, 38, 33, 40], [40, 40, 32, 42]]

(
    Candlestick(init_opts=opts.InitOpts(width="1440px", height="720px"))
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(series_name="", y_axis=y_data)
    .set_series_opts()
    .set_global_opts(
        yaxis_opts=opts.AxisOpts(
            splitline_opts=opts.SplitLineOpts(
                is_show=True, linestyle_opts=opts.LineStyleOpts(width=1)
            )
        )
    )
    .render("basic_candlestick.html")
)
