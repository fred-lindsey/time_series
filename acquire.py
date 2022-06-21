

import pandas as pd
import requests

#___________________________________________________________________________________________________________________
def get_sales_df():

    #create empty list to store the pages
    sales = []

    #set the domain an endpoint
    domain = 'https://python.zgulde.net'
    endpoint = '/api/v1/sales'

    # the url is the combination of domain and endpoint
    url = domain + endpoint

    #set the function parameters
    response = requests.get(url)
    data = response.json()

    # define the pages in the api
    current_page = data['payload']['page']
    next_page = data['payload']['next_page']
    max_page = data['payload']['max_page']

    # write a loop to run through 1: max page range
    for page in range (1, (max_page)):

        url_endpoint = data['payload']['next_page'] #use next page
        url = domain + url_endpoint

        # update the response to use the api next page to progress the script
        response = requests.get(url)
        data = response.json()

        # update the complete_sales_df to include the additional list items
        sales.extend(data['payload']['sales'])

        # check page progress with print statement
        print(f'\rFetching page {page} of {max_page} {url}', end='')

    # return the full dataframe
    return pd.DataFrame(sales)

#___________________________________________________________________________________________________________________
def get_items_df():

    #create empty list to store the pages
    items = []

    #set the domain an endpoint
    domain = 'https://python.zgulde.net'
    endpoint = '/api/v1/items'

    # the url is the combination of domain and endpoint
    url = domain + endpoint

    #set the function parameters
    response = requests.get(url)
    data = response.json()

    # define the pages in the api
    current_page = data['payload']['page']
    next_page = data['payload']['next_page']
    max_page = data['payload']['max_page']

    # write a loop to run through 1: max page range
    for page in range (1, (max_page)):

        endpoint = data['payload']['next_page'] #use next page
        url = domain + endpoint

        # update the response to use the api next page to progress the script
        response = requests.get(url)
        data = response.json()

        # update the complete_sales_df to include a concat of the additional dataframe
        items.extend(data['payload']['items'])

        # check page progress with print statement
        print(f'\rFetching page {page} of {max_page} {url}', end='')

    # return the full dataframe
    return pd.DataFrame(items)

#___________________________________________________________________________________________________________________

def get_stores_df():

    #create empty list to store the pages
    stores = []

    #set the domain an endpoint
    domain = 'https://python.zgulde.net'
    endpoint = '/api/v1/stores'

    # the url is the combination of domain and endpoint
    url = domain + endpoint

    #set the function parameters
    response = requests.get(url)
    data = response.json()

    # define the pages in the api
    current_page = data['payload']['page']
    next_page = data['payload']['next_page']
    max_page = data['payload']['max_page']
    print(max_page)

    # set URL:
    url = domain + endpoint

    # update the complete_sales_df to include a concat of the additional dataframe
    stores.extend(data['payload']['stores'])

    # check page progress with print statement
    print(f'\rFetching page {current_page} of {max_page} {url}', end='')

    # return the full dataframe
    return pd.DataFrame(stores)