from pyecharts import options as opts
from pyecharts.charts import Map, Timeline
from pyecharts.faker import Faker

tl = Timeline()
for i in range(2015, 2020):
    map0 = (
        Map()
        .add("商家A", [list(z) for z in zip(Faker.provinces, Faker.values())], "china")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Map-{}年某些数据".format(i)),
            visualmap_opts=opts.VisualMapOpts(max_=200),
        )
    )
    tl.add(map0, "{}年".format(i))
tl.render("timeline_map.html")
