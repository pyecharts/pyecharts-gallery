
## pyecharts 代码 / 效果

```python
import json

from pyecharts import options as opts
from pyecharts.charts import Tree

with open("flare.json", "r", encoding="utf-8") as f:
    j = json.load(f)
c = (
    Tree()
    .add("", [j], collapse_interval=2, orient="RL")
    .set_global_opts(title_opts=opts.TitleOpts(title="Tree-右左方向"))
    .render("tree_right_left.html")
)

```

<iframe width="100%" height="800px" src="Tree/tree_right_left.html"></iframe>
