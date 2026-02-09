import random
from datetime import datetime, timedelta

from pyecharts import options as opts
from pyecharts.charts import Scatter
from pyecharts.commons.utils import JsCode


xCnt = 10
yCnt = 6

xData = [{"value": f"X{i+1}"} for i in range(xCnt)]
yData = [{"value": f"Y{i+1}"} for i in range(yCnt)]

data = []
for i in range(1, xCnt + 1):
    for j in range(1, yCnt + 1):
        data.append([f"X{i}", f"Y{j}", random.random() * 2 - 1])

scatter_x = [item[0] for item in data]
scatter_y = [item[1:] for item in data]


c = (
    Scatter()
    .set_global_opts(
        matrix_opts=opts.MatrixOpts(
            x_data=opts.MatrixAxisOpts(data=xData),
            y_data=opts.MatrixAxisOpts(data=yData),
            pos_top=80,
        ),
        visualmap_opts=opts.VisualMapOpts(
            type_="continuous",
            min_=-1,
            max_=1,
            dimension=2,
            is_calculable=True,
            orient="horizontal",
            pos_top=5,
            pos_left="center",
            range_color=[
                '#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8',
                '#ffffbf', '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026'
            ],
            range_size=[15, 40]
        ),
        xaxis_opts=opts.AxisOpts(is_show=False),
        yaxis_opts=opts.AxisOpts(is_show=False),
        legend_opts=opts.LegendOpts(is_show=False),
    )
    .add_xaxis(xaxis_data=scatter_x)
    .add_yaxis(
        series_name="0",
        y_axis=scatter_y,
        coordinate_system="matrix",
        itemstyle_opts=opts.ItemStyleOpts(opacity=1),
        label_opts=opts.LabelOpts(
            is_show=True,
            formatter=JsCode("(params) => params.value[2].toFixed(2)"),
        )
    )
)
c.render("matrix_scatter.html")
