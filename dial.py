import json, re, requests

def parse(req_data):
    text = req_data['text']
    attachmentType = req_data['attachments']['type']
    if re.match(r'/likes', text):
       user_id = getMentionId(req_data['attachments']['type'])
       getLikes(user_id)

def getMentionId(attachmentType):
    if attachmentType == 'mentions':
        user_id = attachmentType['user_ids'][0]
        return user_id

def getLikes(id_liked):
    likes = {}
    messages = getMessages()
    for message in messages:
        if message['user_id'] == id_liked and len(message['favorited_by']) != 0:
            for user_id in message['favorited_by']:
                if user_id in likes:
                    likes[user_id] += 1
                else:
                    likes[user_id] = 1
        else:
            pass

    if len(likes) > 0 :
        likes_list = getMaxLikes(likes)
        members = getGroupMembers()
        member_ids = getMemberids(members)
        results = frozenset(likes_list).intersection(member_ids)
        names = convertNames(results)
        if len(names) == 0:
            botpost('Nobody liked ' + name + ' =/')
        elif len(names) == 1:
            botpost(name + ' was liked by ' + names[0] + ' the most.')
        elif len(names) > 1:
            last_name = names[-1]
            first_names = names[:-1]
            botpost(name + ' was most liked by ' + ', '.join(first_names) +
                    ' and ' + last_name + '(Last 100 messages).')            
    else:
        botpost('Try selecting a name after typing @')

def convertNames(results):
    nicknames = []
    members = getGroupMembers()
    for user_id in results:
        for member in members:
            if member['user_id'] == user_id:
                nicknames.append(member['nickname'])
    return nicknames

def getMaxLikes(data):
    highest = max(data.values())
    return [k for k, v in data.items() if v == highest]
    
def getGroupMembers():
    token = 'NB3oRIaPWEUXwJL0cQxOMF32P57eUs4yYfVIIeaT'
    group_api = 'https://api.groupme.com/v3/groups/15551585?token='
    r = requests.get(group_api + token)
    thestuff = r.json()
    return thestuff['response']['members']

def getMemberids(members):
    ids = []
    for member in members:
        ids.append(member['user_id'])
    return ids    

def getMessages():
    token = 'NB3oRIaPWEUXwJL0cQxOMF32P57eUs4yYfVIIeaT'
    msg_api = 'https://api.groupme.com/v3/groups/15551585/messages?token='
    r = requests.get(msg_api + token + "&limit=100")
    messages = r['messages']
    return messages
        
def botpost(text):
    payload = {"bot_id" : "f9b366898c181f1f3ef76da9f6",
               "text" : ""}
    payload['text'] = text
    r = requests.post('https://api.groupme.com/v3/bots/post', data=payload)
    return 'ok'

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
