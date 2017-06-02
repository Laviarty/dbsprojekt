CREATE TABLE tweet(
	index INTEGER,
	--tweet_id INTEGER,
	inhalt VARCHAR NOT NULL,
	is_retweet BOOLEAN NOT NULL,
	"date" VARCHAR NOT NULL,
	is_quote_status BOOLEAN NOT NULL,
	retweet_count INTEGER NOT NULL,
	favorite_count INTEGER NOT NULL,
	source_url VARCHAR NOT NULL,
	PRIMARY KEY(index)
);
	
CREATE TABLE twittert (
	index INTEGER,
	--tweet_id INTEGER,
	account_name VARCHAR NOT NULL,
    PRIMARY KEY (index)
);
	
CREATE TABLE retweetet (
	index INTEGER,
	--tweet_id INTEGER,
	account_name VARCHAR NOT NULL,
    PRIMARY KEY (index) 
);

CREATE TABLE enthält (
	index INTEGER,
	--tweet_id INTEGER,
    "text" VARCHAR NOT NULL,
    PRIMARY KEY ("text")
);
	
CREATE TABLE kommt_vor_mit (
	index INTEGER,
	--tweet_id INTEGER,
	"text" VARCHAR NOT NULL,
	anzahl INTEGER,
	PRIMARY KEY ("text")
);

CREATE TABLE account (
	index INTEGER,
	--tweet_id INTEGER,
	account_name VARCHAR NOT NULL,
    PRIMARY KEY (index)
);

CREATE TABLE hashtag (
	index INTEGER,
	---tweet_id INTEGER,
	"date" VARCHAR,
    "text" VARCHAR NOT NULL,
	PRIMARY KEY ("text")
);