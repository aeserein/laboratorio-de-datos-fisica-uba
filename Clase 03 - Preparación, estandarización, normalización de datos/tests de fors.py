array = ["1", "2", "3", "4"]

for i, a in enumerate(array) :
    a = a.lstrip().rstrip()
    if (a.isnumeric()) :
        print(type(a))
        array[i] = int(a) + 10
        print(type(a))
        print("----------------------")
print("###########")
print(array)
print("#####################################################\n\n")


dictRRSS = {
    1 : ["facebook"],
    2 : ["instagram"],
    3 : ["twitter", "love tw"],
    4 : [],
    5 : ["linkedin"],
    6 : ["reddit", "reditt", "redit"],
    7 : ["youtube", "yt videos", "you tube"],
    8 : ["telegram"],
    9 : ["whatsapp"],
    10 : ["tumblr"]
}

for i in dictRRSS :
    print(i)
    print(dictRRSS[i])
    if len(dictRRSS[i]) > 0 :
        print(dictRRSS[i][0])
    else :
        print("vacío")
    print("-------------------")

print("#####################################################\n\n")

array999 = [-999]
print(-999 in array999)