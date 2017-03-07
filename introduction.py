'''Amigos de amigos do capitulo de introdução'''
from collections import Counter

USERS = [{'id': 0, 'name': 'Hero'},
         {'id': 1, 'name': 'Dunn'},
         {'id': 2, 'name': 'Sue'},
         {'id': 3, 'name': 'Chi'},
         {'id': 4, 'name': 'Thor'},
         {'id': 5, 'name': 'Clive'},
         {'id': 6, 'name': 'Hicks'},
         {'id': 7, 'name': 'Devin'},
         {'id': 8, 'name': 'Kate'},
         {'id': 9, 'name': 'Klein'}
        ]

FRIENDSHIPS = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

for USER in USERS:
    USER['friends'] = []

for i, j in FRIENDSHIPS:
    USERS[i]['friends'].append(USERS[j]) # adiciona i como um amigo de j
    USERS[j]['friends'].append(USERS[i]) # adiciona j como um amigo de i

def number_of_friends(user):
    '''quantos amigos o usuario tem'''
    return len(user['friends'])

TOTAL_CONNECTIONS = sum(number_of_friends(user)
                        for user in USERS)

print('Total de conexões:', TOTAL_CONNECTIONS)


NUM_USERS = len(USERS)
AVG_CONNECTIONS = TOTAL_CONNECTIONS / NUM_USERS

print('Média de conexões:', AVG_CONNECTIONS)

NUM_FRIENDS_BY_ID = [(USER['id'], number_of_friends(USER)) for USER in USERS]

print(sorted(NUM_FRIENDS_BY_ID, key=lambda id_friends: id_friends[1], reverse=True))

def not_the_same(user, other_user):
    '''verifica se os usuários tem ids diferentes'''
    return user['id'] != other_user['id']


def not_friends(user, other_user):
    '''verifica se other_user não é amigos de user'''
    return all(not_the_same(friend, other_user)
               for friend in user['friends'])


def friends_of_friends_ids(user):
    '''lista os amigos em comum de deteterminado user'''
    return Counter(foaf['id']
                   for friend in user['friends']
                   for foaf in friend['friends']
                   if not_the_same(user, foaf)
                   and not_friends(user, foaf))

print(friends_of_friends_ids(USERS[3]))
