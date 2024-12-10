stuid ={"id1":
 {"name": ["sara"],
 "age":["7"] ,"class" : ["V"]},

"id2":
{"name":["susan"],
 "age":["8"],
 "class":["VI"]},
              
"id3":
{"name": ["sara"],
 "age":["7"] ,"class" : ["V"]},          
              
"id4":
{"name":["susan"],
 "age":["8"],
 "class":["VI"]},           
 }

result = {}
for key,value in stuid.items():
    if value not in result.values():
     result[key] = value

print (result)