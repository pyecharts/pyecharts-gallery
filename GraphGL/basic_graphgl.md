
## pyecharts 代码 / 效果

```python
import random

from pyecharts import options as opts
from pyecharts.charts import GraphGL


nodes = []
for i in range(50):
    for j in range(50):
        nodes.append(
            opts.GraphGLNode(
                x=random.random() * 958,
                y=random.random() * 777,
                value=1,
            )
        )

links = []
for i in range(50):
    for j in range(50):
        if i < 50 - 1:
            links.append(
                opts.GraphGLLink(
                    source=i + j * 50,
                    target=i + 1 + j * 50,
                    value=1,
                )
            )
        if j < 50 - 1:
            links.append(
                opts.GraphGLLink(
                    source=i + j * 50,
                    target=i + (j + 1) * 50,
                    value=1,
                )
            )

c = (
    GraphGL(init_opts=opts.InitOpts())
    .add(
        series_name="",
        nodes=nodes,
        links=links,
        itemstyle_opts=opts.ItemStyleOpts(color="rgba(255,255,255,0.8)"),
        linestyle_opts=opts.LineStyleOpts(color="rgba(255,255,255,0.8)", width=3),
        force_atlas2_opts=opts.GraphGLForceAtlas2Opts(
            steps=5,
            edge_weight_influence=4,
        ),
    )
    .set_dark_mode()
    .render("basic_graphgl.html")
)

```

<iframe width="100%" height="800px" src="GraphGL/basic_graphgl.html"></iframe>
