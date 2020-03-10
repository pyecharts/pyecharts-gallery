import json

from pyecharts import options as opts
from pyecharts.charts import Tree


with open("flare.json", "r", encoding="utf-8") as f:
    j = json.load(f)
c = (
    Tree()
    .add(
        "",
        [j],
        collapse_interval=2,
        orient="TB",
        label_opts=opts.LabelOpts(
            position="top",
            horizontal_align="right",
            vertical_align="middle",
            rotate=-90,
        ),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Tree-上下方向"))
    .render("tree_top_bottom.html")
)
