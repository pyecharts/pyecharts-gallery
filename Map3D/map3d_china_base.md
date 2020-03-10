
## pyecharts 代码 / 效果

```python
from pyecharts import options as opts
from pyecharts.charts import Map3D
from pyecharts.globals import ChartType

c = (
    Map3D()
    .add_schema(
        itemstyle_opts=opts.ItemStyleOpts(
            color="rgb(5,101,123)",
            opacity=1,
            border_width=0.8,
            border_color="rgb(62,215,213)",
        ),
        map3d_label=opts.Map3DLabelOpts(
            is_show=True,
            text_style=opts.TextStyleOpts(
                color="#fff", font_size=16, background_color="rgba(0,0,0,0)"
            ),
        ),
        emphasis_label_opts=opts.LabelOpts(is_show=True),
        light_opts=opts.Map3DLightOpts(
            main_color="#fff",
            main_intensity=1.2,
            is_main_shadow=False,
            main_alpha=55,
            main_beta=10,
            ambient_intensity=0.3,
        ),
    )
    .add(series_name="", data_pair="", maptype=ChartType.MAP3D)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="全国行政区划地图-Base"),
        visualmap_opts=opts.VisualMapOpts(is_show=False),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
    .render("map3d_china_base.html")
)

```

<iframe width="100%" height="800px" src="Map3D/map3d_china_base.html"></iframe>
