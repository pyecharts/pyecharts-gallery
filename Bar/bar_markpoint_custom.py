from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker

x, y = Faker.choose(), Faker.values()
c = (
    Bar()
    .add_xaxis(x)
    .add_yaxis(
        "商家A",
        y,
        markpoint_opts=opts.MarkPointOpts(
            data=[opts.MarkPointItem(name="自定义标记点", coord=[x[2], y[2]], value=y[2])]
        ),
    )
    .add_yaxis("商家B", Faker.values())
    .set_global_opts(title_opts=opts.TitleOpts(title="Bar-MarkPoint（自定义）"))
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .render("bar_markpoint_custom.html")
)
