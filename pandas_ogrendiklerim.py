# Pandas Learning Materials with using Kaggle's Wine Review DataSet

import pandas as pd

reviews = pd.read_csv("/Users/emrebasaran/Desktop/archive/winemag-data-130k-v2.csv")

#Describe function like behave summary function in R
#print(reviews.taster_name.describe())

#Unique function show a list of unique values at the dataset
#print(reviews.taster_name.unique())

# value_counts() function show the unqiue values and how they often occur in the dataset
#print(reviews.country.value_counts())

#For a function that takes one set of values and "maps" them to another set of values. 
#In data science we often have a need for creating new representations from  existing data, 
#or for transforming data from the format it is in now to the format that we want it to be in later.

#There are two mapping methods that you will use often.

#review_points_mean = reviews.points.mean()
#print(reviews.points.map(lambda p: p - review_points_mean))

# review_points_mean = reviews.points.mean()
# def remean_points(row):
#     row.points = row.points - review_points_mean
#     return row
# print(reviews.apply(remean_points, axis='columns'))

#What is the median of the points column in the reviews DataFrame?
# print(reviews.points.mean())

# What countries are represented in the dataset? (Your answer should not include any duplicates.)
# print(reviews.country.unique())

# How often does each country appear in the dataset? Create a Series reviews_per_country mapping countries to the count of reviews of wines from that country.
# print(reviews.country.value_counts())

# Create variable centered_price containing a version of the price column with the mean price subtracted.
# centered_price = reviews.price.map(lambda p: p - reviews.price.mean())

#I'm an economical wine buyer. Which wine is the "best bargain"? 
#Create a variable bargain_wine with the title of the wine with the highest points-to-price ratio in the dataset.
# bargain_wine = reviews.loc[(reviews.points / reviews.price).idxmax(), 'title']

# There are only so many words you can use when describing a bottle of wine. 
# Is a wine more likely to be "tropical" or "fruity"? 
# Create a Series descriptor_counts counting how many times each of these two words 
# appears in the description column in the dataset.
# tropically = reviews.description.map(lambda p: 'tropical' in p).sum()
# fruityly = reviews.description.map(lambda p: 'fruity' in p).sum()
# descriptor_counts = pd.Series([tropically,fruityly], index = ['tropical','fruity']) 
# print(descriptor_counts)

# We'd like to host these wine reviews on our website, but a rating system ranging from 80 to 100 points is too hard to understand 
# We'd like to translate them into simple star ratings. 
# A score of 95 or higher counts as 3 stars, a score of at least 85 but less than 95 is 2 stars. Any other score is 1 star.
# Also, the Canadian Vintners Association bought a lot of ads on the site, so any wines from 
# Canada should automatically get 3 stars, regardless of points.
# Create a series star_ratings with the number of stars corresponding to each review in the dataset.

# def stars(row):
#     if row.points >= 95:
#         return 3
#     elif row.points >= 85:
#         return 2
#     elif row.country == 'Canada':
#         return 3
#     else:
#         return 1

# star_rating = reviews.apply(stars, axis = 'columns' )  

######################
# GROUPING & SORTING #
######################

#Hangi point değerinden kaç tane var bulmak istiyorsak:
# print(reviews.groupby('points').points.count())
#Her point değerine ait şaraplar içerisinde en ucuz şarap fiyatı
# print(reviews.groupby('points').price.min())
# Şarap adlandırması yaparken üretici ile title eşlemesi yapma
# print(reviews.groupby('winery').apply(lambda df: df.title.iloc[0]))

# For even more fine-grained control, you can also group by more than one column. 
# For an example, here's how we would pick out the best wine by country and province:
# print(reviews.groupby(['country','province']).apply(lambda df: df.loc[df.points.idxmax()]))

#Eğer birden çok sonksiyonu tek seferde kullanmak istiyorsak, agg ile gruplayabiliririz
#sort_values(by='fonksiyon') ile ilgili fonksiyona göre sıralama yapılabilir.
#ascending ile de True dediğimizde küçükten büyüğe, tersinde tersi şeklinde sıralanbilir.
# print(reviews.groupby(['country']).price.agg([len,min,max,sum]).sort_values(by='sum',ascending=False))

#Dataset'deki en yaygın reviewers?
# print(reviews.groupby('taster_twitter_handle').size().sort_values(ascending=False))

# Her bir fiyat değeri için en yüksek puanlı şarabın puanı kaçtır?
# print(reviews.groupby('price')['points'].max().sort_index())

#Her bir variety için maximum ve minimum fiyat nedir?
# print(reviews.groupby('variety').price.agg([min,max]))
# print(reviews.groupby('variety').price.agg([min,max]).sort_values(by=['min','max'], ascending =False))

# Tasterların tattıkları şarapların ortalama puanı?
# print(reviews.groupby('taster_name').points.mean())

#Tasterların tattıkları şarapların ortalamaları arasında belirgin farklar var mı?
# print(reviews.groupby('taster_name').points.mean().describe())

#Lan acaba öküzgözü var mı?
# print((reviews[reviews.country == 'Turkey'].variety == 'Okuzgozu').sum())
#Şu şarapları şöyle bir ucuzdan pahalıya doğru sıralayalım da adıyla, puanıyla, parasıyla falan lazım olur
# a= reviews[reviews.country == 'Turkey'].sort_values(by='price')[['title', 'variety', 'points','price']]

#### MISSING DATA ####

#Entries missing values are given the value NaN, short for "Not a Number". For technical reasons these NaN values are always of the float64 dtype.
#Pandas provides some methods specific to missing data. To select NaN entries you can use pd.isnull() (or its companion pd.notnull()). 
#This is meant to be used thusly:
# print(reviews[pd.isnull(reviews.country)])

#Replacing missing values is a common operation. Pandas provides a really handy method for this problem: fillna(). 
#fillna() provides a few different strategies for mitigating such data. For example, we can simply replace each NaN with an "Unknown":
# print(reviews.region_2.fillna('Unknown'))

#Alternatively, we may have a non-null value that we would like to replace. For example, suppose that since this dataset was published, 
#reviewer Kerin O'Keefe has changed her Twitter handle from @kerinokeefe to @kerino. One way to reflect this in the dataset is using the replace() method:
# print(reviews.taster_twitter_handle.replace('@kerinokeefe', '@kerino'))

