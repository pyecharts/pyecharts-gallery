from pyecharts.charts import Sunburst
from pyecharts import options as opts

"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://echarts.apache.org/examples/editor.html?c=sunburst-simple

目前无法实现的功能:

1、
"""

data = [
    opts.SunburstItem(
        name="Grandpa",
        children=[
            opts.SunburstItem(
                name="Uncle Leo",
                value=15,
                children=[
                    opts.SunburstItem(name="Cousin Jack", value=2),
                    opts.SunburstItem(
                        name="Cousin Mary",
                        value=5,
                        children=[opts.SunburstItem(name="Jackson", value=2)],
                    ),
                    opts.SunburstItem(name="Cousin Ben", value=4),
                ],
            ),
            opts.SunburstItem(
                name="Father",
                value=10,
                children=[
                    opts.SunburstItem(name="Me", value=5),
                    opts.SunburstItem(name="Brother Peter", value=1),
                ],
            ),
        ],
    ),
    opts.SunburstItem(
        name="Nancy",
        children=[
            opts.SunburstItem(
                name="Uncle Nike",
                children=[
                    opts.SunburstItem(name="Cousin Betty", value=1),
                    opts.SunburstItem(name="Cousin Jenny", value=2),
                ],
            )
        ],
    ),
]

sunburst = (
    Sunburst(init_opts=opts.InitOpts(width="1000px", height="600px"))
    .add(series_name="", data_pair=data, radius=[0, "90%"])
    .set_global_opts(title_opts=opts.TitleOpts(title="Sunburst-基本示例"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}"))
    .render("basic_sunburst.html")
)
