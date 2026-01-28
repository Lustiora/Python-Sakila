import flet
from window import Font

def search_customer(page, conn):
    def scq_id(e):
        cu_id = customer_id.value
        def close_pop(e):
            page.close(error_quit)  # 팝업창 종료 명령어
        error_quit = flet.AlertDialog(
            title=flet.Text("Customer"),
            content=flet.Text(f"Customer ID Not Found [{customer_id.value}]"),
            actions=[flet.TextButton("OK", on_click=close_pop)
                     ], actions_alignment=flet.MainAxisAlignment.END)
        cursor = conn.cursor()
        try:
            cursor.execute(
                """ select 
                        c.customer_id , 
                        c.create_date  , 
                        c.first_name , 
                        c.last_name , 
                        c.email ,
                        a.address
                    from customer c 
                    inner join address a 
                        on c.address_id = a.address_id
                    where c.activebool is true
                        and c.customer_id = %s""",(cu_id,)
            )
            customer_data = cursor.fetchone()
            if customer_data:
                sc_id.rows.clear()
                sc_id.rows.append(
                    flet.DataRow(cells=[
                        flet.DataCell(flet.Text(customer_data[0])),
                        flet.DataCell(flet.Text(customer_data[1])),
                        flet.DataCell(flet.Text(customer_data[2])),
                        flet.DataCell(flet.Text(customer_data[3])),
                        flet.DataCell(flet.Text(customer_data[4])),
                        flet.DataCell(flet.Text(customer_data[5])),
                    ])
                )
                sc_id.update()
            else:
                page.open(error_quit)
        except Exception as err:
            print(f"Search Customer error : {err}")
    customer_id = flet.TextField(width=150, height=30, content_padding=10, max_length=10, autofocus=True)
    search_id = flet.Button(
        "Search", on_click=scq_id, width=80, style=flet.ButtonStyle(shape=(flet.RoundedRectangleBorder(radius=5))))
    sc_id = flet.DataTable(
        columns=[
            flet.DataColumn(flet.Text("ID")),
            flet.DataColumn(flet.Text("Create Date")),
            flet.DataColumn(flet.Text("First Name")),
            flet.DataColumn(flet.Text("Last Name")),
            flet.DataColumn(flet.Text("Email",width=240)),
            flet.DataColumn(flet.Text("Address",width=160)),
        ],
        rows=[],
        border=flet.border.all(1, "flet.Colors.BLUE_GREY_100"), # DataTable Titlebar
        vertical_lines=flet.border.all(1, "flet.Colors.BLUE_GREY_100"), # DataTable Titlebar
        horizontal_lines=flet.border.all(1, "flet.Colors.BLUE_GREY_100"), # DataTable Titlebar
        heading_row_color=flet.Colors.GREY_300, # DataTable Titlebar Inside Color
        heading_row_height=Font.height+4, # DataTable Titlebar Height
        data_row_min_height=Font.height, # DataTable Data Min Height
        data_row_max_height=Font.height, # DataTable Data Max Height
    )
    s_c_id = flet.Column(
        controls=[
            flet.Row([sc_id], scroll=flet.ScrollMode.ALWAYS)
        ],scroll=flet.ScrollMode.AUTO,
        expand=True,
    )

    def scq_firstname(e):
        cu_name = f"%{customer_name.value}%"
        def close_pop(e):
            page.close(error_quit)  # 팝업창 종료 명령어
        error_quit = flet.AlertDialog(
            title=flet.Text("Customer"),
            content=flet.Text(f"Customer Name Not Found [{customer_name.value}]"),
            actions=[flet.TextButton("OK", on_click=close_pop)
                     ], actions_alignment=flet.MainAxisAlignment.END)
        cursor = conn.cursor()
        try:
            cursor.execute(
                """ select 
                        c.customer_id , 
                        c.create_date  , 
                        c.first_name , 
                        c.last_name , 
                        c.email ,
                        a.address
                    from customer c 
                    inner join address a 
                        on c.address_id = a.address_id
                    where c.activebool is true
                        and c.first_name like %s
                        or c.last_name like %s""",(cu_name,cu_name,)
            )
            customer_data = cursor.fetchall()
            if customer_data:
                sc_name.rows.clear()
                print(customer_data)
                for sc_row in customer_data:
                    sc_name.rows.append(
                        flet.DataRow(cells=[
                            flet.DataCell(flet.Text(sc_row[0])),
                            flet.DataCell(flet.Text(sc_row[1])),
                            flet.DataCell(flet.Text(sc_row[2])),
                            flet.DataCell(flet.Text(sc_row[3])),
                            flet.DataCell(flet.Text(sc_row[4])),
                            flet.DataCell(flet.Text(sc_row[5])),
                        ])
                    )
                sc_name.update()
            else:
                page.open(error_quit)
        except Exception as err:
            print(f"Search Customer error : {err}")
    customer_name = flet.TextField(width=150, height=30, content_padding=10, max_length=10, autofocus=True)
    search_name = flet.Button("Search", on_click=scq_firstname, width=80, style=flet.ButtonStyle(shape=(flet.RoundedRectangleBorder(radius=5))))
    sc_name = flet.DataTable(
        columns=[
            flet.DataColumn(flet.Text("ID")),
            flet.DataColumn(flet.Text("Create Date")),
            flet.DataColumn(flet.Text("First Name")),
            flet.DataColumn(flet.Text("Last Name")),
            flet.DataColumn(flet.Text("Email",width=240)),
            flet.DataColumn(flet.Text("Address",width=160)),
        ],
        rows=[],
        border=flet.border.all(1, "flet.Colors.BLUE_GREY_100"), # DataTable Titlebar
        vertical_lines=flet.border.all(1, "flet.Colors.BLUE_GREY_100"), # DataTable Titlebar
        horizontal_lines=flet.border.all(1, "flet.Colors.BLUE_GREY_100"), # DataTable Titlebar
        heading_row_color=flet.Colors.GREY_300, # DataTable Titlebar Inside Color
        heading_row_height=Font.height+4, # DataTable Titlebar Height
        data_row_min_height=Font.height, # DataTable Data Min Height
        data_row_max_height=Font.height, # DataTable Data Max Height
    )
    s_c_name = flet.Column(
        controls=[flet.Row([sc_name], scroll=flet.ScrollMode.ALWAYS)],
        scroll=flet.ScrollMode.AUTO,
        expand=True,
    )
    return flet.Column(
        controls=[
            flet.Row([
                flet.Text("Customer Lookup", style=flet.TextThemeStyle.DISPLAY_MEDIUM, italic=True)
            ], height=80),
            flet.Divider(),
            flet.Row([
                flet.Text("Customer ID :", style=flet.TextThemeStyle.BODY_LARGE),
                customer_id,
                search_id
            ], height=30),
            flet.Divider(),
            flet.Column([
                flet.Container(
                    bgcolor=flet.Colors.GREY_200,
                    content=s_c_id,
                    height=65,
                    padding=10,
                    border_radius=5,
                    border=flet.border.all(1, "flet.Colors.BLUE_GREY_50"),
                )
            ], alignment=flet.alignment.center),
            flet.Divider(),
            flet.Row([
                flet.Text("Name :", style=flet.TextThemeStyle.BODY_LARGE),
                customer_name,
                search_name
            ], height=30),
            flet.Divider(),
            flet.Column([
                flet.Container(
                    bgcolor=flet.Colors.GREY_200,
                    content=s_c_name,
                    expand=True,
                    padding=10,
                    border_radius=5,
                    border=flet.border.all(1, "flet.Colors.BLUE_GREY_50"),
                )
            ], expand=True, alignment=flet.alignment.center),
        ]
    )

