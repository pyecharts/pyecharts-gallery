import math
import random

from pyecharts import options as opts
from pyecharts.charts import Custom
from pyecharts.globals import ChartType


# 星期数组
x_data = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# 数据源（首行表头）
data_source = [['Day', 'value']]

for i in range(len(x_data)):
    # 生成数据条数：10 * round(random * 5) + 5
    data_count = 10 * round(random.random() * 5) + 5

    for j in range(data_count):
        value = math.tan(i) / 2 + 3 * random.random() + 2
        data_source.append([x_data[i], value])


c = (
    Custom()
    .register_echarts_x(chart_type=ChartType.VIOLIN)
    .add(
        series_name="violin",
        color_by="item",
        render_item=ChartType.VIOLIN,
        item_payload_opts={
            "symbolSize": 4,
            "areaOpacity": 0.6,
            "bandWidthScale": 1.5,
        },
    )
    .add(
        series_name="scatter",
        type_=ChartType.SCATTER,
        render_item=None,
        encode={"x": 0, "y": 1},
        color_by="item",
    )
    .add_xaxis(xaxis_data=x_data)
    .add_dataset(source=data_source)
    .set_global_opts(
        tooltip_opts=opts.TooltipOpts(is_show=True),
        xaxis_opts={
            "type": "category",
            "jitter": 100,
            "jitterOverlap": False,
        },
        yaxis_opts=None,
        legend_opts={},
    )
    .render("custom_violin.html")
)
