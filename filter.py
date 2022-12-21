import main
import web_page_scraper

""" this module sets up an interactive filtering mechanism
to filter the data table from user input  """
# rough draft
# need for loop or even a while loop in here
def print_statements():
    input_category = int(input('Choose a product category: \n\n'
                               '\t1. Over Ear Headphones\n\n'
                               '\t2. USB Microphones\n\n'
                               '\t3. 1080p Webcams\n\n'
                               '\t4. Capture Cards\n\n'
                               '\t5. 8-channel Audio Mixers\n\n'
                               '\t6. Gaming Laptops\n\n'))

    categories = ['Over Ear Headphones', 'USB Microphones', '1080p Webcams', 'Capture Cards', '8-channel Audio Mixers',
                  'Gaming Laptops']

    # these are all the VARIABLES for the users choice in filtering
    #STAR INFO
    starreview = int(input('Enter a target star review (ex. 4.5):\n'))
    staroperator = input('Choose an equality operator (>, <, >=, <=, =):\n')

    #NUMBER OF REVIEWS INFO
    numreview = int(input('Enter a target number of reviews (ex: 1000): '))
    reviewoperator= input('Choose an equality operator (>, <, >=, <=, =):\n')

    #PRICE INFO
    targetprice = float(input('Enter a target price:'))
    priceoperator = input('Choose an equality operator (>, <, >=, <=, =):\n')

    executequestion = input('Would you like to execute another query (yes/no):\n')

# these functions are when user chooses the appropriate categories and it displays to them
# idk this part cuz the select statement has all variables and not actual numbers
def OverEarSelection(db_cursor, input_category, categories):
        db_cursor.execute('SELECT * FROM Over_Ear_Headphones_Table WHERE extract_product_rating staroperator starreview AND extract_num_ratings reviewoperator numreviews AND extract_product_price priceoperator targetprice')
        print(db_cursor)
        # using print statement bc we have to print out to the terminal

def MicSelection(db_cursor):
    db_cursor.execute('SELECT * FROM Over_Ear_Headphones_Table WHERE extract_product_rating staroperator starreview AND extract_num_ratings reviewoperator numreviews AND extract_product_price priceoperator targetprice')
    print(db_cursor)

def WebCamSelection(db_cursor):
    db_cursor.execute('SELECT * FROM Over_Ear_Headphones_Table WHERE extract_product_rating staroperator starreview AND extract_num_ratings reviewoperator numreviews AND extract_product_price priceoperator targetprice')
    print(db_cursor)

def CardsSelection(db_cursor):
    db_cursor.execute('SELECT * FROM Over_Ear_Headphones_Table WHERE extract_product_rating staroperator starreview AND extract_num_ratings reviewoperator numreviews AND extract_product_price priceoperator targetprice')
    print(db_cursor)

def AudioSelection(db_cursor):
    db_cursor.execute('SELECT * FROM Over_Ear_Headphones_Table WHERE extract_product_rating staroperator starreview AND extract_num_ratings reviewoperator numreviews AND extract_product_price priceoperator targetprice')
    print(db_cursor)

def GamingLaptopSelection(db_cursor):
    db_cursor.execute('SELECT * FROM Over_Ear_Headphones_Table WHERE extract_product_rating staroperator starreview AND extract_num_ratings reviewoperator numreviews AND extract_product_price priceoperator targetprice')
    print(db_cursor)

# this function filters the category the user chooses from the data tables
# almost like parsing
def filter_data(input_category,categories):
    if input_category == categories[0]:
        OverEarSelection()
    if input_category == categories[1]:
        MicSelection()
    if input_category == categories[2]:
        WebCamSelection()
    if input_category == categories[3]:
        CardsSelection()
    if input_category == categories[4]:
        AudioSelection()
    if input_category == categories[5]:
        GamingLaptopSelection()
    else:
     print('Error: Invalid Number')


# this function displays everything to user, so calling all the functions to make it clean code. and this function
# will be called in main i think
def display_to_user():
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
