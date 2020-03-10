
## pyecharts 代码 / 效果

```python
from pyecharts import options as opts
from pyecharts.charts import Map3D
from pyecharts.globals import ChartType
from pyecharts.commons.utils import JsCode

example_data = [
    ("黑龙江", [127.9688, 45.368, 100]),
    ("内蒙古", [110.3467, 41.4899, 100]),
    ("吉林", [125.8154, 44.2584, 100]),
    ("辽宁", [123.1238, 42.1216, 100]),
    ("河北", [114.4995, 38.1006, 100]),
    ("天津", [117.4219, 39.4189, 100]),
    ("山西", [112.3352, 37.9413, 100]),
    ("陕西", [109.1162, 34.2004, 100]),
    ("甘肃", [103.5901, 36.3043, 100]),
    ("宁夏", [106.3586, 38.1775, 100]),
    ("青海", [101.4038, 36.8207, 100]),
    ("新疆", [87.9236, 43.5883, 100]),
    ("西藏", [91.11, 29.97, 100]),
    ("四川", [103.9526, 30.7617, 100]),
    ("重庆", [108.384366, 30.439702, 100]),
    ("山东", [117.1582, 36.8701, 100]),
    ("河南", [113.4668, 34.6234, 100]),
    ("江苏", [118.8062, 31.9208, 100]),
    ("安徽", [117.29, 32.0581, 100]),
    ("湖北", [114.3896, 30.6628, 100]),
    ("浙江", [119.5313, 29.8773, 100]),
    ("福建", [119.4543, 25.9222, 100]),
    ("江西", [116.0046, 28.6633, 100]),
    ("湖南", [113.0823, 28.2568, 100]),
    ("贵州", [106.6992, 26.7682, 100]),
    ("广西", [108.479, 23.1152, 100]),
    ("海南", [110.3893, 19.8516, 100]),
    ("上海", [121.4648, 31.2891, 100]),
]

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
            is_show=False,
            formatter=JsCode("function(data){return data.name + " " + data.value[2];}"),
        ),
        emphasis_label_opts=opts.LabelOpts(
            is_show=False,
            color="#fff",
            font_size=10,
            background_color="rgba(0,23,11,0)",
        ),
        light_opts=opts.Map3DLightOpts(
            main_color="#fff",
            main_intensity=1.2,
            main_shadow_quality="high",
            is_main_shadow=False,
            main_beta=10,
            ambient_intensity=0.3,
        ),
    )
    .add(
        series_name="Scatter3D",
        data_pair=example_data,
        type_=ChartType.SCATTER3D,
        bar_size=1,
        shading="lambert",
        label_opts=opts.LabelOpts(
            is_show=False,
            formatter=JsCode("function(data){return data.name + ' ' + data.value[2];}"),
        ),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Map3D-Scatter3D"))
    .render("map3d_with_scatter3d.html")
)

```

<iframe width="100%" height="800px" src="Map3D/map3d_with_scatter3d.html"></iframe>
