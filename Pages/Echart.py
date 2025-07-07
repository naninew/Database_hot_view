from nicegui import app as nicegui_app, ui


def PieChart():
    return ui.echart(
        {
            "title": {
                "text": "Referer of a Website",
                "subtext": "Fake Data",
                "left": "center",
            },
            "tooltip": {"trigger": "item"},
            "legend": {
                "orient": "vertical",
                # "left": "left",
                "type": "scroll",
                "right": 0,
                "top": 50,
                "bottom": 20,
            },
            "series": [
                {
                    "name": "Access From",
                    "type": "pie",
                    "radius": "70%",
                    "data": [
                        {"value": 1048, "name": "Search Engine"},
                        {"value": 735, "name": "Direct"},
                        {"value": 580, "name": "Email"},
                        {"value": 484, "name": "Union Ads"},
                        {"value": 300, "name": "Video Ads"},
                    ],
                    "emphasis": {
                        "itemStyle": {
                            "shadowBlur": 10,
                            "shadowOffsetX": 0,
                            "shadowColor": "rgba(0, 0, 0, 0.5)",
                        }
                    },
                }
            ],
            "textStyle": {"fontFamily": "consolas"},
            "toolbox": {
                "feature": {
                    "dataZoom": {"yAxisIndex": "none"},
                    "restore": {},
                    "saveAsImage": {},
                }
            },
            "axisPointer": {"link": [{"xAxisIndex": "all"}]},
            "dataZoom": [
                {
                    "show": "true",
                    "realtime": "true",
                    "start": 0,
                    "end": 100,
                    "xAxisIndex": [0, 1],
                },
                {
                    "type": "inside",
                    "realtime": "true",
                    "start": 0,
                    "end": 100,
                    "xAxisIndex": [0, 1],
                },
            ],
        }
    )


def TimeChart():
    return ui.echart(
        {
            "title": {
                "text": "Referer of a Website",
                "subtext": "Fake Data",
                "left": "center",
            },
            "legend": {
                "data": [
                    "ATX Jeans",
                    "NEU Jacket",
                    "HUCE T Shirt",
                    "UEB Shoes",
                    "FTU Jacket",
                    "HUST Shirt",
                ],
                "orient": "vertical",
                # "left": "left",
                "type": "scroll",
                "right": 0,
                "top": 50,
                "bottom": 20,
            },
            "xAxis": {
                "type": "category",
                "boundaryGap": "false",
                "data": ["2025-1", "2025-2", "2025-3", "2025-4", "2025-5", "2025-6"],
                "axisLabel": {"interval": 0, "rotate": 30},
            },
            "yAxis": {"type": "value"},
            "series": [
                {
                    "name": "ATX Jeans",
                    "data": [3500000, 4500000, 4500000, 3750000, 4000000, 2500000],
                    "type": "line",
                    "stack": "Total",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    # "smooth": "true",
                },
                {
                    "name": "NEU Jacket",
                    "data": [3500000, 4500000, 4500000, 3750000, 4000000, 2500000],
                    "type": "line",
                    "stack": "Total",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    # "smooth": "true",
                },
                {
                    "name": "HUCE T Shirt",
                    "data": [3500000, 4500000, 4500000, 3750000, 4000000, 2500000],
                    "type": "line",
                    "stack": "Total",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    # "smooth": "true",
                },
                {
                    "name": "UEB Shoes",
                    "data": [3500000, 4500000, 4500000, 3750000, 4000000, 2500000],
                    "type": "line",
                    "stack": "Total",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    # "smooth": "true",
                },
                {
                    "name": "FTU Jacket",
                    "data": [3500000, 4500000, 4500000, 3750000, 4000000, 2500000],
                    "type": "line",
                    "stack": "Total",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    # "smooth": "true",
                },
                {
                    "name": "HUST Shirt",
                    "data": [3500000, 4500000, 4500000, 3750000, 4000000, 2500000],
                    "type": "line",
                    "stack": "Total",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    # "smooth": "true",
                },
            ],
            "textStyle": {"fontFamily": "consolas"},
            "tooltip": {
                "trigger": "axis",
                "axisPointer": {
                    "type": "cross",  # cross
                    "label": {"backgroundColor": "#6a7985"},
                },
            },
            "grid": {
                "left": "3%",
                "right": "4%",
                "bottom": "3%",
                "containLabel": "true",
            },
            "toolbox": {
                "feature": {
                    "dataZoom": {"yAxisIndex": "none"},
                    "restore": {},
                    "saveAsImage": {},
                }
            },
            "axisPointer": {"link": [{"xAxisIndex": "all"}]},
            "dataZoom": [
                {
                    "show": "true",
                    "realtime": "true",
                    "start": 0,
                    "end": 100,
                    "xAxisIndex": [0, 1],
                },
                {
                    "type": "inside",
                    "realtime": "true",
                    "start": 0,
                    "end": 100,
                    "xAxisIndex": [0, 1],
                },
            ],
        }
    )


def BarChart():
    return ui.echart(
        {
            "title": {
                "text": "Referer of a Website",
                "subtext": "Fake Data",
                "left": "center",
            },
            "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
            "grid": {
                "left": "3%",
                "right": "4%",
                "bottom": "3%",
                "containLabel": "true",
            },
            "legend": {
                "data": ["Hiện tại", "Đã bán"],
                "orient": "vertical",
                # "left": "left",
                "type": "scroll",
                "right": 0,
                "top": 50,
                "bottom": 20,
            },
            "xAxis": [
                {
                    "type": "category",
                    "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
                    "axisTick": {"alignWithLabel": "true"},
                    "axisLabel": {"interval": 0, "rotate": 60},
                }
            ],
            "yAxis": [{"type": "value"}],
            "series": [
                {
                    "name": "Hiện tại",
                    "type": "bar",
                    "barWidth": "20%",
                    "data": [10, 52, 200, 334, 390, 330, 220],
                },
                {
                    "name": "Đã bán",
                    "type": "bar",
                    "barWidth": "20%",
                    "data": [
                        10,
                        8,
                        4,
                        5,
                        8,
                        6,
                    ],
                },
            ],
            "textStyle": {"fontFamily": "consolas"},
            "toolbox": {
                "feature": {
                    "dataZoom": {"yAxisIndex": "none"},
                    "restore": {},
                    "saveAsImage": {},
                }
            },
            "axisPointer": {"link": [{"xAxisIndex": "all"}]},
            "dataZoom": [
                {
                    "show": "true",
                    "realtime": "true",
                    "start": 0,
                    "end": 1,
                    "xAxisIndex": [0, 1],
                },
                {
                    "type": "inside",
                    "realtime": "true",
                    "start": 0,
                    "end": 1,
                    "xAxisIndex": [0, 1],
                },
            ],
        }
    )
