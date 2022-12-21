""" this module sets up an interactive filtering mechanism
to filter the data table from user input  """
import main


# rough draft
# need for loop or even a while loop in here

def search_selection(db_cursor):
    print('Choose a product category: \n\n'
          '\t1. Over Ear Headphones\n\n'
          '\t2. USB Microphones\n\n'
          '\t3. 1080p Webcams\n\n'
          '\t4. Capture Cards\n\n'
          '\t5. 8-channel Audio Mixers\n\n'
          '\t6. Gaming Laptops\n\n')

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
        # resets by calling recursively
        search_selection()


# categories = ['Over Ear Headphones', 'USB Microphones', '1080p Webcams', 'Capture Cards', '8-channel Audio Mixers',
#               'Gaming Laptops']


def ask_questions_create_sql(db_cursor, table):
    # these are all the VARIABLES for the users choice in filtering
    # STAR INFO
    star_review = input('Enter a target star review (ex. 4.5): ')
    star_operator = input('Choose an equality operator (>, <, >=, <=, =): ')

    # NUMBER OF REVIEWS INFO
    num_review = int(input('Enter a target number of reviews (ex: 1000): '))
    review_operator = input('Choose an equality operator (>, <, >=, <=, =): ')

    # PRICE INFO
    target_price = float(input('Enter a target price:'))
    price_operator = input('Choose an equality operator (>, <, >=, <=, =): ')

    # SELECT * FROM Over_Ear_Headphones_Table WHERE rating >= 4.6 AND num_ratings > 10000 AND price <= 50
    sql = f"""Select * from {table} 
            where rating {star_operator} {star_review} and 
            num_ratings {review_operator} {num_review} and 
            price {price_operator} {target_price}"""
    print('\nPRODUCT NAME                                                                        RATING'
          '\n------------------------------------------------------------------------------------------------------')
    # results = db_cursor.execute(sql)
    i = 1
    for row in db_cursor.execute(sql):
        val = 100 - len(str(row))
        print(str(i), ") ", str(row).strip("(,')").replace("', '", val * " "))
        print('\n')
        i = i + 1

    # executequestion = input('Would you like to execute another query (yes/no):\n')


# these functions are when user chooses the appropriate categories and it displays to them
# idk this part cuz the select statement has all variables and not actual numbers
def OverEarHeadPhones(db_cursor):
    print("\nyou selected OVER EAR HEADPHONES")
    table = 'Over_Ear_Headphones_Table'
    ask_questions_create_sql(db_cursor, table)


def MicSelection(db_cursor):
    print("\nyou selected MIC")
    table = 'USB_Microphones_Table'
    ask_questions_create_sql(db_cursor, table)


def WebCamSelection(db_cursor):
    print("\nyou selected WEBCAM")
    table = 'Webcams_Table'
    ask_questions_create_sql(db_cursor, table)


def CardsSelection(db_cursor):
    print("\nyou selected CARDS")
    table = 'Capture_Cards_Table'
    ask_questions_create_sql(db_cursor, table)


def AudioSelection(db_cursor):
    print("\nyou selected AUDIO THINGY")
    table = 'Audio_Mixers_Table'
    ask_questions_create_sql(db_cursor, table)


def GamingLaptopSelection(db_cursor):
    print("\nyou selected GAMING LAPTOP")
    table = 'Gaming_Laptops_Table'
    ask_questions_create_sql(db_cursor, table)


# this function filters the category the user chooses from the data tables
# almost like parsing
# def filter_data(input_category, categories):
#     if input_category == categories[0]:
#         OverEarSelection()
#     if input_category == categories[1]:
#         MicSelection()
#     if input_category == categories[2]:
#         WebCamSelection()
#     if input_category == categories[3]:
#         CardsSelection()
#     if input_category == categories[4]:
#         AudioSelection()
#     if input_category == categories[5]:
#         GamingLaptopSelection()
#     else:
#         print('Error: Invalid Number')

# this function displays everything to user, so calling all the functions to make it clean code. and this function
# will be called in main i think
# def display_to_user():
#    print(input_category)
#    print(starreview)
#    print(staroperator)
#    print(numreview)
#    print(reviewoperator)
#    print(targetprice)
#    print(priceoperator)
#    filter_data()
#    print(executequestion)
#    if executequestion == 'no' or 'n':
#        break
#    elif executequestion == 'yes' or 'y':
#        continue
#    else:
#        print('Error ')
