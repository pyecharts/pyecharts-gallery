
## pyecharts 代码 / 效果

```python
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker

c = (
    Bar()
    .add_xaxis(Faker.days_attrs)
    .add_yaxis("商家A", Faker.days_values)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-DataZoom（slider-水平）"),
        datazoom_opts=opts.DataZoomOpts(),
    )
    .render("bar_datazoom_slider.html")
)

```

<iframe width="100%" height="800px" src="Bar/bar_datazoom_slider.html"></iframe>
