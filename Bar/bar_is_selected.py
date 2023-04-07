from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker


c = (
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-默认取消显示某 Series"),
        legend_opts=opts.LegendOpts(selected_map={"商家B": False}),
    )
    .render("bar_is_selected.html")
)
