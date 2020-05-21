
with open ('results.csv', encoding="utf8") as f:
    for l in f.readlines():
        l = l.strip()
        partsofline = l.split(",")
        event = partsofline[1] 
        # print(event)
        if event == "Triple Jump Women": 
            print("event")
            print(partsofline[1]) 
            print(partsofline[3])
            print(partsofline[7])

        