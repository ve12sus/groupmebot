import requests, re

def getLink(messages, name=None):
    for message in messages:
        b = "(?P<url>https?://[^\s]+)"
        p = re.compile(b)
        m = p.match(message['text'])
        if (m and name):
            if (message['sender_id'] != '393017' and 
                    message['name'] == name):
                botpost(m.group())
            else:
                pass
        elif (m and message['sender_id'] != '393017'):
            botpost(m.group())
        else:
            pass

def getMessages(before_id=None):
    token = 'NB3oRIaPWEUXwJL0cQxOMF32P57eUs4yYfVIIeaT'
    msg_api = 'https://api.groupme.com/v3/groups/31129835/messages?token='
    if before_id:
        r = requests.get(msg_api + token + '&before_id=' + before_id)
        return r
    else:
        r = requests.get(msg_api + token + '&limit=100')
        return r
        
def botpost(text):
    payload = {"bot_id" : "f9b366898c181f1f3ef76da9f6",
               "text" : ""}
    payload['text'] = text
    r = requests.post('https://api.groupme.com/v3/bots/post', data=payload)

def get_before_id(messages):
    return messages[19]['id']

def paging(pages, name=None):
    before_id = None
    for i in range(pages):
        response = getMessages(before_id)
        thestuff = response.json()
        messages = thestuff['response']['messages']
        if name:
            getLink(messages, name)
        else:
            getLink(messages)
        before_id = get_before_id(messages)

def captureName(saying):                                                        
    b = "@(.*)"                                                                
    p = re.compile(b)                                                           
    m = p.search(saying)                                                        
    return m.group()[1:]
