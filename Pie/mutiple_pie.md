
## pyecharts 代码 / 效果

```python
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.commons.utils import JsCode


fn = """
    function(params) {
        if(params.name == '其他')
            return '\\n\\n\\n' + params.name + ' : ' + params.value + '%';
        return params.name + ' : ' + params.value + '%';
    }
    """


def new_label_opts():
    return opts.LabelOpts(formatter=JsCode(fn), position="center")


c = (
    Pie()
    .add(
        "",
        [list(z) for z in zip(["剧情", "其他"], [25, 75])],
        center=["20%", "30%"],
        radius=[60, 80],
        label_opts=new_label_opts(),
    )
    .add(
        "",
        [list(z) for z in zip(["奇幻", "其他"], [24, 76])],
        center=["55%", "30%"],
        radius=[60, 80],
        label_opts=new_label_opts(),
    )
    .add(
        "",
        [list(z) for z in zip(["爱情", "其他"], [14, 86])],
        center=["20%", "70%"],
        radius=[60, 80],
        label_opts=new_label_opts(),
    )
    .add(
        "",
        [list(z) for z in zip(["惊悚", "其他"], [11, 89])],
        center=["55%", "70%"],
        radius=[60, 80],
        label_opts=new_label_opts(),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Pie-多饼图基本示例"),
        legend_opts=opts.LegendOpts(
            type_="scroll", pos_top="20%", pos_left="80%", orient="vertical"
        ),
    )
    .render("mutiple_pie.html")
)

```

<iframe width="100%" height="800px" src="Pie/mutiple_pie.html"></iframe>
