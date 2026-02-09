import random
from datetime import datetime, timedelta

from pyecharts import options as opts
from pyecharts.charts import Grid, Line
from pyecharts.commons.utils import JsCode


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

_yBreakTimeIndex = 2
_seriesFakeDataLength = 365


def make_id(xidx, yidx):
    return f"{xidx}|{yidx}"


def generate_fake_series_data(day_count, xidx, yidx):
    day_start = datetime(2025, 5, 5)
    day_start = day_start.replace(day=(xidx + 5))

    time_start = day_start
    seven_day = timedelta(days=7)

    cell_data = []
    last_val = int(random.random() * 300)
    turn_count = None
    sign = -1

    for idx in range(day_count):
        if turn_count is None or idx >= turn_count:
            turn_count = idx + round((day_count / 4) * ((random.random() - 0.5) * 0.1))
            sign = -sign

        delta_mag = 50
        delta = int(random.random() * delta_mag - delta_mag / 2 + (sign * delta_mag) / 3)
        last_val = max(0, last_val + delta)

        x_time = time_start + idx * seven_day
        data_x_val = x_time.strftime("%Y-%m-%d")
        cell_data.append([data_x_val, last_val])

    return cell_data


def my_callback(xval, yval, xidx, yidx):
    _id = make_id(xidx, yidx)
    fake_data = generate_fake_series_data(_seriesFakeDataLength, xidx, yidx)

    x_axis_data = [item[0] for item in fake_data]
    y_axis_data = [item[1] for item in fake_data]

    line_chart = (
        Line()
        .add_xaxis(xaxis_data=x_axis_data)
        .add_yaxis(
            series_name="",
            xaxis_id=_id,
            yaxis_id=_id,
            symbol="none",
            linestyle_opts=opts.LineStyleOpts(width=1),
            y_axis=y_axis_data,
        )
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(
                type_="category",
                grid_id=_id,
                is_scale=True,
                axistick_opts=opts.AxisTickOpts(is_show=False),
                axislabel_opts=opts.LabelOpts(is_show=False),
                axisline_opts=opts.AxisLineOpts(is_show=False),
                splitline_opts=opts.SplitLineOpts(is_show=False),
            ),
            yaxis_opts=opts.AxisOpts(
                grid_id=_id,
                interval=9007199254740991,
                is_scale=True,
                axisline_opts=opts.AxisLineOpts(is_show=False),
                axistick_opts=opts.AxisTickOpts(is_show=False),
            ),
            tooltip_opts=opts.TooltipOpts(trigger="axis"),
            datazoom_opts=[
                opts.DataZoomOpts(
                    type_="slider",
                    xaxis_index="all",
                    pos_left="10%",
                    pos_right="10%",
                    pos_bottom=30,
                    height=30,
                    throttle=120,
                    range_start=None,
                    range_end=None,
                ),
                opts.DataZoomOpts(
                    type_="inside",
                    xaxis_index="all",
                    throttle=120,
                    range_start=None,
                    range_end=None,
                )
            ],
            matrix_opts=opts.MatrixOpts(
                x_data=opts.MatrixAxisOpts(
                    data=_matrixDimensionData["x"],
                    level_size=40,
                    label_opts=opts.LabelOpts(font_size=16, color="#555")
                ),
                y_data=opts.MatrixAxisOpts(
                    data=_matrixDimensionData["y"],
                    level_size=70,
                    label_opts=opts.LabelOpts(font_size=14, color="#777")
                ),
                corner_opts=opts.MatrixBodyOrCornerOpts(
                    data=[opts.MatrixBodyDataOpts(coord=[-1, -1], value="Time")],
                    label_opts=opts.LabelOpts(font_size=16, color="#777"),
                ),
                body_opts=opts.MatrixBodyOrCornerOpts(
                    data=[
                        opts.MatrixBodyDataOpts(
                            coord=[None, _yBreakTimeIndex],
                            is_coord_clamp=True,
                            is_merge_cells=True,
                            value="Break",
                            label_opts=opts.LabelOpts(font_size=16, color="#999"),
                        )
                    ],
                ),
                pos_top=30,
                pos_bottom=80,
                width="90%",
                pos_left="center",
            ),
        )
    )

    return line_chart


def each_matrix_cell(cb) -> Grid:
    grid_chart = Grid()

    for yidx, yval_item in enumerate(_matrixDimensionData["y"]):
        yval = yval_item["value"]
        if yidx == _yBreakTimeIndex:
            continue
        for xidx, xval_item in enumerate(_matrixDimensionData["x"]):
            sub_chart = cb(xval_item, yval, xidx, yidx)
            grid_chart.add(
                chart=sub_chart,
                grid_opts=opts.GridOpts(
                    coordinate_system="matrix",
                    coord=[xval_item, yval],
                    pos_top=10,
                    pos_bottom=10,
                    pos_left="center",
                    width="90%",
                    is_contain_label=True,
                ),
            )

    grid_chart.options.update(
        title=None,
        legend=None,
        dataZoom=grid_chart.options.get("dataZoom")[:2]
    )

    return grid_chart


if __name__ == "__main__":
    g = each_matrix_cell(my_callback)
    g.render("matrix_line.html")
