'''Capitulo 1 - Introdução'''
###################################################
##                                               ##
##  Cientistas de dados que talvez você conheça  ##
##                                               ##
###################################################
from collections import Counter
from collections import defaultdict

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

#Traçar dados será abordado com mais detalhadamento no capitulo 3

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

#print(sorted(NUM_FRIENDS_BY_ID, key=lambda id_friends: id_friends[1], reverse=True))

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

print('Amigos dos amigos de Chi', friends_of_friends_ids(USERS[3]))

INTERESTS = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

def data_scientists_who_like(target_interest):
    '''Encontra pessoas com mesmos interesses'''
    return [user_id
            for user_id, user_interest in INTERESTS
            if user_interest == target_interest]

USER_IDS_BY_INTEREST = defaultdict(list)

for user_id, interest in INTERESTS:
    USER_IDS_BY_INTEREST[interest].append(user_id)

INTERESTS_BY_USER_ID = defaultdict(list)

for user_id, interest in INTERESTS:
    INTERESTS_BY_USER_ID[user_id].append(interest)

def most_common_interests_with(user):
    '''Retorna os usuários que tem os mesmo interesses com o user'''
    return Counter(interested_user_id
                   for interest in INTERESTS_BY_USER_ID[user['id']]
                   for interested_user_id in USER_IDS_BY_INTEREST[interest]
                   if interested_user_id != user['id'])

print('Usuários com mesmos interesses com Chi', most_common_interests_with(USERS[3]))

#Combinação de interesses será melhor abordado no capitulo 22

###################################################
##                                               ##
##           Salários e experiências             ##
##                                               ##
###################################################

SALARIES_AND_TENURES = [
    (83000, 8.3), (88000, 8.1),
    (48000, 0.7), (76000, 6),
    (69000, 6.5), (76000, 7.5),
    (60000, 2.5), (83000, 10),
    (48000, 1.9), (63000, 4.2)
]

SALARY_BY_TENURE = defaultdict(list)

for SALARY, TENURE in SALARIES_AND_TENURES:
    SALARY_BY_TENURE[TENURE].append(SALARY)

AVARAGE_BY_TENURE = {
    tenure : sum(salaries) / len(salaries) for tenure,
    salaries in SALARY_BY_TENURE.items()
}

def tenure_bucket(tenure):
    ''' retorna o intervalo de experiencia '''
    if tenure < 2:
        return 'menor que dois'
    elif tenure < 5:
        return 'entre dois e cinco'
    else:
        return 'maior que cinco'

SALARY_BY_TENURE_BUCKET = defaultdict(list)

for SALARY, TENURE in SALARIES_AND_TENURES:
    bucket = tenure_bucket(TENURE)
    SALARY_BY_TENURE_BUCKET[bucket].append(SALARY)

AVARAGE_SALARY_BY_BUCKET = {
    tenure_bucket : sum(salaries) / len(salaries)
    for tenure_bucket, salaries in SALARY_BY_TENURE_BUCKET.items()
}

print(AVARAGE_SALARY_BY_BUCKET)

#Previsões serão aboradados no capitulo 14

###################################################
##                                               ##
##                 Contas a pagar                ##
##                                               ##
###################################################

def predict_paid_or_unpaid(years_experience):
    '''tenta prever a probabilidade de pagamento pelos
        anos de experiencia'''
    if years_experience < 3.0:
        return 'paid'
    elif years_experience < 8.5:
        return 'unpaid'
    else:
        return 'paid'
#Predição e probabilidade será explorado no capitulo 16

###################################################
##                                               ##
##            Tópicos de interessse              ##
##                                               ##
###################################################

WORDS_AND_COUNTS = Counter(word
                           for user, interest in INTERESTS
                           for word in interest.lower().split())
print(*((word, count) for word, count in WORDS_AND_COUNTS.items()), sep='\n')

#Extração de tópicos dos dados será visto no capitulo 20
