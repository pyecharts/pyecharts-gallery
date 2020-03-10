
## pyecharts 代码 / 效果

```python
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker


c = (
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-Brush示例", subtitle="我是副标题"),
        brush_opts=opts.BrushOpts(),
    )
    .render("bar_with_brush.html")
)

```

<iframe width="100%" height="800px" src="Bar/bar_with_brush.html"></iframe>
