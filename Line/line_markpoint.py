import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker

c = (
    Line()
    .add_xaxis(Faker.choose())
    .add_yaxis(
        "商家A",
        Faker.values(),
        markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="min")]),
    )
    .add_yaxis(
        "商家B",
        Faker.values(),
        markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Line-MarkPoint"))
    .render("line_markpoint.html")
)
