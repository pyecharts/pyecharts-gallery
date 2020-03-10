import pyecharts.options as opts
from pyecharts.charts import Line

c = (
    Line()
    .add_xaxis(xaxis_data=["一", "二", "三", "四", "五", "六", "七", "八", "九"])
    .add_yaxis(
        "2 的指数",
        y_axis=[1, 2, 4, 8, 16, 32, 64, 128, 256],
        linestyle_opts=opts.LineStyleOpts(width=2),
    )
    .add_yaxis(
        "3 的指数",
        y_axis=[1, 3, 9, 27, 81, 247, 741, 2223, 6669],
        linestyle_opts=opts.LineStyleOpts(width=2),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Line-对数轴示例"),
        xaxis_opts=opts.AxisOpts(name="x"),
        yaxis_opts=opts.AxisOpts(
            type_="log",
            name="y",
            splitline_opts=opts.SplitLineOpts(is_show=True),
            is_scale=True,
        ),
    )
    .render("line_yaxis_log.html")
)
