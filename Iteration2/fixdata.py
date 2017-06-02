import pandas as pd

#Einlesen der .csv Datei:
reader = pd.read_csv('american-election-tweets.csv', sep=';',header=0)

#Erstellen eines Data Frames:
frame = pd.DataFrame(reader)

#Suche nach Duplicaten:
frame = frame.drop_duplicates(subset=None, keep='first',inplace=False)

#Suche nach NULL Values:
frame = frame.dropna(subset=['handle','text','is_retweet','time'])

#Unnötige Spalten löschen:
frame = frame.drop(['truncated', 'in_reply_to_screen_name'] ,axis=1, inplace=False)
#frame = frame.drop([0])


#Umbenennen der Spalten in die der Datenbank:
frame.columns = ['account_name','inhalt','is_retweet','original_author', 'date', 'is_quote_status', 'retweet_count', 'favorite_count', 'source_url']

#Ausgabe in Datei:
frame.to_csv('cleanedtweets.csv', sep=';')
        