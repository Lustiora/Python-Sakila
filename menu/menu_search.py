from menu.menu_search_customer import *
from menu.menu_search_inventory import *
from menu.menu_search_rental import *

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
    total_rentals, overdue, due_total, input_rental, filter_rental = build_rental_ui()
    return flet.Column(
        controls=[
            flet.Row([
                flet.Text("Rental Status Overview", style=flet.TextThemeStyle.DISPLAY_SMALL,
                          weight=flet.FontWeight.BOLD)], height=60),
            flet.Divider(),
            flet.Row([total_rentals, dummy, overdue, dummy, due_total]),
            dummy,
            flet.Row([input_rental, filter_rental], height=60),
            dummy,
            flet.Column([
                flet.Container(
                    bgcolor=flet.Colors.GREY_200,
                    # content="", # 하단 표시 컨텐츠 (기본 대여중인 목록 전체)
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
