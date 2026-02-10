
## pyecharts 代码 / 效果

> 多折线图矩阵

```python
import random
from datetime import datetime, timedelta
from pyecharts import options as opts
from pyecharts.charts import Grid, Line

_matrixDimensionData = {
    "x": ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    "y": [
        {"value": '8:00\n~\n10:00'},
        {"value": '10:00\n~\n12:00'},
        {"value": '12:00\n~\n14:00', "size": 55},
        {"value": '14:00\n~\n16:00'},
        {"value": '16:00\n~\n18:00'},
        {"value": '18:00\n~\n20:00'}
    ]
}

# 生成每个单元格的折线图
def my_callback(xval, yval, xidx, yidx):
    line_chart = (
        Line()
        .add_xaxis(xaxis_data=x_axis_data)
        .add_yaxis(series_name="", y_axis=y_axis_data, symbol="none")
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(type_="category", ...),
            yaxis_opts=opts.AxisOpts(...),
            matrix_opts=opts.MatrixOpts(...),
        )
    )
    return line_chart

# 构建矩阵网格
grid_chart = Grid()
for yidx, yval_item in enumerate(_matrixDimensionData["y"]):
    for xidx, xval_item in enumerate(_matrixDimensionData["x"]):
        sub_chart = my_callback(xval_item, yval, xidx, yidx)
        grid_chart.add(chart=sub_chart, grid_opts=opts.GridOpts(coordinate_system="matrix"))

grid_chart.render("matrix_line.html")
```

<iframe width="100%" height="800px" src="Matrix/matrix_line.html"></iframe>
