import flet
from window import Font, Ratios

def build_rental_ui():
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
        hint_text="Press Enter to Search", on_submit="", label=" Rental ID or Customer Name ↵",
        text_size=Font.big_fontsize, expand=Ratios.id, content_padding=10, max_length=30)
    filter_rental = flet.Column(
        controls=[
            flet.Dropdown(
                label="Filter",
                bgcolor=flet.Colors.PRIMARY_CONTAINER,
                options=[
                    flet.DropdownOption("Total Rentals"),
                    flet.DropdownOption("Overdue"),
                    flet.DropdownOption("Due Today"),
                ]
            )
        ],alignment=flet.MainAxisAlignment.CENTER)
    return total_rentals, overdue, due_total, input_rental, filter_rental