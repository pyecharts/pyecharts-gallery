
## pyecharts 代码 / 效果

```python
from pyecharts import options as opts
from pyecharts.charts import Scatter
from pyecharts.faker import Faker

c = (
    Scatter()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Scatter-VisualMap(Color)"),
        visualmap_opts=opts.VisualMapOpts(max_=150),
    )
    .render("scatter_visualmap_color.html")
)

```

<iframe width="100%" height="800px" src="Scatter/scatter_visualmap_color.html"></iframe>
