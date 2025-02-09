time = input("time? ")

def convert_time(time):
    hours, minutes = time.split(":")
    minutes = int(minutes)
    global Int_time
    Int_time = hours + (f"{minutes}")
    Int_time = int(Int_time)
    print(Int_time)
    



def main(t):
    convert_time(time)
    if 700 < int(Int_time) < 800:
        print("breakfast time")
    elif 1200 < int(Int_time) < 1300:
        print("lunch time")
    elif 1800 < int(Int_time) < 1900:
        print("dinner time")

main(1)