from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker

c = (
    Bar()
    .add_xaxis(Faker.days_attrs)
    .add_yaxis("商家A", Faker.days_values, color=Faker.rand_color())
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-DataZoom（slider-垂直）"),
        datazoom_opts=opts.DataZoomOpts(orient="vertical"),
    )
    .render("bar_datazoom_slider_vertical.html")
)
