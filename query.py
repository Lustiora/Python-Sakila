class Search:
    #############################################
    # menu search customer
    #############################################
    customer_name_query\
        ="""select customer_id
            from customer
            where first_name ilike %s 
                or last_name ilike %s"""

    customer_id_query\
        ="""select
                case when c.store_id = 1 then '🇨🇦 Lethbridge' else '🇦🇺 Woodridge' end as store ,
                c.first_name || ' ' || c.last_name as name,
                c.customer_id ,
                c.email ,
                '('||left(a.phone,4) ||') '|| substring(a.phone,5,4) ||'-'|| right(a.phone,4) as phone ,
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
                and c.customer_id = ANY(%s)""" # ANY(%s) : 상자에 담겨있는 ID들을 전부 비교
    # <-- View Table Create -->
    # CREATE OR REPLACE VIEW public.not_return_customer as
    #  select distinct r.customer_id
    #  from rental r
    #  inner join inventory i
    #      on r.inventory_id = i.inventory_id
    #  inner join film f
    #      on i.film_id = f.film_id
    #  where r.return_date is null
    #      and r.rental_date + (f.rental_duration * INTERVAL '1 day') < now();

    #############################################
    # menu search inventory
    #############################################
    film_title_query\
        ="""select distinct inventory_id
            from inventory_data
            where title ilike %s """

    inventory_id_query\
        ="""select
                inventory_id ,
                title ,
                case when store_id = 1 then '🇨🇦 Lethbridge' else '🇦🇺 Woodridge' end as store ,
                case when return_date is not null then 'In stock' else 'Checked out' end as status ,
                rental_date ,
                '$'||rental_rate ,
                store_id
            from inventory_data
            where status is not null
            and inventory_id = ANY(%s)""" # ANY(%s) : 상자에 담겨있는 ID들을 전부 비교
    # <-- View Table Create -->
    # CREATE OR REPLACE VIEW public.inventory_data as (
    # select
    #     i.inventory_id ,
    #     f.title ,
    #     i.store_id ,
    #     r.rental_date ,
    #     r.return_date ,
    #     case when rank() over (
    #         partition by i.inventory_id , i.store_id order by r.rental_date desc) = 1 then 1
    #     else null end as status ,
    #     f.rental_rate
    # from inventory i
    # inner join film f
    #     on i.film_id = f.film_id
    # inner join rental r
    #     on i.inventory_id = r.inventory_id);

    #############################################
    # menu search rental
    #############################################
    return_total_query\
        ="""select count(*)
            from rental_data
            where return_date is null
            and store_id = %s"""

    rental_search_total_query \
        = """select 
                rental_id ,
                name ,
                title ,
                to_char(rental_date,'YYYY-MM-DD hh:mm:ss') as rental_date,
                to_char(due_day,'YYYY-MM-DD hh:mm:ss') as due_day ,
                case
                    when due_day < today 
                        then 'Overdue'||' ('||replace(date_trunc('day',over_due)::text,'00:00:00','1 days')||')'
                    else 'Unreturned'
                end as status
            from rental_data
            where return_date is null
            and store_id = %s
            order by return_date desc, rental_date desc"""

    return_overdue_query\
        ="""select count(*)
            from rental_data
            where return_date is null
            and due_day < today
            and store_id = %s"""

    rental_search_overdue_query \
        = """select 
                rental_id ,
                name ,
                title ,
                to_char(rental_date,'YYYY-MM-DD hh:mm:ss') as rental_date,
                to_char(due_day,'YYYY-MM-DD hh:mm:ss') as due_day ,
                case
                    when due_day < today 
                        then 'Overdue'||' ('||replace(date_trunc('day',over_due)::text,'00:00:00','1 days')||')'
                    else 'Unreturned'
                end as status
            from rental_data
            where return_date is null
            and due_day < today
            and store_id = %s
            order by over_due desc"""

    return_due_today_query\
        ="""select count(*)
            from rental_data
            where return_date is null
            and due_day::date = today
            and store_id = %s"""

    rental_search_due_today_query \
        = """select 
                rental_id,
                name,
                title,
                to_char(rental_date,'YYYY-MM-DD hh:mm:ss') as rental_date,
                to_char(due_day,'YYYY-MM-DD hh:mm:ss') as due_day ,
                case
                    when due_day < today 
                        then 'Overdue'||' ('||replace(date_trunc('day',over_due)::text,'00:00:00','1 days')||')'
                    else 'Unreturned'
                end as status
             from rental_data
             where return_date is null
             and due_day::date = today
             and store_id = %s
             order by return_date desc, rental_date desc"""

    rental_search_name_query\
        ="""select 
                rental_id
            from rental_data
            where store_id = %s
            and name ilike %s"""

    rental_search_id_query\
        ="""select 
                rental_id ,
                name ,
                title ,
                to_char(rental_date,'YYYY-MM-DD hh:mm:ss') as rental_date,
                to_char(due_day,'YYYY-MM-DD hh:mm:ss') as due_day ,
                case 
                    when over_due is not null 
                        then 'Overdue'||' ('||replace(date_trunc('day',over_due)::text,'00:00:00','1 days')||')'
                    when today < due_day then 'Unreturned'
                    else 'Returned' 
                end as status
            from rental_data
            where store_id = %s
            and rental_id = ANY(%s)
            order by return_date desc, rental_date desc"""
    # <-- View Table Create -->
    # CREATE OR REPLACE VIEW public.rental_data as (
    # select
    # 	r.rental_id ,
    # 	c.first_name ||' '||c.last_name as name ,
    # 	f.title ,
    # 	r.rental_date ,
    # 	r.rental_date + (interval '1 day' * f.rental_duration) as due_day ,
    # 	r.return_date ,
    # 	f.rental_duration ,
    # 	case
    # 		when r.return_date is null
    # 			and CURRENT_DATE > r.rental_date + (interval '1 day' * f.rental_duration)
    # 			then CURRENT_DATE - (r.rental_date + (interval '1 day' * f.rental_duration))
    # 	end as over_due ,
    # 	CURRENT_DATE as today ,
    # 	c.store_id
    # from rental r
    # inner join customer c
    # 	on r.customer_id = c.customer_id
    # inner join inventory i
    # 	on r.inventory_id = i.inventory_id
    # inner join film f
    # 	on i.film_id = f.film_id
    # order by r.rental_date , f.rental_duration);