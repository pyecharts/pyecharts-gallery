
## pyecharts 代码 / 效果

```python
from pyecharts.charts import Bar
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType

c = (
    Bar({"theme": ThemeType.MACARONS})
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
    .set_global_opts(
        title_opts={"text": "Bar-通过 dict 进行配置", "subtext": "我也是通过 dict 进行配置的"}
    )
    .render("bar_base_dict_config.html")
)

```

<iframe width="100%" height="800px" src="Bar/bar_base_dict_config.html"></iframe>
