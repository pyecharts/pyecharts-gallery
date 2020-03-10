
## pyecharts 代码 / 效果

```python
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker

c = (
    Bar()
    .add_xaxis(Faker.days_attrs)
    .add_yaxis("商家A", Faker.days_values, color=Faker.rand_color())
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-DataZoom（slider-垂直）"),
        datazoom_opts=opts.DataZoomOpts(orient="vertical"),
    )
    .render("bar_datazoom_slider_vertical.html")
)

```

<iframe width="100%" height="800px" src="Bar/bar_datazoom_slider_vertical.html"></iframe>
