def greeting(name, course):
    print(f"hi, {name}. are you a {course} student ?")


# greeting(course="flutter", name="omolara", )


#
# greeting("ife", "python")
# greeting("omolara", "java")
# greeting("aisha", "perl")
# greeting("muhydeen", "flutter")
# greeting("bright", "php")
# greeting("muta", "golang")
# greeting("ola", "dart")
# greeting("zainab", "c++")

#
# def display_message():
#     print("learning about functions")
#
#
# display_message()
#
# def login(password, email, username=""):
#     users = {
#         "user1": {'username': 'bright', 'password': '12345', 'email': 'bright@yahoo.com'},
#
#         "user2": {'username': 'ife', 'password': '34567', 'email': 'ife@yahoo.com'},
#
#         "user3": {'username': 'muhy', 'password': '00000', 'email': 'muhy@yahoo.com'}
#     }
#     for user in users.values():
#         user_email = user["email"]
#         user_password = user["password"]
#         user_name = user["username"]
#
#         if email == user_email and password == user_password:
#             print("login successful")
#             break
#
#         else:
#             print("login failed")
#             break
#
#
# login(email="bright@yahoo.com", password="12345")
#
# def describe_city(city, country):
#     print(f"{city} is in {country} ")
#
#
# describe_city("lagos", "nigeria")
# describe_city("london", "UK")
# describe_city("florida", "USA")
#

# def message_students(names):
#     for name in names:
#         print(f"hi, {name}")
#
#
# student_names = ["omolara", "bright", "ife", "zainab", "ola"]
#
# message_students(student_names)

#
# def show_messages(texts):
#     for text in texts:
#         print(f"hey, {text}")
#
#
# text_message = ["how are you doing?", "hope you are fine?", "call me", "how was your day?", "fuck you!"]
#
# show_messages(text_message)

"ARBITRARY ARGUMENTS"



def print_places(*places):
    print(places)
    for place in places:
        print(place)

#
# print_places("kaduna", "oyo", "ilorin", "osun", "lagos", "US", "canada")


def items_needed_for_graduation(*items):
    print(items)
    for item in items:
        print(item)

#
# items_needed_for_graduation("suit", "shoes", "wristwatch", "belt", "socks", "briefs", "shades")
