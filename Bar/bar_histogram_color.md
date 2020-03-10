
## pyecharts 代码 / 效果

```python
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker


x = Faker.dogs + Faker.animal
xlen = len(x)
y = []
for idx, item in enumerate(x):
    if idx <= xlen / 2:
        y.append(
            opts.BarItem(
                name=item,
                value=(idx + 1) * 10,
                itemstyle_opts=opts.ItemStyleOpts(color="#749f83"),
            )
        )
    else:
        y.append(
            opts.BarItem(
                name=item,
                value=(xlen + 1 - idx) * 10,
                itemstyle_opts=opts.ItemStyleOpts(color="#d48265"),
            )
        )

c = (
    Bar()
    .add_xaxis(x)
    .add_yaxis("series0", y, category_gap=0, color=Faker.rand_color())
    .set_global_opts(title_opts=opts.TitleOpts(title="Bar-直方图（颜色区分）"))
    .render("bar_histogram_color.html")
)

```

<iframe width="100%" height="800px" src="Bar/bar_histogram_color.html"></iframe>
