import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker

c = (
    Line()
    .add_xaxis(Faker.choose())
    .add_yaxis(
        "商家A",
        Faker.values(),
        markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
    )
    .add_yaxis(
        "商家B",
        Faker.values(),
        markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Line-MarkLine"))
    .render("line_markline.html")
)
