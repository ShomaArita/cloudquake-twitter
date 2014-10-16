# -*- coding: utf-8 -*-

import json
import urllib2
import boto
import oauth2 as oauth

def streaming():
    global kinesis
    
    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''
    ACCESS_TOKEN_KEY = ''
    ACCESS_TOKEN_SECRET = ''
    consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth.Token(key=ACCESS_TOKEN_KEY, secret=ACCESS_TOKEN_SECRET)
    url = 'https://stream.twitter.com/1.1/statuses/filter.json?locations=-180,-90,180,90'
    params = {}
    request = oauth.Request.from_consumer_and_token(consumer, token, http_url=url, parameters=params)
    request.sign_request(oauth.SignatureMethod_HMAC_SHA1(), consumer, token)
    res = urllib2.urlopen(request.to_url())
    
    for r in res:
        try:
            data = json.loads(r)
            reply_text = data['text'].encode('utf_8').replace('\n', '')
            if reply_text.find("earthquake")!=-1 or\
                reply_text.find("Erdbeben")!=-1 or\
                reply_text.find("地震")!=-1:
                location = str(data['geo']['coordinates'])
                location = location.replace('[','')
                location = location.replace(']','')
                location = location.replace(' ','')
                location_str = location.split(',')
                time = str(data['created_at']).split(' ')
                send_data = {'year':time[5],'month':time[1],'date':time[2],'time':time[3],'longitude':location_str[1],'latitude':location_str[0]}
                send_json = json.dumps(send_data)
                print('2014-10-'+time[2]+'T'+time[3]+','+location_str[1]+','+location_str[0])
                f.write('2014-10-'+time[2]+'T'+time[3]+','+location_str[1]+','+location_str[0]+'\n')
                print(json.dumps(kinesis.put_record('TwitterStreamTest',send_json,'one'))+'\n')
        except:
            continue

if __name__ == '__main__':
    global kinesis
    f = open('data.csv','w')
    kinesis = boto.connect_kinesis(aws_access_key_id='',aws_secret_access_key='')
    streaming()
    f.close()