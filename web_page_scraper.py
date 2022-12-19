import requests
from bs4 import BeautifulSoup
import main

# this module is for all the products we need to scrape

HEADERS_FOR_GET_REQ = (
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
     'Accept-Language': 'en-US, en;q=0.5'}
)


def get_search_url(keywords):
    # this function creates the url using the given keywords ex: 'over ear headphones'
    listing_counter = 0
    listing_limit = 3  # <--- the number of times this function will run after being called once
    url_results_page_param = 1
    while listing_counter < listing_limit:
        results_url_param = f'&page={url_results_page_param}'
        query_terms = keywords.replace(' ', '+')
        base_amazon_search_url = 'https://www.amazon.com/s?k='
        search_url = f'{base_amazon_search_url}{query_terms}{results_url_param}'
        response = requests.get(search_url, headers=HEADERS_FOR_GET_REQ)
        soup_format = BeautifulSoup(response.content, 'html.parser')
        search_results = soup_format.find_all('div',
                                              {'class': 's-result-item', 'data-component-type': 's-search-result'})
        for listing in search_results:
            listing_counter += 1
            if listing_counter > listing_limit:
                break
            else:
                print(search_url)
                # db_table_row_data = [None, None, None, None, None]  # pseudocode
                # listing_data[0] = extract_product_name()
                # listing_data[1] = extract_product_rating()
                # listing_data[2] = extract_num_ratings()
                # listing_data[3] = extract_product_price()
                # listing_data[4] = extract_product_URL()
                # insert_values_into_db_table(db_cursor, 'table_name', tuple(listing_data))

                # product_name = listing.h2.text
                # print(product_name)
                extract_product_name(listing)
                extract_product_rating(listing)
                extract_num_ratings(listing)
                extract_product_price(listing)
                extract_product_URL(listing)
            url_results_page_param += 1  # this is not counting for some reason it stays on 1


def extract_product_name(listing):
    product_name = listing.h2.text
    print('product name: ', product_name)


def extract_product_rating(listing):
    rating_info = listing.find('i', {'class': 'a-icon'}).text
    print('product rating: ', rating_info)


def extract_num_ratings(listing):
    num_ratings = listing.find('span', {'class': 'a-size-base s-underline-text'}).text
    print('product num ratings: ', num_ratings)


def extract_product_price(listing):
    try:
        price_integer = listing.find('span', {'class': 'a-price-whole'}).text
        price_decimal = listing.find('span', {'class': 'a-price-fraction'}).text
        print('product price: ', price_integer + price_decimal)
    except AttributeError:
        print('No Price')


def extract_product_URL(listing):
    # needs some work
    try:
        product_url_segment = listing.h2.a['href']
        complete_product_url = 'https://amazon.com' + product_url_segment
        print('product URL: ', product_url_segment)
    except AttributeError:
        print('No Product URL')


def scrape_OverEarHeadphones(table_name, db_cursor):
    # this function should scrape the appropriate product listing
    # listing_counter = 0
    # listing_limit = 300
    # url_results_page_param = 1
    # while listing_counter < listing_limit:
    #     results_url_param = f'&page={url_results_page_param}'
    # query_terms = keywords.replace(' ', '+')
    # base_amazon_search_url = 'https://www.amazon.com/s?k=over+ear+headphones'
    # search_url = f'{base_amazon_search_url}{query_terms}{results_url_param}'
    # search_url += '&page=1'

    # get request
    # response = requests.get(search_url, headers=HEADERS_FOR_GET_REQ)
    # print('\n' + '>> search URL: ' + search_url + '\n')

    # for parsing the html code
    # soup_format = BeautifulSoup(response.content, 'html.parser')
    # search_results = soup_format.find_all('div',
    #                                       {'class': 's-result-item', 'data-component-type': 's-search-result'})
    for listing_block in search_results:
        listing_counter += 1
        if listing_counter > listing_limit:
            break
        else:
            # db_table_row_data = [null, null, null, null, null] # pseudocode
            # listing_data[0] = extract_product_name()
            # listing_data[1] = extract_product_rating()
            # listing_data[2] = extract_num_ratings()
            # listing_data[3] = extract_product_price()
            # listing_data[4] = extract_product_URL()
            # insert_values_into_db_table(db_cursor, 'table_name', tuple(listing_data))
            url_results_page_param += 1

        # PRODUCT NAME
        product_name = listing_block.h2.text
        print(product_name)

        # PRODUCT RATINGS (rating + num_ratings)
        try:
            rating = listing_block.find('i', {'class': 'a-icon'}).text
            print(rating)
            num_ratings = listing_block.find('span', {'class': 'a-size-base s-underline-text'}).text
            print(num_ratings)
        except AttributeError:
            print('No Ratings')

        # PRODUCT PRICE - (price REAL in database)
        try:
            price_integer = listing_block.find('span', {'class': 'a-price-whole'}).text
            price_decimal = listing_block.find('span', {'class': 'a-price-fraction'}).text
            price = price_integer + price_decimal
            print(price + '\n')
        except AttributeError:
            print('No Price')

        # PRODUCT URL
        try:
            product_url_segment = listing_block.h2.a['href']
            product_url = 'https://amazon.com' + product_url_segment
            print(product_url + '\n')
        except AttributeError:
            print('No Product URL')

        print()
        # not sure what to do here either
    for listing in search_results:
        listing_counter += 10
        if listing_counter > listing_limit:
            break

    #   not sure what i am doing here
    #   inserting all the records into the corresponding table ??
    if table_name == "Over_Ear_Headphones_Table":
        db_cursor.execute('''INSERT INTO Over_Ear_Headphones_Table VALUES(?, ?, ?, ?, ?)''',
                          listing_block.get('product_name', None),
                          listing_block.get('rating', None),
                          listing_block.get('num_ratings', None),
                          listing_block.get('price', None),
                          listing_block.get('product_url', None))
    if table_name is not None:
        db_cursor = main.insert_into_table(db_cursor, table_name, (
            listing_block.get('product_name', None),
            listing_block.get('rating', None),
            listing_block.get('num_ratings', None),
            listing_block.get('price', None),
            listing_block.get('product_url', None),))


