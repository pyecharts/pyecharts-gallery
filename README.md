<h1 align="center">pyecharts-gallery</h1>

---

* [English Introduction is Here](https://github.com/pyecharts/pyecharts-gallery/blob/master/README_EN.md)

---

## 项目简介

* 项目基于 pyecharts 1.3.1 版本进行展示
* 百度官方 Echarts [官方实例](https://echarts.baidu.com/examples/)

## 项目须知

* 项目代码结构按照 Echarts 官网的实例模块进行划分
* 代码内有根据 1.3.1 版本的 pyecharts 所生成的可视化数据视图和官方的进行对比, 有列出能实现的功能以及未实现的功能
* 以下图例多数会基于 Echarts 的官方实例，不过也有部分会基于 Echarts 的社区 Gallery 实现

## 目前进度

* 折线图 Line
    * [Basic Line Chart](https://echarts.baidu.com/examples/editor.html?c=line-simple) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Line/basic_line_chart.py) -- pyecharts 版本 1.3.1 测试通过
    * [Basic Area Chart](https://echarts.baidu.com/examples/editor.html?c=area-basic) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Line/basic_area_chart.py) -- pyecharts 版本 1.3.1 测试通过
    * [Smoothed Line Chart](https://echarts.baidu.com/examples/editor.html?c=line-smooth) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Line/smoothed_line_chart.py) -- pyecharts 版本 1.3.1 测试通过
    * [Stacked Area Chart](https://echarts.baidu.com/examples/editor.html?c=area-stack) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Line/stacked_area_chart.py) -- pyecharts 版本 1.3.1 测试通过
    * [Stacked Line Chart](https://echarts.baidu.com/examples/editor.html?c=line-stack) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Line/stacked_line_chart.py) -- pyecharts 版本 1.3.1 测试通过
    * [Rainfall](https://echarts.baidu.com/examples/editor.html?c=area-rainfall) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Line/rainfall.py) -- pyecharts 版本 1.3.1 测试通过
    * [Beijing AQI](https://echarts.baidu.com/examples/editor.html?c=line-aqi) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Line/beijing_aqi.py) -- pyecharts 版本 1.3.1 测试通过
    * [Log Axis](https://www.echartsjs.com/examples/editor.html?c=line-log) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Line/log_axis.py) -- pyecharts 版本 1.3.1 测试通过
    * [Temperature Change In The Coming Week](https://echarts.baidu.com/examples/editor.html?c=line-marker) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Line/temperature_change_line_chart.py) -- pyecharts 版本 1.3.1 测试通过
    * [Distribution of Electricity](https://www.echartsjs.com/examples/editor.html?c=line-sections) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Line/distribution_of_electricity.py) -- pyecharts 版本 1.3.1 测试通过
    * [Line Style and Item Style](https://echarts.baidu.com/examples/editor.html?c=line-style) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Line/line_style_and_item_style.py) -- pyecharts 版本 1.3.1 测试通过
    * [Multiple X Axes](https://echarts.baidu.com/examples/editor.html?c=multiple-x-axis) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Line/multiple_x_axes.py) -- pyecharts 版本 1.3.1 测试通过

* 极坐标 Polar
    * [Two Value-Axes in Polar](https://www.echartsjs.com/examples/editor.html?c=line-polar) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Polar/two_value_axes_in_polar.py) -- pyecharts 版本 1.3.1 测试通过
    * [Two Value-Axes in Polar 2](https://www.echartsjs.com/examples/editor.html?c=line-polar2) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Polar/two_value_axes_in_polar_2.py) -- pyecharts 版本 1.3.1 测试通过
    
* 柱状图 Bar
    * [Bar Chart Display Delay](https://echarts.baidu.com/examples/editor.html?c=bar-animation-delay) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Bar/bar_chart_display_delay.py) -- pyecharts 版本 1.3.1 测试通过
    * [Mixed Line and Bar](https://echarts.baidu.com/examples/editor.html?c=mix-line-bar) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Bar/mixed_bar_and_line.py) -- pyecharts 版本 1.3.1 测试通过
    * [Multiple Y Axes](https://www.echartsjs.com/examples/editor.html?c=multiple-y-axis) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Bar/multiple_y_axes.py) -- pyecharts 版本 1.3.1 测试通过
    * [Finance Indices 2002](https://www.echartsjs.com/examples/editor.html?c=mix-timeline-finance) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Bar/finance_indices_2002.py) -- pyecharts 版本 1.3.1 测试通过

* 饼图 Pie
    * [Customized Pie](https://echarts.baidu.com/examples/editor.html?c=pie-custom) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Pie/customized_pie.py) -- pyecharts 版本 1.3.1 测试通过
    * [Doughnut Chart](https://echarts.baidu.com/examples/editor.html?c=pie-doughnut) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Pie/doughnut_chart.py) -- pyecharts 版本 1.3.1 测试通过
    * [Nested Pies](https://echarts.baidu.com/examples/editor.html?c=pie-nest) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Pie/nested_pies.py) -- pyecharts 版本 1.3.1 测试通过

* 散点图 Scatter
    * [Basic Scatter Chart](https://echarts.baidu.com/examples/editor.html?c=scatter-simple) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Scatter/basic_scatter_chart.py) -- pyecharts 版本 1.3.1 测试通过

* 地理坐标/地图/百度地图 GEO / Map / BMap
    * [Population Density of HongKong](https://echarts.baidu.com/examples/editor.html?c=map-HK) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Geo_Map_BMap/population_density_of_HongKong.py) -- pyecharts 版本 1.3.1 测试通过。
    * [Population Density of HongKong Version 2](https://echarts.baidu.com/examples/editor.html?c=map-HK) -- [实现的代码2](https://github.com/pyecharts/pyecharts-gallery/blob/master/Geo_Map_BMap/population_density_of_HongKong_v2.py) -- pyecharts 版本 1.3.1 + [echarts-china-cities-js](https://github.com/echarts-map/echarts-china-cities-js)
    * [BMap of hiking train in HangZhou](https://echarts.baidu.com/examples/editor.html?c=lines-bmap) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Geo_Map_BMap/hiking_trail_in_hangzhou.py) -- pyecharts 版本 1.3.1 测试通过
    * [China GDP FROM 1980](https://gallery.echartsjs.com/editor.html?c=xSkGI6zLmb) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Geo_Map_BMap/china_gdp_from_1980.py) -- pyecharts 版本 1.3.1 测试通过

* K 线图 Candlestick
    * [Basic Candlestick](https://echarts.baidu.com/examples/editor.html?c=candlestick-simple) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Candlestick/basic_candlestick.py) -- pyecharts 版本 1.3.1 测试通过
    * [Professional Candlestick](https://gallery.echartsjs.com/editor.html?c=xByOFPcjBe) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Candlestick/professional_kline_chart.py) -- pyecharts 版本 1.3.1 测试通过

* 雷达图 Radar
    * [Basic Radar Chart](https://echarts.baidu.com/examples/editor.html?c=radar) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Radar/basic_radar_chart.py) -- pyecharts 版本 1.3.1 测试通过

* 盒须图 Boxplot
    * [Boxplot Light Velocity](https://echarts.baidu.com/examples/editor.html?c=boxplot-light-velocity) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Boxplot/boxplot_light_velocity.py) -- pyecharts 版本 1.3.1 测试通过
    * [Multiple Categories](https://www.echartsjs.com/examples/editor.html?c=boxplot-multi) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Boxplot/multiple_categories.py) -- pyecharts 版本 1.3.1 测试通过

* 热力图 Heatmap
    * [HeatMap on Cartesian](https://echarts.baidu.com/examples/editor.html?c=heatmap-cartesian) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Heatmap/heatmap_on_cartesian.py) -- pyecharts 版本 1.3.1 测试通过
    
* 关系图 Graph
    * [NPM Dependencies](https://echarts.baidu.com/examples/editor.html?c=graph-npm) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Graph/npm_dependencies.py) -- pyecharts 版本 1.3.1 测试通过
    
* 树图 Tree
    * [Radial Tree](https://echarts.baidu.com/examples/editor.html?c=tree-radial) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Tree/radial_tree.py) -- pyecharts 版本 1.3.1 测试通过

* 矩形树图 Treemap
    * [Echarts Option Query](https://echarts.baidu.com/examples/editor.html?c=treemap-drill-down) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Treemap/echarts_option_query.py) -- pyecharts 版本 1.3.1 测试通过
    
* 旭日图 Sunburst
    * [Basic Sunburst](https://www.echartsjs.com/examples/editor.html?c=sunburst-simple) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Sunburst/basic_sunburst.py) -- pyecharts 版本 1.3.1 测试通过
    * [Drink Flavors](https://www.echartsjs.com/examples/editor.html?c=sunburst-simple) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Sunburst/drink_flavors.py) -- pyecharts 版本 1.3.1 测试通过

* 平行坐标系 Parallel
    * [Basic Parallel](https://echarts.baidu.com/examples/editor.html?c=parallel-simple) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Parallel/basic_parallel.py) -- pyecharts 版本 1.3.1 测试通过

* 桑基图 Sankey
    * [Sankey Diagram](https://echarts.baidu.com/examples/editor.html?c=sankey-energy) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Sankey/sankey_diagram.py) -- pyecharts 版本 1.3.1 测试通过

* 漏斗图 Funnel
    * [Funnel Chart](https://echarts.baidu.com/examples/editor.html?c=funnel) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Funnel/funnel_chart.py) -- pyecharts 版本 1.3.1 测试通过

* 仪表盘 Gauge
    * [Gauge](https://echarts.baidu.com/examples/editor.html?c=gauge) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Gauge/gauge.py) -- pyecharts 版本 1.3.1 测试通过
    * [Gauge Change Color](https://gallery.echartsjs.com/editor.html?c=xH1vxib94f) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Gauge/gauge_change_color.py) -- pyecharts 版本 1.3.1 测试通过
    
* 主题河流图 ThemeRiver
    * [ThemeRiver](https://echarts.baidu.com/examples/editor.html?c=themeRiver-basic) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/ThemeRiver/theme_river.py) -- pyecharts 版本 1.3.1 测试通过

* 日历坐标系 Calendar
    * [Calendar Heatmap](https://echarts.baidu.com/examples/editor.html?c=calendar-heatmap) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Calendar/calendar_heatmap.py) -- pyecharts 版本 1.3.1 测试通过

* 3D 柱状图 3D Bar
    * [Bar3D - Punch Card](https://echarts.baidu.com/examples/editor.html?c=bar3d-punch-card&gl=1) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Bar3D/bar3d_punch_card.py) -- pyecharts 版本 1.3.1 测试通过

* 3D 散点图 3D Scatter
    * [Scatter3D](https://echarts.baidu.com/examples/editor.html?c=scatter3d&gl=1&theme=dark) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Scatter3D/scatter3d.py) -- pyecharts 版本 1.3.1 测试通过

* 3D 曲面 3D Surface
    * [Surface Wave](https://echarts.baidu.com/examples/editor.html?c=surface-wave&gl=1) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Surface3D/surface_wave.py) -- pyecharts 版本 1.3.1 测试通过

* 3D 折线图 3D Line
    * [三维折线图正交投影](https://echarts.baidu.com/examples/editor.html?c=line3d-orthographic&gl=1) -- [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/Line3D/line3d_rectangular_projection.py) -- pyecharts 版本 1.3.1 测试通过

* 词云
    * [实现的代码](https://github.com/pyecharts/pyecharts-gallery/blob/master/WordCloud/basic_wordcloud.py) -- pyecharts 版本 1.3.1 测试通过