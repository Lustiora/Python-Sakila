import flet
from window import Font

def build_customer_id_ui(page, store_id, conn):
    total_width = page.width * 0.5 - 40
    total_width10 = total_width * 0.1
    total_width15 = total_width * 0.15
    total_width20 = total_width * 0.2
    def query_customer_by_id(e):
        int_customer_id = int(customer_id_text.value)
        def close_pop(e):
            page.close(error_quit)  # 팝업창 종료 명령어
        error_quit = flet.AlertDialog(
            title=flet.Text("Customer"),
            content=flet.Text(f"Customer ID Not Found [{customer_id_text.value}]"),
            actions=[flet.TextButton("OK", on_click=close_pop)
                     ], actions_alignment=flet.MainAxisAlignment.END)
        cursor = conn.cursor()
        try:
            cursor.execute(
                """ select 
                        case when c.store_id = 1 then '🇨🇦 Lethbridge' else '🇦🇺 Woodridge' end as store ,
                        c.customer_id , 
                        c.first_name || ' ' || c.last_name as name, 
                        c.email, 
                        a.address, 
                        c.create_date ,
                        case when n.customer_id is not null then 'Overdue' else 'Normal' end as status ,
                        c.store_id
                    from customer c
                    inner join address a 
                        on c.address_id = a.address_id
                    left join not_return_customer n 
                        on n.customer_id = c.customer_id
                    where c.activebool is true
                        and c.customer_id = %s""",(int_customer_id,)
            )
            customer_data = cursor.fetchone()
            if customer_data:
                status_color = flet.Colors.BLACK
                store_color = flet.Colors.BLACK
                if customer_data[6] == 'Overdue':
                    status_color = flet.Colors.RED_ACCENT
                if customer_data[7] == store_id:
                    if customer_data[0] == '🇦🇺 Woodridge':
                        store_color = flet.Colors.ORANGE
                    if customer_data[0] == '🇨🇦 Lethbridge':
                        store_color = flet.Colors.BLUE
                else:
                    store_color = flet.Colors.RED_ACCENT
                customer_id_data.rows.clear()
                customer_id_data.rows.append(
                    flet.DataRow(cells=[
                        flet.DataCell(flet.Text(
                            customer_data[0], tooltip=customer_data[0],
                            width=total_width10, no_wrap=True, overflow=flet.TextOverflow.ELLIPSIS, color=store_color)),
                        flet.DataCell(flet.Text(
                            customer_data[1], tooltip=str(customer_data[1]), # customer_data[1] 값=int 형변환 필요
                            width=total_width10, no_wrap=True, overflow=flet.TextOverflow.ELLIPSIS, )),
                        flet.DataCell(flet.Text(
                            customer_data[2], tooltip=customer_data[2],
                            width=total_width15, no_wrap=True, overflow=flet.TextOverflow.ELLIPSIS, )),
                        flet.DataCell(flet.Text(
                            customer_data[3], tooltip=customer_data[3],
                            width=total_width20, no_wrap=True, overflow=flet.TextOverflow.ELLIPSIS, )),
                        flet.DataCell(flet.Text(
                            customer_data[4], tooltip=customer_data[4],
                            width=total_width20, no_wrap=True, overflow=flet.TextOverflow.ELLIPSIS, )),
                        flet.DataCell(flet.Text(str(customer_data[5])[:10], tooltip=str(customer_data[5]),
                                                # [:10] : 앞쪽 10자만 출력(str 형변환 필요)
                            width=total_width15, no_wrap=True, overflow=flet.TextOverflow.ELLIPSIS, color=status_color)),
                        flet.DataCell(flet.Text(
                            customer_data[6], tooltip=customer_data[6],# no_wrap=True : 줄바꿈 금지
                            width=total_width10, no_wrap=True, overflow=flet.TextOverflow.ELLIPSIS, color=status_color)),
                            # overflow : 넘치면 ... 출력, tooltip : 마우스 올리면 전체 표시
                    ])
                )
                customer_id_data.update()
            else:
                page.open(error_quit)
        except Exception as err:
            print(f"Search Customer error : {err}")
    customer_id_text = flet.TextField(
        text_size=Font.fontsize, width=150, height=30, content_padding=5, max_length=10, autofocus=True)
    search_id = flet.Button(
        "Search", on_click=query_customer_by_id, width=80,
        style=flet.ButtonStyle(shape=(flet.RoundedRectangleBorder(radius=5))))
    customer_id_data = flet.DataTable(
        columns=[
            flet.DataColumn(flet.Text("Store", width=total_width10)),
            flet.DataColumn(flet.Text("ID", width=total_width10)),
            flet.DataColumn(flet.Text("Name", width=total_width15)),
            flet.DataColumn(flet.Text("Email", width=total_width20)),
            flet.DataColumn(flet.Text("Address", width=total_width20)),
            flet.DataColumn(flet.Text("Create Date", width=total_width15)),
            flet.DataColumn(flet.Text("Status", width=total_width10)),
        ],
        rows=[],
        border=flet.border.all(1, "flet.Colors.BLUE_GREY_100"), # DataTable Titlebar
        vertical_lines=flet.border.all(1, "flet.Colors.BLUE_GREY_100"), # DataTable Titlebar
        horizontal_lines=flet.border.all(1, "flet.Colors.BLUE_GREY_100"), # DataTable Titlebar
        heading_row_color=flet.Colors.GREY_300, # DataTable Titlebar Inside Color
        heading_row_height=Font.height, # DataTable Titlebar Height
        data_row_min_height=Font.height-2, # DataTable Data Min Height
        data_row_max_height=Font.height-2, # DataTable Data Max Height
    )
    customer_id = flet.Row(
        controls=[
            flet.Column([customer_id_data])
        ],
        expand=True,
    )
    return customer_id_text, search_id, customer_id

