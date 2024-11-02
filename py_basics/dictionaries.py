# users = {1: "ola", 2: "muhy", 3: "lara", 4: "ekene", 5: "emeka", 6: "zainab", 7: "faruq"}

# second_user = users[2]
# print(second_user)

# new_dic = {"car": "a means of land transportation", "honey": "a sweet drink", "phone": "a means of communication",
#            "boat": "a means of water transportation"}
#
# search = input("search word: ")
# result = new_dic[f'{search}']
# # print(result)

# information = {"firstname": "muhy", "lastname": "dogba", "age": "19", "city": "florida"}

# print(information)

users = {"user1": "zainab", "user2": "muhy", "user3": "omolara", "user4": "emeka", "user5": "ife", "user6": "ola"}
#
# for key, value in users.items():
#     print(f'key: {key} value: {value}')


# looping through keys
# for values in users.values():
#     print(values)

# voters = ["zainab", "muhy", "lara", "emeka", "ife", "ola"]
#
# voted = {"zainab": "atiku", "muhy": "tinubu", "lara": "obi"}
#
# for voter in voters:
#     if voter in voted.keys():
#         print(f"{voter}, thanks for voting")
#     else:
#         print(f"{voter}, oga cast your vote")
#

cities = { "florida": {
    "country": "usa",
    "population": "200million",
    "fact": "highest number of obesity \n"
 },
    "milan": {
        "country": "italy",
        "population": "100million",
        "fact": "city of fashion \n"
 },
    "syprus": {
        "country": "turkey",
        "population": "90million",
        "fact": "good tea"
    }
           }

for key, value in cities.items():
    print(f"{key} has the following info: ")
    country = value.get("country")
    population = value.get("population")
    fact = value.get("fact")
    print(country)
    print(population)
    print(fact)