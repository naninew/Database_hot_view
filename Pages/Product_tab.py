from nicegui import app as nicegui_app, ui
from Pages.Echart import PieChart, TimeChart, BarChart
from datetime import datetime, timedelta
import time
from Database_controller import (
    RevenueOfProduct,
    MonthlyRevenue,
    StockOfProduct,
    SoldOfProduct,
)


def Product_tab(Refresshable_Product):
    with ui.row():
        with ui.card().classes("fit").style("min-height: 700px;min-width:700px"):
            Day1 = nicegui_app.storage.user.get("Day1")
            ui.label("Số ngày thống kê:")
            Input1 = (
                ui.slider(min=0, max=1500, step=1, value=Day1).props("label-always")
            ).on(
                "update:model-value",
                lambda e: nicegui_app.storage.user.update({"Day1": e.args}),
            )
            # .on("update:model-value", lambda: Refresshable_Product.refresh())

            BarChart1 = BarChart().style("min-height: 700px")
            BarChart1.options["title"]["text"] = (
                "Số lượng sản phẩm trong kho hiện tại & số lượng đã bán trong {} ngày".format(
                    nicegui_app.storage.user.get("Day1")
                )
            )
            BarChart1.options["title"]["subtext"] = ""
            DataX, DataY1 = StockOfProduct()
            DataY2 = SoldOfProduct(
                str(
                    (
                        datetime.today()
                        - timedelta(days=int(nicegui_app.storage.user.get("Day1")))
                    ).strftime("%Y-%m-%d")
                )
            )
            if len(DataY2) < len(DataY1):
                DataY2 += [0] * (len(DataY1) - len(DataY2))
            IndexList = sorted([(DataY1[i] - DataY2[i], i) for i in range(len(DataY1))])
            # if len(IndexList) > 50:
            #     IndexList = IndexList[:50]
            DataX = [DataX[i[1]] for i in IndexList]
            DataY1 = [DataY1[i[1]] for i in IndexList]
            DataY2 = [DataY2[i[1]] for i in IndexList]
            BarChart1.options["xAxis"][0]["data"] = DataX
            BarChart1.options["series"][0]["data"] = DataY1
            BarChart1.options["series"][1]["data"] = DataY2

        with ui.card().classes("fit").style("min-height: 700px;min-width:700px"):
            # ui.label("Tỉ lệ doanh thu từng sản phẩm")
            Day2 = nicegui_app.storage.user.get("Day2")
            ui.label("Số ngày thống kê:")
            Input2 = (
                ui.slider(min=0, max=360, step=1, value=Day2).props("label-always")
            ).on(
                "update:model-value",
                lambda e: nicegui_app.storage.user.update({"Day2": e.args}),
            )
            ui.label("Số lượng data hiển thị tối đa:")
            Limit2 = (
                ui.slider(
                    min=2, max=300, step=1, value=nicegui_app.storage.user.get("Limit2")
                ).props("label-always")
            ).on(
                "update:model-value",
                lambda e: nicegui_app.storage.user.update({"Limit2": e.args}),
            )

            PieChart1 = PieChart().style("min-height: 700px")
            PieChart1.options["title"]["text"] = (
                "Tỉ lệ doanh thu từng sản phẩm theo thời gian ({}) ngày gần đây".format(
                    nicegui_app.storage.user.get("Day2")
                )
            )
            PieChart1.options["title"]["subtext"] = ""
            PieChart1.options["series"][0]["data"] = RevenueOfProduct(
                str(
                    (
                        datetime.today()
                        - timedelta(days=int(nicegui_app.storage.user.get("Day2")))
                    ).strftime("%Y-%m-%d")
                )
            )[: nicegui_app.storage.user.get("Limit2")]
        with ui.card().classes("fit").style("min-height: 700px;min-width:700px"):
            # ui.label("Doanh số từng tháng")
            Month3 = nicegui_app.storage.user.get("Month3")
            ui.label("Số tháng thống kê:")
            Input3 = (
                ui.slider(min=0, max=72, step=1, value=Month3).props("label-always")
            ).on(
                "update:model-value",
                lambda e: nicegui_app.storage.user.update({"Month3": e.args}),
            )
            TimeChart1 = TimeChart().style("min-height: 700px")
            TimeChart1.options["title"]["text"] = "Doanh thu theo thời gian"
            TimeChart1.options["title"]["subtext"] = (
                "thống kê trong {} tháng gần đây".format(
                    nicegui_app.storage.user.get("Month3")
                )
            )
            DataX, Series = MonthlyRevenue(
                str(
                    (
                        datetime.today()
                        - 30
                        * timedelta(days=int(nicegui_app.storage.user.get("Month3")))
                    ).strftime("%Y-%m-%d")
                )
            )
            TimeChart1.options["xAxis"]["data"] = DataX
            TimeChart1.options["series"] = Series


# .style("min-width: 300px")
# ui.label("Số lượng sản phẩm trong kho hiện tại")
# with ui.input("Start day") as date:
#     with ui.menu().props("no-parent-event") as menu:
#         with ui.date().bind_value(date):
#             with ui.row().classes("justify-end"):
#                 ui.button("Close", on_click=menu.close).props("flat")
#     with date.add_slot("append"):
#         ui.icon("edit_calendar").on("click", menu.open).classes(
#             "cursor-pointer"
#         )
