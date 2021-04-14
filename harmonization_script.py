data1 = [["name", "var1", "var2", "var3"],["a", 1,1,"x" ],["b", 2,1,"y" ],["c", 3,1,"z" ]]

key_dict = {"var1":{1:3,2:2,3:1}, "var2":{1:-1,2:-2,3:-3}, "var3":{"x":1,"y":2,"z":3}}


x = 4 #number of variables /  collums in top row

for i in range(0,x):
    search_string = data1[1][0]
    print(search_string)
    print(key_dict[search_string])