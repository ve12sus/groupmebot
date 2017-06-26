import json, re, requests

def parse(req_data):
    text = req_data['text']
    if re.match(r'/likes', text):
        botpost("You said likes.")
        name = captureName(text)
        if name:
            getLikes(name)
        else:
            botpost("you didn't enter a name")

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
    botpost(name)
#    before_id = Noe
#    likes = {}
#    for i in range(pages):
#        response = getMessages(before_id)
#        thestuff = response.json()
#        messages = thestuff['response']['messages']
#        for message in messages:
#            if message['name'] == name and message['favorited_by']:
#                for user_id in message['favorited_by']:
#                    default = 'no name'
#                    if likes.get(user_id, default) == 'no name':
#                        likes[user_id] = 1
#                    else:
#                        likes[user_id] += 1
#            else:
#                pass
#        before_id = get_before_id(messages)
#    if person = keywithmaxval(likes):
#        response = getGroupMembers()
#        thestuff = response.json()
#        members = thestuff['response']['members']
#        for member in members:
#            if member['user_id'] == person:
#                botpost(name + ' was most liked by ' + member['nickname'])
#    else:
#        botpost('No one likes ' + name)
    
def getGroupMembers():
    token = 'NB3oRIaPWEUXwJL0cQxOMF32P57eUs4yYfVIIeaT'
    group_api = 'https://api.groupme.com/v3/groups/22856815?token='
    r = requests.get(group_api + token)
    return r

def getMessages(before_id=None):
    token = 'NB3oRIaPWEUXwJL0cQxOMF32P57eUs4yYfVIIeaT'
    msg_api = 'https://api.groupme.com/v3/groups/22856815/messages?token='
    if before_id:
        r = requests.get(msg_api + token + '&before_id=' + before_id + 
                '&limit=100')
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

def captureName(text):                                                        
    b = "@(.*)"                                                                
    p = re.compile(b)                                                           
    m = p.search(text)                                                        
    return m.group()[1:]

def keywithmaxval(d):
    """ a) create a list of the dict's keys and values; 
        b) return the key with the max value"""  
    v=list(d.values())
    k=list(d.keys())
    return k[v.index(max(v))]
