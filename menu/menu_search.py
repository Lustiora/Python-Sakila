import flet
from flet.core.types import CrossAxisAlignment, MainAxisAlignment

from menu.menu_search_customer import *
from menu.menu_search_inventory import *
from menu.menu_search_film import *

def view_search_customer(page, store_id, conn):
    input_customer, view_customer = build_customer_ui(page, store_id, conn) # Module Return Value get
    return flet.Column(
        controls=[
            flet.Row([
                flet.Text("Customer Lookup", style=flet.TextThemeStyle.DISPLAY_MEDIUM, italic=True)
            ], height=80),
            flet.Divider(),
            flet.Row([input_customer], height=60),
            flet.Divider(),
            flet.Column([
                flet.Container(
                    bgcolor=flet.Colors.GREY_200,
                    alignment=flet.alignment.top_left,
                    expand=True,
                    content=view_customer,
                    padding=10,
                    border_radius=5,
                    border=flet.border.all(1, "flet.Colors.BLUE_GREY_50"),
                )
            ], alignment=flet.alignment.center, expand=True),
        ]
    )

def view_search_inventory(page, store_id, conn):
    input_inventory, view_inventory = build_inventory_ui(page, store_id, conn)  # Module Return Value get
    return flet.Column(
        controls=[
            flet.Row([
                flet.Text("Inventory Search", style=flet.TextThemeStyle.DISPLAY_MEDIUM, italic=True)
            ], height=80),
            flet.Divider(),
            flet.Row([input_inventory,], height=60),
            flet.Divider(),
            flet.Column([
                flet.Container(
                    bgcolor=flet.Colors.GREY_200,
                    content=view_inventory,
                    alignment=flet.alignment.top_left,
                    expand=True,
                    padding=10,
                    border_radius=5,
                    border=flet.border.all(1, "flet.Colors.BLUE_GREY_50"),
                )
            ], alignment=flet.alignment.center, expand=True),
        ]
    )

def view_search_rental():
    dummy = flet.Container()
    total_rentals = flet.Container(
        bgcolor=flet.Colors.GREY_200,
        expand=1,
        padding=10,
        border_radius=10,
        height=80,
        alignment=flet.alignment.center_left,
        border=flet.border.all(1, "flet.Colors.BLUE_GREY_50"),
        content=flet.Column([
            flet.Text("Total Rentals:", style=flet.TextThemeStyle.TITLE_MEDIUM),
            flet.Text("대여중인 재고", style=flet.TextThemeStyle.HEADLINE_SMALL, weight=flet.FontWeight.BOLD)
        ], spacing=1)
    )
    overdue = flet.Container(
        bgcolor=flet.Colors.GREY_200,
        expand=1,
        padding=10,
        border_radius=10,
        height=80,
        alignment=flet.alignment.center_left,
        border=flet.border.all(1, "flet.Colors.BLUE_GREY_50"),
        content=flet.Column([
            flet.Text("Overdue:", style=flet.TextThemeStyle.TITLE_MEDIUM, color=flet.Colors.ERROR),
            flet.Text("연체중인 재고", style=flet.TextThemeStyle.HEADLINE_SMALL, weight=flet.FontWeight.BOLD, color=flet.Colors.ERROR)
        ], spacing=1)
    )
    due_total = flet.Container(
        bgcolor=flet.Colors.GREY_200,
        expand=1,
        padding=10,
        border_radius=10,
        height=80,
        alignment=flet.alignment.center_left,
        border=flet.border.all(1, "flet.Colors.BLUE_GREY_50"),
        content=flet.Column([
            flet.Text("Due Today:", style=flet.TextThemeStyle.TITLE_MEDIUM),
            flet.Text("금일 반납예정인 재고", style=flet.TextThemeStyle.HEADLINE_SMALL, weight=flet.FontWeight.BOLD)
        ], spacing=1)
    )
    input_rental = flet.TextField(
        hint_text=" Rental ID or Customer Name ↵", on_submit="", label="Press Enter to Search",
        text_size=Font.big_fontsize, expand=Ratios.id, content_padding=10, max_length=30)
    filter_rental = flet.Column(
        controls=[
            flet.Dropdown(
                label="Filter",
                bgcolor=flet.Colors.GREY_200,
                options=[
                    flet.DropdownOption("Red"),
                    flet.DropdownOption("Blue"),
                    flet.DropdownOption("Green"),
                ]
            )
        ],alignment=MainAxisAlignment.CENTER
    )
    return flet.Column(
        controls=[
            flet.Row([
                flet.Text("Rental Status Overview", style=flet.TextThemeStyle.DISPLAY_SMALL,
                          weight=flet.FontWeight.BOLD)], height=60),
            flet.Row([total_rentals, dummy, overdue, dummy, due_total]),
            dummy,
            flet.Row([input_rental, filter_rental], height=60),
            dummy,
            flet.Column([
                flet.Container(
                    bgcolor=flet.Colors.GREY_200,
                    # content=view_inventory,
                    alignment=flet.alignment.top_left,
                    expand=True,
                    padding=10,
                    border_radius=5,
                    border=flet.border.all(1, "flet.Colors.BLUE_GREY_50"),
                )
            ], alignment=flet.alignment.center, expand=True),
        ]
    )

def view_search_payment():
    payment = flet.TextField(width=150, height=30, content_padding=10, max_length=10, autofocus=True)
    search = flet.Button("Search", on_click="", width=80,
                        style=flet.ButtonStyle(shape=(flet.RoundedRectangleBorder(radius=5))))
    return flet.Column(
        controls=[
            flet.Row([
                flet.Text("Payment History Search", style=flet.TextThemeStyle.DISPLAY_MEDIUM, italic=True)
            ], height=80),
            flet.Divider(),
            flet.Row([
                flet.Text("ID :", style=flet.TextThemeStyle.BODY_LARGE, width=100, text_align="right"),
                payment,
                search
            ], height=30),
        ]
    )
