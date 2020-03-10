
## pyecharts 代码 / 效果

```python
import pyecharts.options as opts
from pyecharts.charts import Bar, Line

"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://www.echartsjs.com/examples/editor.html?c=mix-line-bar

目前无法实现的功能:

1、暂无
"""

x_data = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]

bar = (
    Bar(init_opts=opts.InitOpts(width="1600px", height="800px"))
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="蒸发量",
        yaxis_data=[
            2.0,
            4.9,
            7.0,
            23.2,
            25.6,
            76.7,
            135.6,
            162.2,
            32.6,
            20.0,
            6.4,
            3.3,
        ],
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="降水量",
        yaxis_data=[
            2.6,
            5.9,
            9.0,
            26.4,
            28.7,
            70.7,
            175.6,
            182.2,
            48.7,
            18.8,
            6.0,
            2.3,
        ],
        label_opts=opts.LabelOpts(is_show=False),
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            name="温度",
            type_="value",
            min_=0,
            max_=25,
            interval=5,
            axislabel_opts=opts.LabelOpts(formatter="{value} °C"),
        )
    )
    .set_global_opts(
        tooltip_opts=opts.TooltipOpts(
            is_show=True, trigger="axis", axis_pointer_type="cross"
        ),
        xaxis_opts=opts.AxisOpts(
            type_="category",
            axispointer_opts=opts.AxisPointerOpts(is_show=True, type_="shadow"),
        ),
        yaxis_opts=opts.AxisOpts(
            name="水量",
            type_="value",
            min_=0,
            max_=250,
            interval=50,
            axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
    )
)

line = (
    Line()
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="平均温度",
        yaxis_index=1,
        y_axis=[2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2],
        label_opts=opts.LabelOpts(is_show=False),
    )
)

bar.overlap(line).render("mixed_bar_and_line.html")

```

<iframe width="100%" height="800px" src="Bar/mixed_bar_and_line.html"></iframe>
