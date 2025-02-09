media = input("File name? ")

media = media.lower()

if ".jpeg" in media:
    print("image/jpeg")
elif ".gif" in media:
    print("image/gif")
elif ".jpg" in media:
    print("image/jpg")
elif ".png" in media:
    print("image/png")
elif ".pdf" in media:
    print("application/pdf")
elif ".txt" in media:
    print("plain/txt")
elif ".zip" in media:
    print("application/zip")
else:
    print("application/octet-stream")