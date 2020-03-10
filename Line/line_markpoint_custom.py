import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker

x, y = Faker.choose(), Faker.values()
c = (
    Line()
    .add_xaxis(x)
    .add_yaxis(
        "商家A",
        y,
        markpoint_opts=opts.MarkPointOpts(
            data=[opts.MarkPointItem(name="自定义标记点", coord=[x[2], y[2]], value=y[2])]
        ),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Line-MarkPoint（自定义）"))
    .render("line_markpoint_custom.html")
)
