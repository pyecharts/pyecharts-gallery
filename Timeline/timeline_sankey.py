from pyecharts import options as opts
from pyecharts.charts import Sankey, Timeline
from pyecharts.faker import Faker

tl = Timeline()
names = ("商家A", "商家B", "商家C")
nodes = [{"name": name} for name in names]
for i in range(2015, 2020):
    links = [
        {"source": names[0], "target": names[1], "value": Faker.values()[0]},
        {"source": names[1], "target": names[2], "value": Faker.values()[0]},
    ]
    sankey = (
        Sankey()
        .add(
            "sankey",
            nodes,
            links,
            linestyle_opt=opts.LineStyleOpts(opacity=0.2, curve=0.5, color="source"),
            label_opts=opts.LabelOpts(position="right"),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="{}年商店（A, B, C）营业额差".format(i))
        )
    )
    tl.add(sankey, "{}年".format(i))
tl.render("timeline_sankey.html")
