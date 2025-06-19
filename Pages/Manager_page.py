from nicegui import app as nicegui_app, ui
from Pages.Product_tab import Product_tab
from Pages.Order_tab import Order_tab


def Manager_page():
    nicegui_app.storage.user.update({"Day1": 7, "Day2": 30, "Month3": 6})
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

    @ui.refreshable
    def Refresshable_Product():
        Product_tab(Refresshable_Product)

    @ui.refreshable
    def Refresshable_Order():
        Order_tab()

    with ui.tab_panels(tabs, value="Product").classes("w-full"):
        with ui.tab_panel("Product"):
            Refresshable_Product()
        with ui.tab_panel("Order"):
            Refresshable_Order()
    ui.timer(10, Refresshable_Product.refresh)
