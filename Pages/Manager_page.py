from nicegui import app as nicegui_app, ui
from Pages.Product_tab import Product_tab
from Pages.Order_tab import Order_tab


def AutoRefresh(Timer):
    Timer.active = not Timer.active


def Manager_page():
    @ui.refreshable
    def Refresshable_Product():
        Product_tab(Refresshable_Product)

    nicegui_app.storage.user.update({"Day1": 30, "Day2": 30, "Month3": 6, "Limit2": 30})
    dark_mode = ui.dark_mode()
    with ui.header().classes(replace="row items-center") as header:
        ui.button(on_click=lambda: left_drawer.toggle(), icon="menu").props(
            "flat color=white"
        )
        with ui.tabs() as tabs:
            ui.tab("Product")
            ui.tab("Order")
    with ui.left_drawer().classes("border w-48") as left_drawer:
        ui.menu_item("Light Mode", on_click=dark_mode.disable)
        ui.menu_item("Dark Mode", on_click=dark_mode.enable)
        ui.menu_item("Toggle auto refresh", on_click=lambda: AutoRefresh(Timer))

    @ui.refreshable
    def Refresshable_Order():
        Order_tab()

    with ui.tab_panels(tabs, value="Product").classes("w-full"):
        with ui.tab_panel("Product"):
            Refresshable_Product()
        with ui.tab_panel("Order"):
            Refresshable_Order()
    Timer = ui.timer(3, Refresshable_Product.refresh)
