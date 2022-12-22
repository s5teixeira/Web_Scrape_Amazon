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


def write_to_file(x):
    """This function writes filtered data to a txt file """
    with open("filtered_data.txt", "a") as data_out_file:
        try:
            data_out_file.write(f'\n{x}\n\n')
        except UnicodeEncodeError:
            data_out_file.write(f"\nUnicodeEncodeError\n\n")


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
    print('\nAvailable Listings'
          '\n------------------------------------------------------------------------------------------------------------------------------------------------')
    # results = db_cursor.execute(sql)
    line_to_filtered_data_file = f'----------------------------------------------------------------------------------------\n' \
                                 f'{str(table).strip("_Table", "")} results with: {star_operator} {star_review} stars, {review_operator} {num_review}, ' \
                                 f'{price_operator} {target_price}:\n' \
                                 f'----------------------------------------------------------------------------------------\n'
    write_to_file(line_to_filtered_data_file)
    i = 1
    for row in db_cursor.execute(sql):
        val = 100 - len(str(row))
        print(str(i), ") ", str(row).strip("(,')").replace("', '", val * " "))
        print('\n')
        i = i + 1
        write_to_file(row)
    main.ask_to_continue(db_cursor)


def OverEarHeadPhones(db_cursor):
    """ this function applies the Headphones choice selection to the appropriate filtered table"""
    print("\nOVER EAR HEADPHONES SELECTION")
    print('\n------------------------------------------------------------------------------------------------')
    table = 'Over_Ear_Headphones_Table'
    questions_about_filtering(db_cursor, table)


def MicSelection(db_cursor):
    """ this function applies the Mic selection to the appropriate filtered table"""
    print("\nUSB MICROPHONES SELECTION")
    print('\n------------------------------------------------------------------------------------------------')
    table = 'USB_Microphones_Table'
    questions_about_filtering(db_cursor, table)


def WebCamSelection(db_cursor):
    """ this function applies the Webcam selection to the appropriate filtered table"""
    print("\nWEBCAM SELECTION")
    print('\n------------------------------------------------------------------------------------------------')
    table = 'Webcams_Table'
    questions_about_filtering(db_cursor, table)


def CardsSelection(db_cursor):
    """ this function applies the Cards selection to the appropriate filtered table"""
    print("\nCAPTURE CARDS SELECTION")
    print('\n------------------------------------------------------------------------------------------------')
    table = 'Capture_Cards_Table'
    questions_about_filtering(db_cursor, table)


def AudioSelection(db_cursor):
    """ this function applies the Audio selection to the appropriate filtered table"""
    print("\nAUDIO MIXERS SELECTION")
    print('\n------------------------------------------------------------------------------------------------')
    table = 'Audio_Mixers_Table'
    questions_about_filtering(db_cursor, table)


def GamingLaptopSelection(db_cursor):
    """ this function applies the Gaming selection to the appropriate filtered table"""
    print("\nGAMING LAPTOP SELECTION")
    print('\n------------------------------------------------------------------------------------------------')
    table = 'Gaming_Laptops_Table'
    questions_about_filtering(db_cursor, table)
