
## pyecharts 代码 / 效果

```python
from pyecharts import options as opts
from pyecharts.charts import Map3D
from pyecharts.globals import ChartType

example_data = [
    [[119.107078, 36.70925, 1000], [116.587245, 35.415393, 1000]],
    [[117.000923, 36.675807], [120.355173, 36.082982]],
    [[118.047648, 36.814939], [118.66471, 37.434564]],
    [[121.391382, 37.539297], [119.107078, 36.70925]],
    [[116.587245, 35.415393], [122.116394, 37.509691]],
    [[119.461208, 35.428588], [118.326443, 35.065282]],
    [[116.307428, 37.453968], [115.469381, 35.246531]],
]
c = (
    Map3D()
    .add_schema(
        maptype="山东",
        itemstyle_opts=opts.ItemStyleOpts(
            color="rgb(5,101,123)",
            opacity=1,
            border_width=0.8,
            border_color="rgb(62,215,213)",
        ),
        light_opts=opts.Map3DLightOpts(
            main_color="#fff",
            main_intensity=1.2,
            is_main_shadow=False,
            main_alpha=55,
            main_beta=10,
            ambient_intensity=0.3,
        ),
        view_control_opts=opts.Map3DViewControlOpts(center=[-10, 0, 10]),
        post_effect_opts=opts.Map3DPostEffectOpts(is_enable=False),
    )
    .add(
        series_name="",
        data_pair=example_data,
        type_=ChartType.LINES3D,
        effect=opts.Lines3DEffectOpts(
            is_show=True,
            period=4,
            trail_width=3,
            trail_length=0.5,
            trail_color="#f00",
            trail_opacity=1,
        ),
        linestyle_opts=opts.LineStyleOpts(is_show=False, color="#fff", opacity=0),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Map3D-Lines3D"))
    .render("map3d_with_lines3d.html")
)

```

<iframe width="100%" height="800px" src="Map3D/map3d_with_lines3d.html"></iframe>
