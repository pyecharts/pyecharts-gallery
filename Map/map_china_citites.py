from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker

c = (
    Map()
    .add(
        "商家A",
        [list(z) for z in zip(Faker.guangdong_city, Faker.values())],
        "china-cities",
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Map-中国地图（带城市）"),
        visualmap_opts=opts.VisualMapOpts(),
    )
    .render("map_china_cities.html")
)