def scrape_USBMicrophones():
    query_terms = keywords.replace(' ', '+')
    base_amazon_search_url = 'https://www.amazon.com/s?k=usb+microphones'
    search_url = f'{base_amazon_search_url}{query_terms}'
    search_url += '&page=1'
    response = requests.get(search_url, headers=HEADERS_FOR_GET_REQ)
    print('\n' + '>> search URL: ' + search_url + '\n')
    soup_format = BeautifulSoup(response.content, 'html.parser')
    search_results = soup_format.find_all('div', {'class': 's-result-item', 'data-component-type': 's-search-result'})
    for listing_block in search_results:
        # PRODUCT NAME
        product_name = listing_block.h2.text
        print(product_name)
        # adding the product name into the database

        # PRODUCT RATINGS
        try:
            rating_info = listing_block.find('i', {'class': 'a-icon'}).text
            print(rating_info)
            num_ratings = listing_block.find('span', {'class': 'a-size-base s-underline-text'}).text
            print(num_ratings)
        except AttributeError:
            print('No Ratings')

        # PRODUCT PRICE - (price REAL in database)
        try:
            price_integer = listing_block.find('span', {'class': 'a-price-whole'}).text
            price_decimal = listing_block.find('span', {'class': 'a-price-fraction'}).text
            price = price_integer + price_decimal
            print(price + '\n')
        except AttributeError:
            print('No Price')

        # PRODUCT URL
        try:
            product_url_segment = listing_block.h2.a['href']
            product_url = 'https://amazon.com' + product_url_segment
            print(product_url + '\n')
        except AttributeError:
            print('No Product URL')

        print()


def scrape_Webcams():
    query_terms = keywords.replace(' ', '+')
    base_amazon_search_url = 'https://www.amazon.com/s?k=1080p+Webcams'
    search_url = f'{base_amazon_search_url}{query_terms}'
    search_url += '&page=1'
    response = requests.get(search_url, headers=HEADERS_FOR_GET_REQ)
    print('\n' + '>> search URL: ' + search_url + '\n')
    soup_format = BeautifulSoup(response.content, 'html.parser')
    search_results = soup_format.find_all('div', {'class': 's-result-item', 'data-component-type': 's-search-result'})
    for listing_block in search_results:
        # PRODUCT NAME
        product_name = listing_block.h2.text
        print(product_name)
        # PRODUCT RATINGS
        try:
            rating_info = listing_block.find('i', {'class': 'a-icon'}).text
            print(rating_info)
            num_ratings = listing_block.find('span', {'class': 'a-size-base s-underline-text'}).text
            print(num_ratings)
        except AttributeError:
            print('No Ratings')

        # PRODUCT PRICE - (price REAL in database)
        try:
            price_integer = listing_block.find('span', {'class': 'a-price-whole'}).text
            price_decimal = listing_block.find('span', {'class': 'a-price-fraction'}).text
            price = price_integer + price_decimal
            print(price + '\n')
        except AttributeError:
            print('No Price')

        # PRODUCT URL
        try:
            product_url_segment = listing_block.h2.a['href']
            product_url = 'https://amazon.com' + product_url_segment
            print(product_url + '\n')
        except AttributeError:
            print('No Product URL')

        print()


