import pandas as pd
import re
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px
import plotly.figure_factory as ff
import streamlit as st


st.title(':violet[**--------------airbnb analysis--------------**]')
df = pd.read_csv(r"D:\Sudharsan\Guvi_Data science\DS101_Sudharsan\Mainboot camp\capstone project\airbnb analysis\listings.csv")

st.subheader(':green[**1.click here below to get airbnb data**]')
if (st.button(':red[click here]')):
    st.markdown("\n#### :orange[1.1 airbnb dataframe:]\n")
    st.write(df.head(4))

    st.markdown("\n#### :orange[1.2 number of data:]\n")
    st.info(len(df))
    
    st.markdown("\n#### :orange[1.3 airbnb geomap:]\n")
    columns = ['latitude','longitude']
    st.map(df)

#) to get the columns
#df.columns

#) check for first 10 columns and decide to drop the unnecessaries
#df[['id','listing_url','scrape_id','last_scraped','name','summary','space','description','experiences_offered','neighborhood_overview']]

#) removal of unnecessary columns in first 10 columns
df.drop(['listing_url','scrape_id','last_scraped','summary','space','description','experiences_offered','neighborhood_overview'],axis=1,inplace=True)

#) check second 10 columns and decide to drop the unnecessaries
#df[['notes','transit','thumbnail_url','medium_url','picture_url','xl_picture_url','host_id','host_url','host_name','host_since']]

#) removal of unnecessary columns in second 10 columns
df.drop(['notes','transit','thumbnail_url','medium_url','picture_url','xl_picture_url','host_id','host_url'],axis=1,inplace=True)


#) check third 10 columns and decide to drop the unnecessaries
#df[[ 'host_location', 'host_about','host_response_time', 'host_response_rate', 'host_acceptance_rate','host_is_superhost', 'host_thumbnail_url', 'host_picture_url','host_neighbourhood','host_listings_count']] 

#) removal of unnecessary columns in third 10 columns
df.drop([ 'host_location', 'host_about','host_is_superhost'],axis=1,inplace=True)

#) removal of unnecessary columns in third 10 columns
df.drop([ 'host_thumbnail_url','host_picture_url'],axis=1,inplace=True)

#) check fourth 10 columns and decide to drop the unnecessaries
#df[['host_verifications', 'host_has_profile_pic', 'host_identity_verified','street', 'neighbourhood', 'neighbourhood_cleansed','neighbourhood_group_cleansed','city', 'state', 'zipcode']]

#) check fourth 10 columns and decide to drop the unnecessaries
df.drop(['host_verifications', 'host_has_profile_pic', 'host_identity_verified','street'],axis=1,inplace=True)

#) to check fifth 10 columns
#df[['market', 'smart_location', 'country_code','country', 'latitude', 'longitude', 'is_location_exact','property_type', 'room_type', 'accommodates']]

#) check fourth 10 columns and decide to drop the unnecessaries
df.drop(['is_location_exact'],axis=1,inplace=True)

#) to check fifth 13 columns
#df[['bathrooms', 'bedrooms', 'beds', 'bed_type','amenities', 'square_feet', 'price', 'weekly_price', 'monthly_price',
#    'security_deposit', 'cleaning_fee', 'guests_included', 'extra_people']]

#) next 16 columns
#df[['minimum_nights', 'maximum_nights', 'calendar_updated','has_availability', 'availability_30', 'availability_60',
#    'availability_90', 'availability_365', 'calendar_last_scraped','number_of_reviews', 'first_review', 'last_review',
#    'review_scores_rating', 'review_scores_accuracy','review_scores_cleanliness', 'review_scores_checkin']]

#) drop unnecessary columns 
#df.drop(['calendar_updated','has_availability','calendar_last_scraped'],axis=1,inplace=True)

#) to check the unnecessary columns in the last columns
#df[['review_scores_communication', 'review_scores_location','review_scores_value', 'requires_license', 'license',
#    'jurisdiction_names', 'instant_bookable', 'cancellation_policy','require_guest_profile_picture', 
#    'require_guest_phone_verification','calculated_host_listings_count', 'reviews_per_month']]

#) to check the unique in a column
#df['name'].unique()

#) to count na
#df.isna().sum()

#)fill the null values
temp_df = df.ffill()
temp_df = df.bfill()


#) to check the null value after ffill and bfill
#temp_df.isna().sum()

#temp_df.columns

#temp_df['city'].unique()

#temp_df['country'].unique()

#temp_df['price']

#) removing $ symbol from price column
list_price = temp_df['price'].tolist() #) converting item_date column into list
price_string = map(str, list_price)
list_price_string = list(price_string)

new_price_list = []
for num in list_price:
       price = re.findall(r'\d+\.\d+', num)
       converted = float(price[0])
       new_price_list.append(converted)
#new_price_list

#) converting list into column
temp_df['new_price'] = new_price_list


#) removal of $ symbol drom extra_people column
import re
list_epeople = temp_df['extra_people'].tolist() #) converting item_date column into list
epeople_string = map(str, list_epeople)
list_epeople_string = list(epeople_string)

new_epeople_list = []

