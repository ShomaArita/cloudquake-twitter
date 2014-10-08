# -*- coding: utf-8 -*-
 
import json
import urllib2
import oauth2 as oauth

def streaming():
 
	CONSUMER_KEY = '***************'
	CONSUMER_SECRET = '***************'
	ACCESS_TOKEN_KEY = '***************'
	ACCESS_TOKEN_SECRET = '***************'

	consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
	token = oauth.Token(key=ACCESS_TOKEN_KEY, secret=ACCESS_TOKEN_SECRET)
	# url = 'https://stream.twitter.com/1.1/statuses/filter.json?track=\u306F'
	url = 'https://stream.twitter.com/1.1/statuses/sample.json'
	params = {}

	request = oauth.Request.from_consumer_and_token(consumer, token, http_url=url, parameters=params)
	request.sign_request(oauth.SignatureMethod_HMAC_SHA1(), consumer, token)
	res = urllib2.urlopen(request.to_url())

	for r in res:
		try:
			data = json.loads(r)
			reply_id = str(data['id'])
			reply_text = data['text'].encode('utf_8').replace('\n', '')
			if 
			tweet_id = str(data['in_reply_to_status_id'])
			time = str(data['created_at'])
			f.write(time.replace(" ",",") + '\n')
			print(reply_id + '\t' +time+'\n' + reply_text + '\n\n')
		except:
			continue
			
if __name__ == '__main__':
	f = open('data.csv','w')
	streaming()
	f.close()