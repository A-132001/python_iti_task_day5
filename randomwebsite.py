import webbrowser
mydict = {"linkedin":"https://www.linkedin.com/feed/","facbook":"https://www.facbook.com/"}

link = input("Enter the website you want to visit:linkedin or facbook:- ")

for i in mydict:
    if i == link.lower():
        webbrowser.open(mydict[i])
    else:
        print("invaild input")
        
