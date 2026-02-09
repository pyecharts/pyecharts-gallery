import random
from datetime import datetime, timedelta

from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.commons.utils import JsCode


x_cnt = 9
y_cnt = 6

c = (
    Pie()
    .set_global_opts(
        legend_opts=opts.LegendOpts(
            is_show=True,
            pos_bottom=40,
        ),
        matrix_opts=opts.MatrixOpts(
            x_data=opts.MatrixAxisOpts(
                data=[
                    opts.MatrixAxisDataOpts(
                        value="Primary School",
                        children=JsCode("Array.from({ length: 5 }, (_, i) => { return `Grade ${i + 1}`; })")
                    ),
                    opts.MatrixAxisDataOpts(
                        value="High School",
                        children=JsCode("Array.from({ length: 4 }, (_, i) => { return `Grade ${i + 6}`; })")
                    ),
                ]
            ),
            y_data=opts.MatrixAxisOpts(
                data=JsCode("Array.from({ length: 6 }, (_, i) => { return `Class ${i + 1}`; })")
            ),
            pos_top=80,
            pos_bottom=80,
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
)

for i in range(x_cnt):
    for j in range(y_cnt):
        c.add(
            series_name=f"pie_{i}_{j}",
            coordinate_system="matrix",
            center=[f"Grade {i+1}", f"Class {j+1}"],
            radius=15,
            data_pair=[
                opts.PieItem(value=round(random.random() * 10) + 10, name="Male"),
                opts.PieItem(value=round(random.random() * 10) + 10, name="Female")
            ],
            label_opts=opts.LabelOpts(is_show=False),
            emphasis_opts=opts.EmphasisOpts(
                label_opts=opts.LabelOpts(is_show=False),
            ),
        )

c.render("matrix_pie.html")
