
## pyecharts 代码 / 效果

* 需要 pyecharts 2.0.7+ 以上版本才有该图例（Requires pyecharts 2.0.7+ or higher to have this chart）

```python
from pyecharts import options as opts
from pyecharts.charts import AMap
from pyecharts.faker import Faker

c = (
    AMap()
    .add_schema(amap_ak="fakekey", center=[120.13066322374, 30.240018034923])
    .add(
        "amap",
        [list(z) for z in zip(Faker.provinces, Faker.values())],
        label_opts=opts.LabelOpts(formatter="{b}"),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="AMap-基本示例"))
    .render("amap_base.html")
)

# 下面的示例大概率无法展示，原因是需要一个有效的 amap_ak，需要自行申请！
# There is a high probability that the following example will not be displayed, due to the need for a valid amap_ak, which needs to be requested on its own!
```

<iframe width="100%" height="800px" src="AMap/amap_base.html"></iframe>