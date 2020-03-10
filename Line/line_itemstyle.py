import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker

c = (
    Line()
    .add_xaxis(xaxis_data=Faker.choose())
    .add_yaxis(
        "商家A",
        Faker.values(),
        symbol="triangle",
        symbol_size=20,
        linestyle_opts=opts.LineStyleOpts(color="green", width=4, type_="dashed"),
        itemstyle_opts=opts.ItemStyleOpts(
            border_width=3, border_color="yellow", color="blue"
        ),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Line-ItemStyle"))
    .render("line_itemstyle.html")
)
