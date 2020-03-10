import json

from pyecharts import options as opts
from pyecharts.charts import PictorialBar

location = ["山西", "四川", "西藏", "北京", "上海", "内蒙古", "云南", "黑龙江", "广东", "福建"]
values = [13, 42, 67, 81, 86, 94, 166, 220, 249, 262]


with open("symbol.json", "r", encoding="utf-8") as f:
    symbols = json.load(f)

c = (
    PictorialBar()
    .add_xaxis(["reindeer", "ship", "plane", "train", "car"])
    .add_yaxis(
        "2015",
        [
            {"value": 157, "symbol": symbols["reindeer"]},
            {"value": 21, "symbol": symbols["ship"]},
            {"value": 66, "symbol": symbols["plane"]},
            {"value": 78, "symbol": symbols["train"]},
            {"value": 123, "symbol": symbols["car"]},
        ],
        label_opts=opts.LabelOpts(is_show=False),
        symbol_size=22,
        symbol_repeat="fixed",
        symbol_offset=[0, 5],
        is_symbol_clip=True,
    )
    .add_yaxis(
        "2016",
        [
            {"value": 184, "symbol": symbols["reindeer"]},
            {"value": 29, "symbol": symbols["ship"]},
            {"value": 73, "symbol": symbols["plane"]},
            {"value": 91, "symbol": symbols["train"]},
            {"value": 95, "symbol": symbols["car"]},
        ],
        label_opts=opts.LabelOpts(is_show=False),
        symbol_size=22,
        symbol_repeat="fixed",
        symbol_offset=[0, -25],
        is_symbol_clip=True,
    )
    .reversal_axis()
    .set_global_opts(
        title_opts=opts.TitleOpts(title="PictorialBar-Vehicles in X City"),
        xaxis_opts=opts.AxisOpts(is_show=False),
        yaxis_opts=opts.AxisOpts(
            axistick_opts=opts.AxisTickOpts(is_show=False),
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(opacity=0)
            ),
        ),
    )
    .render("pictorialbar_multi_custom_symbols.html")
)
