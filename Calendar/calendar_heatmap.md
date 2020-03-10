
## pyecharts 代码 / 效果

```python
import random
import datetime

import pyecharts.options as opts
from pyecharts.charts import Calendar


begin = datetime.date(2017, 1, 1)
end = datetime.date(2017, 12, 31)
data = [
    [str(begin + datetime.timedelta(days=i)), random.randint(1000, 25000)]
    for i in range((end - begin).days + 1)
]

(
    Calendar(init_opts=opts.InitOpts(width="1600px", height="1000px"))
    .add(
        series_name="",
        yaxis_data=data,
        calendar_opts=opts.CalendarOpts(
            pos_top="120",
            pos_left="30",
            pos_right="30",
            range_="2017",
            yearlabel_opts=opts.CalendarYearLabelOpts(is_show=False),
        ),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(pos_top="30", pos_left="center", title="2017年步数情况"),
        visualmap_opts=opts.VisualMapOpts(
            max_=20000, min_=500, orient="horizontal", is_piecewise=False
        ),
    )
    .render("calendar_heatmap.html")
)

```

<iframe width="100%" height="800px" src="Calendar/calendar_heatmap.html"></iframe>
