import math
import random

from pyecharts import options as opts
from pyecharts.charts import Custom
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ChartType

data = []
cnt = 300

for i in range(cnt):
    # 按 JS 逻辑计算
    val1 = (math.sin((i / cnt) * math.pi * 2) + random.random() * 0.2 - 0.4) \
           * 100 * random.random()
    val2 = (math.cos((i / cnt) * math.pi * 2) + random.random() * 0.2 - 0.4) \
           * 100 * random.random()
    val3 = random.random() * 10000

    data.append([val1, val2, val3])


c = (
    Custom()
    .register_echarts_x(chart_type=ChartType.CONTOUR)
    .add(
        series_name="data",
        render_item=ChartType.CONTOUR,
        data=data,
        item_payload_opts={
            "itemStyle": {
                "color": ['#5470c6', '#91cc75', '#fac858', '#ee6666'],
            },
            "lineStyle": {
                "opacity": 0.5,
            },
            "bandwidth": 30,
        },
        encode={
            "x": 0,
            "y": 1,
            "tooltip": 2,
        }
    )
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(
            series_index=1,
            min_=0,
            max_=10000,
            range_size=[3, 5],
            type_="continuous",
            is_show=False,
        )
    )
    .render("custom_contour.html")
)
