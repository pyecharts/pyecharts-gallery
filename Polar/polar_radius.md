
## pyecharts 代码 / 效果

```python
from pyecharts import options as opts
from pyecharts.charts import Polar
from pyecharts.faker import Faker

c = (
    Polar()
    .add_schema(
        radiusaxis_opts=opts.RadiusAxisOpts(data=Faker.week, type_="category"),
        angleaxis_opts=opts.AngleAxisOpts(is_clockwise=True, max_=10),
    )
    .add("A", [1, 2, 3, 4, 3, 5, 1], type_="bar")
    .set_global_opts(title_opts=opts.TitleOpts(title="Polar-RadiusAxis"))
    .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
    .render("polar_radius.html")
)

```

<iframe width="100%" height="800px" src="Polar/polar_radius.html"></iframe>
