
## pyecharts 代码 / 效果

```python
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker


c = (
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values(), category_gap="80%")
    .set_global_opts(title_opts=opts.TitleOpts(title="Bar-单系列柱间距离"))
    .render("bar_same_series_gap.html")
)

```

<iframe width="100%" height="800px" src="Bar/bar_same_series_gap.html"></iframe>
