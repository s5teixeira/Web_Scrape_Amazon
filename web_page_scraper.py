import requests
from bs4 import BeautifulSoup
import main

# this module is for all the products we need to scrape

HEADERS_FOR_GET_REQ = (
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
     'Accept-Language': 'en-US, en;q=0.5'}
)


def write_to_file(x):
    with open("output_data.txt", "a") as data_out_file:
        try:
            data_out_file.write(f'\n{x}\n\n')
        except UnicodeEncodeError:
            data_out_file.write(f"\nUnicodeEncodeError\n\n")


def get_search_url(db_cursor, table_name, keywords):
    # this function creates the url using the given keywords ex: 'over ear headphones'
    listing_counter = 0
    listing_limit = 300  # <--- the number of times this function will run after being called once supposed to be 300
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

                name = extract_product_name(listing)
                rating = extract_product_rating(listing)
                num_ratings = extract_num_ratings(listing)
                price = extract_product_price(listing)
                product_url = extract_product_URL(listing, search_url)
                main.insert_into_table(db_cursor, table_name, (name, rating, num_ratings, price, product_url))
                # for record in search_results:
                #     main.insert_into_table(name, rating, num_ratings, price, product_url)
        # print(search_url)
        url_results_page_param += 1  # this is not counting for some reason it stays on 1


def extract_product_name(listing):
    product_name = listing.h2.text
    # print('product name: ', product_name)
    write_to_file(product_name)
    return product_name


def extract_product_rating(listing):
    rating_listing = listing.find('i', {'class': 'a-icon'})

    if rating_listing:
        rating_info = rating_listing.text
    else:
        rating_info = 'N/A'

    # print('product rating: ', rating_info)
    write_to_file(rating_info)

    return rating_info


def extract_num_ratings(listing):
    try:
        num_ratings = listing.find('span', {'class': 'a-size-base s-underline-text'}).text
        # print('product num ratings: ', num_ratings)
        write_to_file(num_ratings)
    except AttributeError:
        num_ratings = '0'
    return num_ratings


def extract_product_price(listing):
    try:
        price_integer = listing.find('span', {'class': 'a-price-whole'}).text
        price_decimal = listing.find('span', {'class': 'a-price-fraction'}).text
        # print('product price: $', price_integer + price_decimal)
        write_to_file('$' + price_integer + price_decimal)
        return price_integer + price_decimal
    except AttributeError:
        return 0

def extract_product_URL(listing, search_url):
    try:
        product_url_segment = listing.h2.a['href']
        complete_product_url = 'https://amazon.com' + product_url_segment
        # print('product URL: ', complete_product_url)
        write_to_file(complete_product_url)
        return complete_product_url
    except AttributeError:
        return 0
