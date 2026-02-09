
## pyecharts 代码 / 效果

```python
from pyecharts import options as opts
from pyecharts.charts import Chord

c = (
    Chord()
    .add(
        series_name="chord",
        data=[
            opts.ChordData(name="A"),
            opts.ChordData(name="B"),
            opts.ChordData(name="C"),
            opts.ChordData(name="D"),
        ],
        links=[
            opts.ChordLink(source="A", target="B", value=40),
            opts.ChordLink(source="A", target="C", value=20),
            opts.ChordLink(source="B", target="D", value=20),
        ],
        is_clockwise=False,
        label_opts=opts.LabelOpts(is_show=True),
        linestyle_opts=opts.LineStyleOpts(color="target"),
    )
    .render("chord_base.html")
)
```

<iframe width="100%" height="800px" src="Chord/chord_base.html"></iframe>
