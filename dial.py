import requests, re

def dial():
    token = 'NB3oRIaPWEUXwJL0cQxOMF32P57eUs4yYfVIIeaT'
    r = requests.get('https://api.groupme.com/v3/groups/31129835/messages?token='
                    + token)

    thestuff = r.json()

    messages = thestuff['response']['messages']
    print len(messages)
    print messages[19]['id']
    for message in messages:
        print message['text']
        b = "(?P<url>https?://[^\s]+)"
        p = re.compile(b)
        m = p.match(message['text'])
        if m:
            print 'match found', m.group()
        else:
            print 'no matches'

def getLink(messsages):
    for message in messages:
        b = "(?P<url>https?://[^\s]+)"
        p = re.compile(b)
        m = p.match(message['text'])
        if m:
            botpost(meessage['text'])
        else:
            continue

def getMessages(before_id=None):
    token = 'NB3oRIaPWEUXwJL0cQxOMF32P57eUs4yYfVIIeaT'
    msg_api = 'https://api.groupme.com/v3/groups/31129835/messages?token='
    if before_id:
        r = requests.get(msg_api + token + '&before_id=' + before_id)
        print r.json()
    else:
        r = requests.get(msg_api + token)
        print r.json()
        
def botpost(text):
    payload = {"bot_id" : "f9b366898c181f1f3ef76da9f6",
               "text" : ""}
    payload['text'] = text
    r = requests.post('https://api.groupme.com/v3/bots/post', data=payload)

def paging(before_id):
    r = requsts.get('https://api.groupme.com/v3/groups/31129835/messages?token='+
            token + '&before_id=' + before_id)
