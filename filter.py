import main

""" This module sets up an interactive filtering mechanism
to filter the data table from user input  """


def search_selection(db_cursor):
    """This function parses the users input and corresponds it to the appropriate selection  """
    print_statement()
    param = input("(type 1, 2, 3, 4, 5, or 6) >> ")

    if param == "1":
        OverEarHeadPhones(db_cursor)

    elif param == "2":
        MicSelection(db_cursor)

    elif param == "3":
        WebCamSelection(db_cursor)

    elif param == "4":
        CardsSelection(db_cursor)

    elif param == "5":
        AudioSelection(db_cursor)

    elif param == "6":
        GamingLaptopSelection(db_cursor)

    else:
        print("\ninvalid input\n")
        search_selection()


def print_statement():
    """This function prints out the list of choices the user can choose from"""
    print('Choose a product category: \n\n'
          '\t1. Over Ear Headphones\n\n'
          '\t2. USB Microphones\n\n'
          '\t3. 1080p Webcams\n\n'
          '\t4. Capture Cards\n\n'
          '\t5. 8-channel Audio Mixers\n\n'
          '\t6. Gaming Laptops\n\n')


def questions_about_filtering(db_cursor, table):
    """This function asks the user about filtering """
    star_review = float(input('Enter a target star review (ex. 4.5): '))
    star_operator = input('Choose an equality operator (>, <, >=, <=, =): ')

    num_review = int(input('Enter a target number of reviews (ex: 1000): '))
    review_operator = input('Choose an equality operator (>, <, >=, <=, =): ')

    target_price = float(input('Enter a target price:'))
    price_operator = input('Choose an equality operator (>, <, >=, <=, =): ')
    sqlfunction(db_cursor, table, star_operator, star_review, review_operator, num_review, target_price,
                price_operator)


def sqlfunction(db_cursor, table, star_operator, star_review, review_operator, num_review, target_price,
                price_operator):
    """this function uses the select statement to filter based on users input """
    sql = f"""Select * from {table} 
            where rating {star_operator} {star_review} and 
            num_ratings {review_operator} {num_review} and 
            price {price_operator} {target_price}"""
    print('\nPRODUCT NAME                                                                                                                        RATING'
          '\n------------------------------------------------------------------------------------------------------------------------------------------------')
    # results = db_cursor.execute(sql)
    i = 1
    for row in db_cursor.execute(sql):
        val = 100 - len(str(row))
        print(str(i), ") ", str(row).strip("(,')").replace("', '", val * " "))
        print('\n')
        i = i + 1
    main.ask_to_continue(db_cursor)


def OverEarHeadPhones(db_cursor):
    """ this function applies the Headphones choice selection to the appropriate filtered table"""
    print("\nyou selected OVER EAR HEADPHONES")
    table = 'Over_Ear_Headphones_Table'
    questions_about_filtering(db_cursor, table)


def MicSelection(db_cursor):
    """ this function applies the Mic selection to the appropriate filtered table"""
    print("\nyou selected MIC")
    table = 'USB_Microphones_Table'
    questions_about_filtering(db_cursor, table)


def WebCamSelection(db_cursor):
    """ this function applies the Webcam selection to the appropriate filtered table"""
    print("\nyou selected WEBCAM")
    table = 'Webcams_Table'
    questions_about_filtering(db_cursor, table)


def CardsSelection(db_cursor):
    """ this function applies the Cards selection to the appropriate filtered table"""
    print("\nyou selected CARDS")
    table = 'Capture_Cards_Table'
    questions_about_filtering(db_cursor, table)


def AudioSelection(db_cursor):
    """ this function applies the Audio selection to the appropriate filtered table"""
    print("\nyou selected AUDIO THINGY")
    table = 'Audio_Mixers_Table'
    questions_about_filtering(db_cursor, table)


def GamingLaptopSelection(db_cursor):
    """ this function applies the Gaming selection to the appropriate filtered table"""
    print("\nyou selected GAMING LAPTOP")
    table = 'Gaming_Laptops_Table'
    questions_about_filtering(db_cursor, table)
