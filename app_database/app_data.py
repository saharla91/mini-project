from multiprocessing.spawn import import_main_path
from select import select
import pymysql
import os
from dotenv import load_dotenv


load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

connection = pymysql.connect(
    host = host,
    user = user,
    password = password,
    database = database,
)
cursor = connection.cursor()

#----main menu------
while True: 
    print('''--------VIEW MAIN MENU--------

        [0] To exit the program

        [1]To view the Product menu

        [2]To view Courier menu

        [3]To view Order menu''')

    menu = int(input("select one of the options: "))
        
    
    #------products-------
    if menu == 1:
        while True:    
            print('''-----PRODUCT MENU-----

        [0]To exit product menu

        [1]To view the Products

        [2]To create product

        [3]To update product

        [4]To delete a product''')

        #PRODUCT MENU
        #input to get product list
            product_menu = int(input("Enter product menu option: "))
            if product_menu == 1:
                cursor.execute("SELECT * FROM products")
                product_connect = cursor.fetchall()
                for x in product_connect:
                    print(x)

            if product_menu == 2:
                new_product = input("Enter product: ")
                new_price = input("Enter price: ")
                sql = "INSERT INTO products (name, price) VALUES (%s, %s)"
                val = (new_product, new_price)
                cursor.execute(sql, val)
                product_dictionary ={"name":new_product, "price":new_price}
                print("This is your new Product",product_dictionary)
                
            if product_menu == 3:
                cursor.execute('SELECT * FROM products')
                for i in cursor:
                    print(i)
                select_id = int(input("Enter id: "))
                updated_product_name = input("Update product name: ")
                updated_product_price = float(input("Enter updated price: "))
                if updated_product_name:
                    sql_update_name = "UPDATE products SET name = %s WHERE id = %s"
                    val_update_name = (updated_product_name, select_id)
                    cursor.execute(sql_update_name,val_update_name)
                    print("Product name has been updated")
                if updated_product_price:
                    sql_update_price = "UPDATE products SET price = %s WHERE id = %s"
                    val_update_price = (updated_product_price, select_id)
                    cursor.execute(sql_update_price, val_update_price)
                    print("price has been updated")

            if product_menu == 4:
                cursor.execute('SELECT * FROM products')
                for i in cursor:
                    print(i)
                cursor = connection.cursor()
                delete_product_id = int(input("Enter product id: "))
                sql_delete_product = "DELETE FROM products WHERE id = %s"
                val_delete_product = (delete_product_id)
                cursor.execute(sql_delete_product, val_delete_product)
                connection.commit()
                print(cursor.rowcount, "record(s) deleted")

            if product_menu == 0:
                print("product menu has ended")
                break

    #------couriers--------
    if menu == 2:
        while True:
            print('''-----COURIER MENU----

            [0]Exit courier menu

            [1]To view couriers

            [2]To create courier

            [3]Update courier
            
            [4]To delete courier''')

            courier_menu = int(input("Enter courier menu option: "))
            if courier_menu == 1:
                cursor.execute("SELECT * FROM couriers")
                courier_connect = cursor.fetchall()
                for x in courier_connect:
                    print(x)
                

            if courier_menu == 2:
                new_courier = input("Enter courier: ")
                new_courier_number = int(input("Enter number: "))
                sql = "INSERT INTO couriers (name, number) VALUES (%s, %s)"
                val = (new_courier, new_courier_number)
                cursor.execute(sql, val)
                courier_dictionary ={"name":new_courier, "number":new_courier_number}
                print("This is your new Product",courier_dictionary)
            
            if courier_menu == 3:
                    cursor.execute('SELECT * FROM couriers')
                    for i in cursor:
                        print(i)
                    select_courier_id = int(input("Enter id: "))
                    updated_courier_name = input("Update courier name:")
                    updated_courier_number = int(input("update courier number: "))
                    if updated_courier_name:
                        sql_updated_courier_name = "UPDATE couriers SET name = %s WHERE id = %s"
                        val_updated_courier_name = (updated_courier_name, select_courier_id)
                        cursor.execute(sql_updated_courier_name, val_updated_courier_name)
                        print("courier name has been updated")
                    if updated_courier_number:
                        sql_updated_courier_number = "UPDATE couriers SET number = %s WHERE id = %s"
                        val_updated_courier_number = (updated_courier_number, select_courier_id)
                        cursor.execute(sql_updated_courier_number, val_updated_courier_number)
                        print("courier number has been updated")

                    connection.commit()

            if courier_menu == 4:
                cursor.execute('SELECT * FROM couriers')
                for i in cursor:
                    print(i)
                cursor = connection.cursor()
                delete_courier_id = int(input("enter courier id: "))
                sql_delete_courier = "DELETE FROM couriers WHERE id = %s"
                val_delete_courier = (delete_courier_id)
                cursor.execute(sql_delete_courier, val_delete_courier)
                connection.commit()
                print(cursor.rowcount, "record(s) deleted")

            if courier_menu == 0:
                print("courier menu has ended")
                break
            #cursor.close()
            #connection.close()

    #-------orders------
    if menu == 3:
        while True:
            print('''-----ORDER MENU----

        [0]Exit orders menu

        [1]To view  orders

        [2]To create order
    
        [3]Update orders
        
        [4]Delete order''')

            order_menu = int(input("enter order menu option: "))
            if order_menu == 1:
                cursor.execute('''SELECT orders.id, orders.name, orders.address, orders.phone, orders.courier, orders.status, group_concat(products.name) FROM orders
JOIN products_on_orders on orders.id = products_on_orders.order_id
JOIN products on products_on_orders.product_id = products.id
GROUP BY orders.id, orders.name, orders.address, orders.phone, orders.courier, orders.status''')
                order_connect = cursor.fetchall()
                for x in order_connect:
                    print(x)

            if order_menu == 2:
                cursor.execute('''SELECT orders.id, orders.name, orders.address, orders.phone, orders.courier, orders.status, group_concat(products.name) FROM orders
JOIN products_on_orders on orders.id = products_on_orders.order_id
JOIN products on products_on_orders.product_id = products.id
GROUP BY orders.id, orders.name, orders.address, orders.phone, orders.courier, orders.status ''')
                for i in cursor:
                    print(i)
                new_customer_name = input("Enter customer name: ")
                new_customer_address = input("Enter customer address: ")
                new_customer_phone = int(input("Enter customer number: "))
                cursor.execute("SELECT * FROM couriers")
                courier_connect = cursor.fetchall()
                for x in courier_connect:
                    print(x)
                customer_courier = int(input("which courier do you want to add: "))
                if new_customer_name:
                    sql_customer_name = "INSERT INTO orders (name, address, phone, courier, status) VALUES (%s, %s, %s, %s, %s)"
                    val_customer_name = (new_customer_name, new_customer_address, new_customer_phone, customer_courier, "preparing")
                    cursor.execute(sql_customer_name, val_customer_name)
                    order_id = cursor.lastrowid
                    cursor.execute("SELECT * FROM products")
                    product_connect = cursor.fetchall()
                    for x in product_connect:
                        print(x)
                    user_product_selection = input("what product would you like: ")
                    user_product_list = user_product_selection.split(",")

                    for product in user_product_list:
                        sql_order_id_to_orders = "INSERT INTO products_on_orders (order_id, product_id) VALUES (%s, %s)"
                        val_order_id_to_orders = (order_id, int(product))
                        cursor.execute(sql_order_id_to_orders, val_order_id_to_orders)


                        print("customer order details has been added")
                        connection.commit()


            if order_menu == 3:
                cursor.execute('SELECT * FROM orders')
                for i in cursor:
                    print(i)
                order_id = int(input("Select order id: "))
                update_status_order = input("update status order: ")
                if update_status_order:
                    sql_update_status_order = "UPDATE orders SET status = %s WHERE id = %s"
                    val_update_status_order = (update_status_order, order_id)
                    cursor.execute(sql_update_status_order, val_update_status_order)
                    print("order status has been updated",)
                    cursor.execute('SELECT * FROM orders')
                    for i in cursor:
                        print(i)
                    connection.commit()

            if order_menu == 4:
                cursor.execute('SELECT * FROM orders')
                for a in cursor:
                    print(a)
                cursor = connection.cursor()
                delete_order_id = int(input("enter order id: "))
                sql_delete_order = "DELETE FROM orders WHERE id = %s"
                val_delete_order = (delete_order_id)
                cursor.execute(sql_delete_order, val_delete_order)
                connection.commit()
                print(cursor.rowcount, "record(s) deleted")
    
            if order_menu == 0:
                print("order menu has ended")
                break
    
    #---Menu is finished------
    if menu == 0:
        print("Menu had ended, Thank you")
        break
                

            
