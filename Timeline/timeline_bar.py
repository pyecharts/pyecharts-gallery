from pyecharts import options as opts
from pyecharts.charts import Bar, Timeline
from pyecharts.faker import Faker

x = Faker.choose()
tl = Timeline()
for i in range(2015, 2020):
    bar = (
        Bar()
        .add_xaxis(x)
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts("某商店{}年营业额".format(i)))
    )
    tl.add(bar, "{}年".format(i))
tl.render("timeline_bar.html")
