import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker

c = (
    Line()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values(), areastyle_opts=opts.AreaStyleOpts(opacity=0.5))
    .add_yaxis("商家B", Faker.values(), areastyle_opts=opts.AreaStyleOpts(opacity=0.5))
    .set_global_opts(title_opts=opts.TitleOpts(title="Line-面积图"))
    .render("line_area_style.html")
)