for num in list_epeople:
       epeople = re.findall(r'\d+\.\d+', num)
       converted = float(epeople[0])
       new_epeople_list.append(converted)
#new_epeople_list

temp_df['new_epeople'] = new_epeople_list


#) to check data type of new columns
datatypes = temp_df.dtypes
#datatypes

#df['weekly_price']

#) to check nan values in weekly_price column
#temp_df['weekly_price'].isna().sum()

#) to check nan values in monthly_price column
#temp_df['monthly_price'].isna().sum()


#temp_df['weekly_price'].isna()

#temp_df['monthly_price'].isna()

#) deleting non value in weekly_price column and monthly_column
temp_df.drop([3813,3814,3815,3816,3817],axis=0,inplace=True)

#temp_df['monthly_price'].isna().sum()

#)removal of $ symbol drom weekly price
list_wprice = temp_df['weekly_price'].tolist()
wprice_string = map(str, list_wprice)
list_wprice_string = list(wprice_string)

new_wprice_list = []

for num in list_wprice_string:
       wprice = re.findall(r'\d+\.\d+', num)
       converted = float(wprice[0])
       new_wprice_list.append(converted)
#new_wprice_list

temp_df['new_wprice'] = new_wprice_list


#)removal of $ symbol drom monthly price
list_mprice = temp_df['monthly_price'].tolist()
mprice_string = map(str, list_mprice)
list_mprice_string = list(mprice_string)

new_mprice_list = []

for num in list_mprice_string:
       mprice = re.findall(r'\d+\.\d+', num)
       converted = float(mprice[0])
       new_mprice_list.append(converted)
#ew_mprice_list

temp_df['new_mprice'] = new_mprice_list


#)removal of % symbol from host_response column
res_list = temp_df['host_response_rate'].tolist()
res_string = map(str, res_list)
list_res_string = list(res_string)

index = 0
list_res_new = []

while index < len(list_res_string):
    percent = list_res_string[index]
    #) to pick up year
    num = percent[:-1]
    list_res_new.append(num)
    index+=1
#list_res_new
temp_df['new_hresponse'] = list_res_new


st.subheader(':green[**2.Data Visualization**]')
RadioButton = st.radio('Select the chart: ',('2.1 altair chart',
                                             '2.2 line chart',
                                             '2.3 area chart',
                                             '2.4 piechart',
                                             '2.5 histogram'))

if RadioButton == '2.1 altair chart':
      # altair scatter plot
      st.markdown("\n#### :orange[2.1 (a) altair chart:]\n")
      chart = alt.Chart(temp_df).mark_circle().encode(x = 'beds', y = 'new_price', size = 'bathrooms',
                                                      tooltip =  ['beds','new_price','bathrooms'])
      st.altair_chart(chart)

      st.markdown("\n#### :orange[2.1 (b) insights:]\n")
      st.markdown(':blue[- mostly 2 - 5 beds are used]')
      st.markdown(':blue[- mostly 4 bathrooms are preferred]')

elif RadioButton == '2.2 line chart':
    #) 2.2 line chart
    st.markdown("\n#### :orange[2.2(a) line chart:]\n")
    airbnb_list = temp_df.columns.tolist()
    airbnb_criteria = st.multiselect('choose airbnb criteria',airbnb_list)
    new_df = temp_df[airbnb_criteria]
    st.line_chart(new_df)

    st.markdown("\n#### :orange[2.2(b) insights:]\n")
    st.markdown(':blue[- mostly 2 - 6 accomodates preferred]')

elif RadioButton == '2.3 area chart':
     #) 2.3 area chart
     st.subheader(":orange[2.3(a) area chart]")
     airbnb_list = temp_df.columns.tolist()
     airbnb_criteria = st.multiselect('choose airbnb criteria',airbnb_list)
     new_df = temp_df[airbnb_criteria]
     st.area_chart(new_df)

     st.markdown("\n#### :orange[2.3(b) insights:]\n")
     st.markdown(':blue[- less than 1500 square ft of area are preferred]')

elif RadioButton == '2.4 piechart':
    #) 2.4 pie chart
    st.markdown("\n#### :orange[2.4(a) piechart:]\n")
    fig = px.pie(temp_df, values = 'new_price', names = 'room_type')
    st.plotly_chart(fig)

    st.markdown("\n#### :orange[2.4(b) insights:]\n")
    st.markdown(':blue[- mostly entire home/apt are preferred over sharing, private rooms]')

elif RadioButton == '2.5 histogram':
    #) 2.5 histogram
    st.markdown("\n#### :orange[2.5(a) histogram:]\n")
    #) converting list to array
    list_reviews = temp_df['number_of_reviews'].tolist()
    np_reviews = np.array(list_reviews)
    np_nprice = np.array(new_price_list)
    hist_data = [np_reviews,np_nprice]
    group_labels = ['number_of_reviews', 'price']
    fig = ff.create_distplot(hist_data, group_labels, bin_size=[.1,.25,.5])
    st.plotly_chart(fig)

    st.markdown("\n#### :orange[2.5(b) insights:]\n")
    st.markdown(':blue[- number of reviews are low which is independent of price]')