def search_inventory():
    inventory = flet.TextField(width=150, height=30, content_padding=10, max_length=10, autofocus=True)
    search = flet.Button("Search", on_click="", width=80,
                        style=flet.ButtonStyle(shape=(flet.RoundedRectangleBorder(radius=5))))
    return flet.Column(
        controls=[
            flet.Row([
                flet.Text("Inventory Search", style=flet.TextThemeStyle.DISPLAY_MEDIUM, italic=True)
            ], height=80),
            flet.Divider(),
            flet.Row([
                flet.Text("Inventory :", style=flet.TextThemeStyle.BODY_LARGE),
                inventory,
                search
            ], height=30),
        ]
    )

def search_film():
    film = flet.TextField(width=150, height=30, content_padding=10, max_length=10, autofocus=True)
    search = flet.Button("Search", on_click="", width=80,
                        style=flet.ButtonStyle(shape=(flet.RoundedRectangleBorder(radius=5))))
    return flet.Column(
        controls=[
            flet.Row([
                flet.Text("Film Catalog Search", style=flet.TextThemeStyle.DISPLAY_MEDIUM, italic=True)
            ], height=80),
            flet.Divider(),
            flet.Row([
                flet.Text("Film :", style=flet.TextThemeStyle.BODY_LARGE),
                film,
                search
            ], height=30),
        ]
    )

def search_rental():
    rental = flet.TextField(width=150, height=30, content_padding=10, max_length=10, autofocus=True)
    search = flet.Button("Search", on_click="", width=80,
                        style=flet.ButtonStyle(shape=(flet.RoundedRectangleBorder(radius=5))))
    return flet.Column(
        controls=[
            flet.Row([
                flet.Text("Rental Status Lookup", style=flet.TextThemeStyle.DISPLAY_MEDIUM, italic=True)
            ], height=80),
            flet.Divider(),
            flet.Row([
                flet.Text("Rental :", style=flet.TextThemeStyle.BODY_LARGE),
                rental,
                search
            ], height=30),
        ]
    )

def search_payment():
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
                flet.Text("Payment :", style=flet.TextThemeStyle.BODY_LARGE),
                payment,
                search
            ], height=30),
        ]
    )
