
## pyecharts 代码 / 效果

```python
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker

c = (
    Line()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
    .set_global_opts(title_opts=opts.TitleOpts(title="Line-基本示例"))
    .render("line_base.html")
)

```

<iframe width="100%" height="800px" src="Line/line_base.html"></iframe>
