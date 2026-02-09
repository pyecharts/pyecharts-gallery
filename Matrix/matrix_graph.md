
## pyecharts 代码 / 效果

> 课程先决条件关系图 - Matrix 坐标系

```python
import math
from pyecharts import options as opts
from pyecharts.charts import Graph
from pyecharts.commons.utils import JsCode

c = (
    Graph()
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Course Prerequisites"),
        matrix_opts=opts.MatrixOpts(
            x_data=opts.MatrixAxisOpts(data=['Data Analysis', 'Programming', 'Algorithms']),
            y_data=opts.MatrixAxisOpts(data=['1st Year', '2nd Year', '3rd Year', '4th Year']),
            pos_left=80, pos_right=80, pos_top=150, pos_bottom=150,
        ),
    )
    .add(
        series_name="course",
        coordinate_system="matrix",
        edge_symbol=["none", "arrow"],
        symbol_size=15,
        links=[...],
        nodes=[...],
    )
)
c.render("matrix_graph.html")
```

<iframe width="100%" height="800px" src="Matrix/matrix_graph.html"></iframe>
