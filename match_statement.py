http_status = int(input("Enter your http humber: "))

match http_status:
    case 200 | 201:
        print("Success")
    case 400:
        print("Not Fund")
    case 500 | 501:
        print("Server Error")
    case _:
        print("Unknown")
        


https = 554

if https == 200 or https == 201:
    print("Success Done")
elif https == 400:
    print("Bad request")
elif https == 404:
    print("Not Found")
elif https == 500 or 501:
    print("Server Erro")
else:
    print("Unknown request")