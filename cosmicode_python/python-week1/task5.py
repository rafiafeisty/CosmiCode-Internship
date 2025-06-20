def timeconversion():
    seconds=int(input("Enter the seconds: "))
    hours=int(seconds/3600)
    seconds=seconds-(hours*3600)
    minutes=int(seconds/60)
    seconds=seconds-(minutes*60)
    print("hours: ",hours)
    print("minutes: ",minutes)
    print("seconds: ", seconds)

timeconversion()