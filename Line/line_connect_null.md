
## pyecharts 代码 / 效果

```python
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker

y = Faker.values()
y[3], y[5] = None, None
c = (
    Line()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", y, is_connect_nones=True)
    .set_global_opts(title_opts=opts.TitleOpts(title="Line-连接空数据"))
    .render("line_connect_null.html")
)

```

<iframe width="100%" height="800px" src="Line/line_connect_null.html"></iframe>
