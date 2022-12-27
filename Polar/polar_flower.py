import math

from pyecharts import options as opts
from pyecharts.charts import Polar

data = []
for i in range(361):
    t = i / 180 * math.pi
    r = math.sin(2 * t) * math.cos(2 * t)
    data.append([r, i])
c = (
    Polar()
    .add_schema(
        angleaxis_opts=opts.AngleAxisOpts(
            type_="value",
            boundary_gap=False,
            start_angle=0,
            split_number=12,
            is_clockwise=True,
        )
    )
    .add("flower", data, label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="Polar-Flower"))
    .render("polar_flower.html")
)
