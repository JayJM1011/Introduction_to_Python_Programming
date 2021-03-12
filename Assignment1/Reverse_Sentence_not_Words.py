String, start, Subs= input(), 0, []
for i in range(len(String)):
    if String[i] == " ":
        Subs.append(String[start:i])
        start= i+ 1
    if (i == len(String)- 1) and (i != " "):
        Subs.append(String[start:i+ 1])
String= ""
for i in range(len(Subs)- 1, -1, -1):
    String+= Subs[i]+ " "
print(String)