
## pyecharts 代码 / 效果

```python
import pyecharts.options as opts
from pyecharts.charts import Line

"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://www.echartsjs.com/examples/editor.html?c=line-log

目前无法实现的功能:

1、暂无
"""

x_data = ["一", "二", "三", "四", "五", "六", "七", "八", "九"]
y_data_3 = [1, 3, 9, 27, 81, 247, 741, 2223, 6669]
y_data_2 = [1, 2, 4, 8, 16, 32, 64, 128, 256]
y_data_05 = [1 / 2, 1 / 4, 1 / 8, 1 / 16, 1 / 32, 1 / 64, 1 / 128, 1 / 256, 1 / 512]


(
    Line(init_opts=opts.InitOpts(width="1600px", height="800px"))
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="1/2的指数",
        y_axis=y_data_05,
        linestyle_opts=opts.LineStyleOpts(width=2),
    )
    .add_yaxis(
        series_name="2的指数", y_axis=y_data_2, linestyle_opts=opts.LineStyleOpts(width=2)
    )
    .add_yaxis(
        series_name="3的指数", y_axis=y_data_3, linestyle_opts=opts.LineStyleOpts(width=2)
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="对数轴示例", pos_left="center"),
        tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b} : {c}"),
        legend_opts=opts.LegendOpts(pos_left="left"),
        xaxis_opts=opts.AxisOpts(type_="category", name="x"),
        yaxis_opts=opts.AxisOpts(
            type_="log",
            name="y",
            splitline_opts=opts.SplitLineOpts(is_show=True),
            is_scale=True,
        ),
    )
    .render("log_axis.html")
)

```

<iframe width="100%" height="800px" src="Line/log_axis.html"></iframe>
