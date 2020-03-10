
## pyecharts 代码 / 效果

```python
import json

from pyecharts.charts import BMap
from pyecharts import options as opts

"""
参考地址: https://gallery.echartsjs.com/editor.html?c=bmap-bus
"""

BAIDU_MAP_AK = "FAKE_AK"

# 读取项目中的 json 文件
with open("busRoutines.json", "r", encoding="utf-8") as f:
    bus_lines = json.load(f)

c = (
    BMap(init_opts=opts.InitOpts(width="1200px", height="800px"))
    .add_schema(
        baidu_ak=BAIDU_MAP_AK,
        center=[116.40, 40.04],
        zoom=10,
        is_roam=True,
        map_style={
            "styleJson": [
                {
                    "featureType": "water",
                    "elementType": "all",
                    "stylers": {"color": "#031628"},
                },
                {
                    "featureType": "land",
                    "elementType": "geometry",
                    "stylers": {"color": "#000102"},
                },
                {
                    "featureType": "highway",
                    "elementType": "all",
                    "stylers": {"visibility": "off"},
                },
                {
                    "featureType": "arterial",
                    "elementType": "geometry.fill",
                    "stylers": {"color": "#000000"},
                },
                {
                    "featureType": "arterial",
                    "elementType": "geometry.stroke",
                    "stylers": {"color": "#0b3d51"},
                },
                {
                    "featureType": "local",
                    "elementType": "geometry",
                    "stylers": {"color": "#000000"},
                },
                {
                    "featureType": "railway",
                    "elementType": "geometry.fill",
                    "stylers": {"color": "#000000"},
                },
                {
                    "featureType": "railway",
                    "elementType": "geometry.stroke",
                    "stylers": {"color": "#08304b"},
                },
                {
                    "featureType": "subway",
                    "elementType": "geometry",
                    "stylers": {"lightness": -70},
                },
                {
                    "featureType": "building",
                    "elementType": "geometry.fill",
                    "stylers": {"color": "#000000"},
                },
                {
                    "featureType": "all",
                    "elementType": "labels.text.fill",
                    "stylers": {"color": "#857f7f"},
                },
                {
                    "featureType": "all",
                    "elementType": "labels.text.stroke",
                    "stylers": {"color": "#000000"},
                },
                {
                    "featureType": "building",
                    "elementType": "geometry",
                    "stylers": {"color": "#022338"},
                },
                {
                    "featureType": "green",
                    "elementType": "geometry",
                    "stylers": {"color": "#062032"},
                },
                {
                    "featureType": "boundary",
                    "elementType": "all",
                    "stylers": {"color": "#465b6c"},
                },
                {
                    "featureType": "manmade",
                    "elementType": "all",
                    "stylers": {"color": "#022338"},
                },
                {
                    "featureType": "label",
                    "elementType": "all",
                    "stylers": {"visibility": "off"},
                },
            ]
        },
    )
    .add(
        "",
        type_="lines",
        is_polyline=True,
        data_pair=bus_lines,
        linestyle_opts=opts.LineStyleOpts(opacity=0.2, width=0.5),
        # 如果不是最新版本的话可以注释下面的参数（效果差距不大）
        progressive=200,
        progressive_threshold=500,
    )
    .render("bmap_beijing_bus_routines.html")
)

```

<iframe width="100%" height="800px" src="BMap/bmap_beijing_bus_routines.html"></iframe>