def build_customer_name_ui(page, store_id, conn):
    def query_customer_by_name(e):
        customer_name_value = f"%{customer_name_text.value}%"
        def close_pop(e):
            page.close(error_quit)  # 팝업창 종료 명령어
        error_quit = flet.AlertDialog(
            title=flet.Text("Customer"),
            content=flet.Text(f"Customer Name Not Found [{customer_name_text.value}]"),
            actions=[flet.TextButton("OK", on_click=close_pop)
                     ], actions_alignment=flet.MainAxisAlignment.END)
        cursor = conn.cursor()
        try:
            cursor.execute(
                """ select
                        id ,
                        name ,
                        address ,
                        "zip code" ,
                        phone ,
                        city ,
                        country ,
                        notes
                    from customer_list
                    where name Ilike %s
                        and sid = %s
                    order by id , name """,(customer_name_value,store_id,)
            )
            customer_data = cursor.fetchall()
            if customer_data:
                customer_name_data.rows.clear()
                for sc_row in customer_data:
                    customer_name_data.rows.append(
                        flet.DataRow(cells=[
                            flet.DataCell(flet.Text(sc_row[0])),
                            flet.DataCell(flet.Text(sc_row[1])),
                            flet.DataCell(flet.Text(sc_row[2])),
                            flet.DataCell(flet.Text(sc_row[3])),
                            flet.DataCell(flet.Text(sc_row[4])),
                            flet.DataCell(flet.Text(sc_row[5])),
                            flet.DataCell(flet.Text(sc_row[6])),
                            flet.DataCell(flet.Text(sc_row[7])),
                        ])
                    )
                customer_name_data.update()
            else:
                page.open(error_quit)
        except Exception as err:
            print(f"Search Customer error : {err}")
    customer_name_text = flet.TextField(
        text_size=Font.fontsize, width=150, height=30, content_padding=5, max_length=10, autofocus=True)
    search_name = flet.Button("Search", on_click=query_customer_by_name, width=80,
                              style=flet.ButtonStyle(shape=(flet.RoundedRectangleBorder(radius=5))))
    customer_name_data = flet.DataTable(
        columns=[
            flet.DataColumn(flet.Text("ID")),
            flet.DataColumn(flet.Text("Name")),
            flet.DataColumn(flet.Text("Address")),
            flet.DataColumn(flet.Text("Zip Code")),
            flet.DataColumn(flet.Text("Phone")),
            flet.DataColumn(flet.Text("City")),
            flet.DataColumn(flet.Text("Country")),
            flet.DataColumn(flet.Text("Notes")),
        ],
        rows=[],
        border=flet.border.all(1, "flet.Colors.BLUE_GREY_100"), # DataTable Titlebar
        vertical_lines=flet.border.all(1, "flet.Colors.BLUE_GREY_100"), # DataTable Titlebar
        horizontal_lines=flet.border.all(1, "flet.Colors.BLUE_GREY_100"), # DataTable Titlebar
        heading_row_color=flet.Colors.GREY_300, # DataTable Titlebar Inside Color
        heading_row_height=Font.height, # DataTable Titlebar Height
        data_row_min_height=Font.height-2, # DataTable Data Min Height
        data_row_max_height=Font.height-2, # DataTable Data Max Height
    )
    customer_name = flet.Row(
        controls=[flet.Column([customer_name_data], scroll=flet.ScrollMode.ALWAYS)],
        scroll=flet.ScrollMode.AUTO,
        expand=True,
    )
    return customer_name_text, search_name, customer_name