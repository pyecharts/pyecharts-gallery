
## pyecharts 代码 / 效果

```python
from pyecharts import options as opts
from pyecharts.charts import Line, Scatter
from pyecharts.faker import Faker

x = Faker.choose()
line = (
    Line()
    .add_xaxis(x)
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
    .set_global_opts(title_opts=opts.TitleOpts(title="Overlap-line+scatter"))
)
scatter = (
    Scatter()
    .add_xaxis(x)
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
)
line.overlap(scatter)
line.render("overlap_line_scatter.html")

```

<iframe width="100%" height="800px" src="Overlap/overlap_line_scatter.html"></iframe>
