products = {
    "mobiles": {
        "Apple": [
            {
                "id": 1,
                "name": "iPhone 7",
                "price": 300
            },
            {
                "id": 2,
                "name": "iPhone 8",
                "price": 350
            },
            {
                "id": 3,
                "name": "iPhone Xr",
                "price": 450
            },
            {
                "id": 4,
                "name": "iPhone Xs",
                "price": 460
            },
            {
                "id": 5,
                "name": "iPhone 11",
                "price": 900
            },
            {
                "id": 6,
                "name": "iPhone 12",
                "price": 1100
            },
            {
                "id": 7,
                "name": "iPhone 13",
                "price": 1300
            },
        ],
        "Samsung": [
            {
                "id": 8,
                "name": "Samsung Galaxy Beam",
                "price": 150
            },
            {
                "id": 9,
                "name": "Samsung Galaxy S6",
                "price": 200
            },
            {
                "id": 10,
                "name": "Samsung Galaxy S7",
                "price": 300
            },
        ],
        "Xiaomi": [
            {
                "id": 11,
                "name": "Xiaomi Redmi Note 8",
                "price": 250
            },
            {
                "id": 12,
                "name": "Xiaomi Redmi Note 8 Pro",
                "price": 300
            },
        ]
    },
    "laptops": {
        "DELL": [
            {
                "id": 13,
                "name": "Dell Inspiron 15",
                "price": 600
            },
            {
                "id": 14,
                "name": "Dell Latitude 14",
                "price": 650
            },
        ],
        "MAC": [
            {
                "id": 15,
                "name": "MacBook Pro 13",
                "price": 900
            },
            {
                "id": 16,
                "name": "MacBook M1",
                "price": 1500
            },
        ]
    },
}

while True:
    selector=input("Please enter a valid option:\n1-Show product list\n2-Buy\n3-Add coupon\n4-Exit\n->")
    if selector == "1":
        for type, brands in products.items():
            for product, item in brands.items():
                for order in item:
                    print("{}) {} - {}$"
                    .format(order["id"], order["name"], order["price"]))
    elif selector == "4":
        break
    elif selector == "2":
        product_to_buy=int(input("Please enter the item number (can be checked on the product list): "))
        product_selected: None
        client_info={}
        for type, brands in products.items():
            for product, item in brands.items():
                for order in item:
                    if order.get("id") == product_to_buy:
                        product_selected=order
        if product_selected == None:
            print("Product not found")
            continue
        else:
            client_info["name"] = input("Please enter your name: ")
            client_info["lastname"] = input("Please enter your last name: ")
            client_info["id_number"] = input("Please enter your ID number: ")
            client_info["product_id"] = product_to_buy
        
        print("***** RECEIPT ******")
        print("Name:",client_info.get("name"))
        print("Lastname:",client_info.get("lastname"))
        print("Id Card:",client_info.get("id_card"))
        print("Product:",product_selected.get("name"))
        print("Total:",product_selected.get("price"))
