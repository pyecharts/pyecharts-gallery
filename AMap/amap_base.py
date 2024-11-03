from pyecharts import options as opts
from pyecharts.charts import AMap
from pyecharts.faker import Faker

# Start from pyecharts version 2.0.7

c = (
    AMap()
    .add_schema(amap_ak="fakekey", center=[120.13066322374, 30.240018034923])
    .add(
        "amap",
        [list(z) for z in zip(Faker.provinces, Faker.values())],
        label_opts=opts.LabelOpts(formatter="{b}"),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="AMap-基本示例"))
    .render("amap_base.html")
)
