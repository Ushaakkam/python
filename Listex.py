# REPLACE,APPEND,SORT,DELETE,INSERT,REVERSE,REMOVE,EXTEND

personToDo=["usha","udaya"]
doingMsOpt=["Usa","london","canada","australia"]

doingMsOpt[3]="Germany"
print(doingMsOpt)

doingMsOpt.append("australia")
print(doingMsOpt)

doingMsOpt.sort()
print(doingMsOpt)

del doingMsOpt[0]
print(doingMsOpt)

doingMsOpt.insert(4,"newyork")
print(doingMsOpt)

doingMsOpt.reverse()
print(doingMsOpt)

doingMsOpt.remove("australia")
print(doingMsOpt)

doingMsOpt.extend(personToDo)
print(doingMsOpt)




 
            
