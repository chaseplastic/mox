
import pandas as pd #requires pandas
  	
df = pd.read_csv("~/Desktop/PresTweets1.csv", dayfirst=True, na_values=[" "]) #imports appropriate csv to dataframe

df['text'] = df['text'].str.strip('\n') #removes /n line break
df['text'] = df['text'].str.strip('\r') #removes /r line break

#deleteList = ([longitude,latitude,place_id,place_full_name,place_name,place_type,place_country_code,place_country,place_contained_within,place_attributes,place_bounding_box,source_url,truncated,entities,extended_entities,])

cleanTweets = df['text'].str.split(' ').apply(pd.Series, 1).fillna(' ') # creates df cleanTweets of just the words in 'text' and makes each word a new column
cleanTweets = "words::" + cleanTweets.astype(str) #appends string "words::" to the beginning of each datapoint in cleanTweets

# add categories column by column
handle = "handle::" + df.handle.astype(str)
retweet = "is_retweet::" + df.is_retweet.astype(str)
replySN = "in_reply_to_screen_name::" + df.in_reply_to_screen_name.astype(str)
isQuote = "is_quote_status::" + df.is_quote_status.astype(str)
rtCount = "retweet_count::" + df.retweet_count.astype(str)
favCount = "favorite_count::" + df.favorite_count.astype(str)
origAuth = "original_author::" + df.original_author.astype(str)

# deletes confusing or unnecessary columns
del df['original_author']
del df['id']
del df['handle']
del df['is_retweet']
del df['in_reply_to_screen_name']
del df['is_quote_status']
del df['retweet_count']
del df['favorite_count']

del df['text']
del df['in_reply_to_status_id']
del df['in_reply_to_user_id']
del df['lang']
del df['longitude']
del df['latitude']
del df['place_id']
del df['place_full_name']
del df['place_name']
del df['place_type']
del df['place_country_code']
del df['place_country']
del df['place_contained_within']
del df['place_attributes']
del df['place_bounding_box']
del df['source_url']
del df['truncated']
del df['entities']
del df['extended_entities']

result = pd.concat([df, handle, retweet, origAuth, replySN, isQuote, rtCount, favCount, cleanTweets], axis=1).fillna(' ') #brings series' and DF back together

print result


with open('newTweets.csv', 'a') as f:
    result.to_csv(f, header=None)
