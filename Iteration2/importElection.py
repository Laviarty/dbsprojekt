import pandas as pd
from sqlalchemy import create_engine

#Mit Datenbank verbinden:
engine = create_engine('postgresql://postgres:postgres@localhost:5432/Election')

#Csv einlesen:
reader = pd.read_csv('cleanedtweets.csv', sep=';',header=0,encoding='latin1')
frame = pd.DataFrame(reader)

frame.columns = ['tweet_id','account_name','inhalt','is_retweet','original_author', 'date', 'is_quote_status', 'retweet_count', 'favorite_count', 'source_url']

frame = frame.drop('tweet_id',axis=1, inplace=False)


#Tweet Table:
tweet = frame.drop(['account_name', 'original_author'] ,axis=1, inplace=False)
    
tweet.to_sql(name='tweet', con=engine,if_exists='replace')

#Account Table:
account = frame['account_name']
account.to_sql(name='account', con=engine,if_exists='replace')

#Twittert Table:
twittert = frame['account_name']
twittert.to_sql(name='twittert', con=engine,if_exists='replace')

#Retweetet Table:
retweetet = frame['account_name']
retweetet.to_sql(name='retweetet', con=engine,if_exists='replace')

#Die Tabellen enthält,hashtag und kommt_vor_mit bleiben vorerst leer, 
# da wir auf ein Problem gestoßen sind. Siehe Dokumentation.
