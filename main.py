from nicegui import app as nicegui_app, ui
from Pages.Manager_page import Manager_page


@ui.page("/")
async def manager():
    Manager_page()


if __name__ in {"__main__", "__mp_main__"}:
    ui.run(storage_secret="THIS_NEEDS_TO_BE_CHANGED")
