# Time Series: Data Acquisition Exercises

#Function for Exercise #1
#------------------------
# 1. Using the code from the lesson as a guide
# and the REST API from https://python.zgulde.net/api/v1/items as we did in the lesson, 
# #create a dataframe named items that has all of the data for items.

#This function acquires data from a REST API at the url above and returns a dataframe containing all the items

def get_items():

    import pandas as pd
    import requests  

    # Define base url to obtain api from
    url= 'https://python.zgulde.net'

    # create response containing the contents of the response from the api
    response = requests.get(url + '/api/v1/items')

    #Turn that .json content into a dictionary for use with Python
    data = response.json()

    #Create a dataframe containing the dictionary created from the .json sent by the api
    df_items = pd.DataFrame(data['payload']['items'])

    return df_items


#Function for Exercise #2
#------------------------
# 2. Do the same thing as #1, but for stores (https://python.zgulde.net/api/v1/stores)

#This function acquires data from a REST API at the url above and returns a dataframe containing all the stores

def get_stores():

    import pandas as pd
    import requests  

    # Define base url to obtain api from
    url= 'https://python.zgulde.net'

    # create response containing the stores from the api
    response_stores = requests.get(url + '/api/v1/stores')

    #Turn that .json content into a dictionary for use with Python
    data_stores = response_stores.json()

    #Create a dataframe containing the dictionary created from the .json sent by the api
    df_stores = pd.DataFrame(data_stores['payload']['stores'])

    return df_stores

#Function for Exercise #3
#------------------------
# 2. Extract the data for sales (https://python.zgulde.net/api/v1/sales). 
# There are a lot of pages of data here, so your code will need to be a little more complex. 
# Your code should continue fetching data from the next page until all of the data is extracted. 

#This function acquires data from a REST API at the url above and returns a dataframe containing all the sales

def get_sales():

    import pandas as pd
    import requests  

    # Define base url to obtain api from
    url= 'https://python.zgulde.net'

    #Iterating thru every page and concatenating the sales info from each page, we create a loop

    #acquire .json from url
    response_sales = requests.get(url + '/api/v1/sales')

    #turn .json content into dictionary
    data_sales = response_sales.json()

    #turn dictionary into a dataframe
    df_sales = pd.DataFrame(data_sales['payload']['sales'])

    #Get ready to iterate thru all pages 
    num_pages = data_sales['payload']['max_page']

    # loop thru the iterations
    for i in range(1,num_pages):

        response_sales = requests.get(url + data_sales['payload']['next_page'])
        data_sales = response_sales.json()
        df_sales = pd.concat([df_sales, pd.DataFrame(data_sales['payload']['sales'])])

    return df_sales    
 

#Function for Exercise #4
#------------------------
#4. Save the data in your files to local csv files so that it will be faster to access in the future.

#This function calls the get_sales function and creates a .csv with sales data and saves it locally
def create_sales_data_csv():

    df_sales = get_sales()

    #create a csv from sales data and store locally
    df_sales.to_csv('sales.csv')


#Function for Exercise #5
#------------------------
# Combine the data from your three separate dataframes into one large dataframe.

#This function calls 3 functions that get sales, stores, and items and concatenates and returns all the data in one dataframe

def combine_sales_stores_items_data():

    import pandas as pd

    df_sales = get_sales()
    df_stores = get_stores()
    df_items = get_items()

    df_sales_and_stores = pd.merge(df_sales, df_stores, how='left', left_on='store' , right_on='store_id')

    df_all = pd.merge(df_sales_and_stores, df_items, how='left', left_on='item', right_on='item_id')

    return df_all


#Function for Exercise #6
#------------------------
#This function reads data from a link to a .csv file and returns a dataframe

def csv_to_df(url):

    import pandas as pd

    df_from_csv = pd.read_csv(url)

    return df_from_csv

