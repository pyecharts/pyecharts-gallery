
## pyecharts 代码 / 效果

> MBTI 性格匹配矩阵热力图

```python
from pyecharts import options as opts
from pyecharts.charts import HeatMap, Scatter
from pyecharts.commons.utils import JsCode

mbti = ['ENFJ', 'ENFP', 'ENTJ', 'ENTP', 'ESFJ', 'ESFP', 'ESTJ', 'ESTP',
        'INFJ', 'INFP', 'INTJ', 'INTP', 'ISFJ', 'ISFP', 'ISTJ', 'ISTP']

# 数据准备...
heatmap_data = []
scatter_data = []

s = (
    Scatter()
    .add_xaxis(xaxis_data=[...])
    .add_yaxis(series_name="scatter", coordinate_system="matrix", ...)
)

h = (
    HeatMap(init_opts=opts.InitOpts(bg_color="#F0F7F9"))
    .add_yaxis(series_name="heatmap", yaxis_data=[], value=heatmap_data, coordinate_system="matrix")
    .overlap(chart=s)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="MBTI Partner Compatibility"),
        matrix_opts=opts.MatrixOpts(...),
        visualmap_opts=[opts.VisualMapOpts(type_="continuous", min_=0, max_=1)],
    )
)
h.render("matrix_heatmap_mbti.html")
```

<iframe width="100%" height="800px" src="Matrix/matrix_heatmap_mbti.html"></iframe>
