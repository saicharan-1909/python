# favorite_movies = ["darling","orange","mirchi"]

# # for movies in favorite_movies:
# #     print(movies)


# student = {
#      "name" : "sai",
#      "age" : 19,
#      "college" : "abcd",
#      "branch" : "csm"}
# for key, value in student.items ():
#         print(key,":",value)


# text = "i love python"
# print(text.upper())
# print(text.lower())
# print(text.replace("python","programming"))


# laptop = {
#     "brand" : "HP",
#     "model" : "victus",
#     "ram" : 8,
#     "price" : 65000
#     }
# for key, value in laptop.items ():
#       print(key,":",value)


with open("story.txt", "r") as file:
    text = file.read()

words = text.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word, count in word_count.items():
    print(word, ":", count)