def Capture_Cards():
    query_terms = keywords.replace(' ', '+')
    base_amazon_search_url = 'https://www.amazon.com/s?k=capture+cards'
    search_url = f'{base_amazon_search_url}{query_terms}'
    search_url += '&page=1'
    response = requests.get(search_url, headers=HEADERS_FOR_GET_REQ)
    print('\n' + '>> search URL: ' + search_url + '\n')
    soup_format = BeautifulSoup(response.content, 'html.parser')
    search_results = soup_format.find_all('div', {'class': 's-result-item', 'data-component-type': 's-search-result'})
    for listing_block in search_results:
        # PRODUCT NAME
        product_name = listing_block.h2.text
        print(product_name)
        # PRODUCT RATINGS
        try:
            rating_info = listing_block.find('i', {'class': 'a-icon'}).text
            print(rating_info)
            num_ratings = listing_block.find('span', {'class': 'a-size-base s-underline-text'}).text
            print(num_ratings)
        except AttributeError:
            print('No Ratings')

        # PRODUCT PRICE - (price REAL in database)
        try:
            price_integer = listing_block.find('span', {'class': 'a-price-whole'}).text
            price_decimal = listing_block.find('span', {'class': 'a-price-fraction'}).text
            price = price_integer + price_decimal
            print(price + '\n')
        except AttributeError:
            print('No Price')

        # PRODUCT URL
        try:
            product_url_segment = listing_block.h2.a['href']
            product_url = 'https://amazon.com' + product_url_segment
            print(product_url + '\n')
        except AttributeError:
            print('No Product URL')

        print()


def AudioMixers():
    query_terms = keywords.replace(' ', '+')
    base_amazon_search_url = 'https://www.amazon.com/s?k=8-channel+Audio+Mixers'
    search_url = f'{base_amazon_search_url}{query_terms}'
    search_url += '&page=1'
    response = requests.get(search_url, headers=HEADERS_FOR_GET_REQ)
    print('\n' + '>> search URL: ' + search_url + '\n')
    soup_format = BeautifulSoup(response.content, 'html.parser')
    search_results = soup_format.find_all('div', {'class': 's-result-item', 'data-component-type': 's-search-result'})
    for listing_block in search_results:
        # PRODUCT NAME
        product_name = listing_block.h2.text
        print(product_name)
        # PRODUCT RATINGS
        try:
            rating_info = listing_block.find('i', {'class': 'a-icon'}).text
            print(rating_info)
            num_ratings = listing_block.find('span', {'class': 'a-size-base s-underline-text'}).text
            print(num_ratings)
        except AttributeError:
            print('No Ratings')

        # PRODUCT PRICE - (price REAL in database)
        try:
            price_integer = listing_block.find('span', {'class': 'a-price-whole'}).text
            price_decimal = listing_block.find('span', {'class': 'a-price-fraction'}).text
            price = price_integer + price_decimal
            print(price + '\n')
        except AttributeError:
            print('No Price')

        # PRODUCT URL
        try:
            product_url_segment = listing_block.h2.a['href']
            product_url = 'https://amazon.com' + product_url_segment
            print(product_url + '\n')
        except AttributeError:
            print('No Product URL')

        print()


def GamingLaptops():
    query_terms = keywords.replace(' ', '+')
    base_amazon_search_url = 'https://www.amazon.com/s?k=gaming+laptops'
    search_url = f'{base_amazon_search_url}{query_terms}'
    search_url += '&page=1'
    response = requests.get(search_url, headers=HEADERS_FOR_GET_REQ)
    print('\n' + '>> search URL: ' + search_url + '\n')
    soup_format = BeautifulSoup(response.content, 'html.parser')
    search_results = soup_format.find_all('div', {'class': 's-result-item', 'data-component-type': 's-search-result'})
    for listing_block in search_results:
        # PRODUCT NAME
        product_name = listing_block.h2.text
        print(product_name)
        # PRODUCT RATINGS
        try:
            rating_info = listing_block.find('i', {'class': 'a-icon'}).text
            print(rating_info)
            num_ratings = listing_block.find('span', {'class': 'a-size-base s-underline-text'}).text
            print(num_ratings)
        except AttributeError:
            print('No Ratings')

        # PRODUCT PRICE - (price REAL in database)
        try:
            price_integer = listing_block.find('span', {'class': 'a-price-whole'}).text
            price_decimal = listing_block.find('span', {'class': 'a-price-fraction'}).text
            price = price_integer + price_decimal
            print(price + '\n')
        except AttributeError:
            print('No Price')

        # PRODUCT URL
        try:
            product_url_segment = listing_block.h2.a['href']
            product_url = 'https://amazon.com' + product_url_segment
            print(product_url + '\n')
        except AttributeError:
            print('No Product URL')
        print()
