import asyncio

import flet as ft

class AdaptiveNavigationBarDestination(ft.NavigationBarDestination):
    def __init__(self, ios_icon, android_icon, label):
        super().__init__()
        self._ios_icon = ios_icon
        self._android_icon = android_icon
        self.label = label

    def build(self):
        # we can check for platform in build method because self.page is known
        self.icon = (
            self._ios_icon
            if self.page.platform == ft.PagePlatform.IOS
               or self.page.platform == ft.PagePlatform.MACOS
            else self._android_icon
        )

async def main(page: ft.Page):

    await asyncio.sleep(5)

    counter = ft.Text("0", size=50, data=0)

    def increment_click(e):
        counter.data += 1
        counter.value = str(counter.data)
        counter.update()

    page.adaptive = True

    """
    page.appbar = ft.AppBar(
        title=ft.Text("Floating Action Button", weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK87),
        actions=[
            ft.IconButton(ft.Icons.MENU, tooltip="Menu", icon_color=ft.Colors.BLACK87)
        ],
        bgcolor=ft.Colors.BLUE,
        center_title=True,
        color=ft.Colors.WHITE,
    )
    """

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            AdaptiveNavigationBarDestination(
                ios_icon=ft.cupertino_icons.PERSON_3_FILL,
                android_icon=ft.Icons.PERSON,
                label="Contacts",
            ),
            AdaptiveNavigationBarDestination(
                ios_icon=ft.cupertino_icons.CHAT_BUBBLE_2,
                android_icon=ft.Icons.CHAT,
                label="Chats",
            ),
            AdaptiveNavigationBarDestination(
                ios_icon=ft.cupertino_icons.SETTINGS,
                android_icon=ft.Icons.SETTINGS,
                label="Settings",
            ),
        ],
        border=ft.Border(
            top=ft.BorderSide(color=ft.CupertinoColors.SYSTEM_GREY2, width=0)
        ),
    )

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD,
        on_click=increment_click,
        tooltip="Increment",
        bgcolor=ft.Colors.BLUE,
        mini=True,
    )
    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.Container(
                        counter,
                        alignment=ft.alignment.center,
                    ),
                    ft.Checkbox(value=False, label="Dark Mode"),
                    ft.Text("First field:"),
                    ft.TextField(keyboard_type=ft.KeyboardType.TEXT),
                    ft.Text("Second field:"),
                    ft.TextField(keyboard_type=ft.KeyboardType.TEXT),
                    ft.Switch(label="A switch"),
                    ft.FilledButton(content=ft.Text("Adaptive button")),
                    ft.Text("Text line 1"),
                    ft.Text("Text line 2"),
                    ft.Text("Text line 3"),
                ]
            ),
            expand=True,
        )
    )


ft.app(main)
