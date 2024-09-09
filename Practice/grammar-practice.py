fruit_color = {"apple" : "red", "banana" : "yellow", "peach":"pink"}
no_bana = {}

for key in fruit_color:
    if key != "banana":
        no_bana[key] = fruit_color[key]

print(no_bana)
