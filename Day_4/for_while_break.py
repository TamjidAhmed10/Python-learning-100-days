a_var="the string"

for i in range(len(a_var)):
    print("hello ",a_var[i])
    if (a_var[i] == "i"):
        print("Broken")
        break
    else:
        continue

i=0
while i<len(a_var):
    print("hello ", a_var[i])
    
    if (a_var[i] == "i"):
        print("Broken")
        break
    else:
        i += 1
        continue
