from pyecharts import options as opts
from pyecharts.charts import BMap, Timeline
from pyecharts.faker import Faker

tl = Timeline()
tl.add_schema(pos_left="50%", pos_right="10px", pos_bottom="15px")
for i in range(2015, 2020):
    bmap = (
        BMap()
        .add_schema(baidu_ak="FAKE_AK", center=[120.13066322374, 30.240018034923])
        .add(
            "bmap",
            [list(z) for z in zip(Faker.provinces, Faker.values())],
            type_="heatmap",
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Timeline-BMap-热力图-{}年".format(i)),
            visualmap_opts=opts.VisualMapOpts(pos_bottom="center", pos_right="10px"),
            tooltip_opts=opts.TooltipOpts(formatter=None),
        )
    )
    tl.add(bmap, "{}年".format(i))
tl.render("timeline_bmap.html")
