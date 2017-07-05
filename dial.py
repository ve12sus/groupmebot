import json, re, requests, pprint

def parse(req_data):
    text = req_data['text']
    if re.match(r'/likes', text):
#        botpost("You said likes.")
        name = captureName(text)
        if name:
            getLikes(name)
        else:
            botpost("incorrect username")

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

def getLikes(name):
    likes = {}
#    for i in range(3):
    response = getMessages()
    thestuff = response.json()
#    pp = pprint.PrettyPrinter(indent=4)
#    pp.pprint(thestuff['response']['messages'])
    messages = thestuff['response']['messages']
    for message in messages:
        print message['name']
        if message['name'] == name and len(message['favorited_by']) != 0:
            print message['favorited_by']
            for user_id in message['favorited_by']:
                if user_id in likes:
                    likes[user_id] += 1
                else:
                    likes[user_id] = 1
        else:
            print 'no'
    pp.pprint(likes)
    try:
        person = keywithmaxval(likes)
        members = getGroupMembers()
        for member in members:
            if member['user_id'] == person:
                botpost(member['nickname'] + ' liked ' + name +
                        ' the most.(Last 100 messages)')
    except ValueError:
        botpost('nobody liked ' + name + ' =/')
    
def getGroupMembers():
    token = 'NB3oRIaPWEUXwJL0cQxOMF32P57eUs4yYfVIIeaT'
    group_api = 'https://api.groupme.com/v3/groups/22856815?token='
    r = requests.get(group_api + token)
    pp = pprint.PrettyPrinter(indent=4)
    thestuff = r.json()
    return thestuff['response']['members']

def getMessages():
    token = 'NB3oRIaPWEUXwJL0cQxOMF32P57eUs4yYfVIIeaT'
    msg_api = 'https://api.groupme.com/v3/groups/22856815/messages?token='
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

def captureName(text):                                                        
    b = "@(.*)"                                                                
    p = re.compile(b)                                                           
    m = p.search(text)                                                        
    if m:
        return m.group()[1:]
    else:
        return None

def keywithmaxval(d):
    """ a) create a list of the dict's keys and values; 
        b) return the key with the max value"""  
    v=list(d.values())
    k=list(d.keys())
    return k[v.index(max(v))]
