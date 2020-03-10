
## pyecharts 代码 / 效果

```python
from pyecharts import options as opts
from pyecharts.charts import EffectScatter
from pyecharts.faker import Faker

c = (
    EffectScatter()
    .add_xaxis(Faker.choose())
    .add_yaxis("", Faker.values())
    .set_global_opts(title_opts=opts.TitleOpts(title="EffectScatter-基本示例"))
    .render("effectscatter_base.html")
)

```

<iframe width="100%" height="800px" src="EffectScatter/effectscatter_base.html"></iframe>
