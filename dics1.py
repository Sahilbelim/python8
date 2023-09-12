dics={"name":"sahil","age":18,"weight":45.36,"gender":True}

print(dics)

print(dics["name"])

print(dics["gender"])

dics["height"]=5.3

dics["name"]="harsh"

print(dics)

dics["number"]=(1,2,3)

print(dics)

dics["data"]=[14,45.36,85,"param"]

print(dics)
dics2=dics.copy()
dics.clear()
print(dics)
print(dics2)

name=dics2.get("name")
print(name)
name=dics2.items()
print(name)
name=dics2.keys()
print(name)
name=dics2.pop("weight")
print(name)
print(dics2)
name=dics2.popitem()
print(name)
print(dics2)
name=dics2.values()
print(name)


