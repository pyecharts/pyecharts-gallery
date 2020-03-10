
## pyecharts 代码 / 效果

```python
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode
from pyecharts.faker import Faker


color_function = """
        function (params) {
            if (params.value > 0 && params.value < 50) {
                return 'red';
            } else if (params.value > 50 && params.value < 100) {
                return 'blue';
            }
            return 'green';
        }
        """
c = (
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis(
        "商家A",
        Faker.values(),
        itemstyle_opts=opts.ItemStyleOpts(color=JsCode(color_function)),
    )
    .add_yaxis(
        "商家B",
        Faker.values(),
        itemstyle_opts=opts.ItemStyleOpts(color=JsCode(color_function)),
    )
    .add_yaxis(
        "商家C",
        Faker.values(),
        itemstyle_opts=opts.ItemStyleOpts(color=JsCode(color_function)),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Bar-自定义柱状颜色"))
    .render("bar_custom_bar_color.html")
)

```

<iframe width="100%" height="800px" src="Bar/bar_custom_bar_color.html"></iframe>
