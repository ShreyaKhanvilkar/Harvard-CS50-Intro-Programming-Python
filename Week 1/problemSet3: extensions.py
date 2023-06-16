user_input = input("File name: ").lower().strip().split(".")

match user_input[-1]:
    case "gif" | "png":
        print("image/" + user_input[-1])
    case "jpg" | "jpeg":
         print("image/jpeg")
    case "txt":
        print("text/plain")
    case "zip" | "pdf":
        print("application/" + user_input[-1])
    case _:
        print("application/octet-stream")
