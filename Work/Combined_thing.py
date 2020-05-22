listofx = []
listofy = []

event_want = 'Discus Throw Men'

with open ('results.csv', encoding="utf8") as f:
    for l in f.readlines():
        l = l.strip() # this thing gets rid of the new line character at the end of each line
        partsofline = l.split(",") # splits the string into bits
        print(l)
        print(partsofline)
        
        event = partsofline[1] # finds the 1st (second) bit fo the list and labels it "event"
        # print(event)
        if event == event_want: #if the event is "triple jump women" then print the things below it
            print("event")
            distance = partsofline[7]
            if distance != "None":
                
                distancenumber = float(distance) 
                listofy.append(distancenumber)
                print("distance is: ", distance)
                # print(listofx)
                # print(listofy)
                print(partsofline[1])
                date = partsofline[3] 
                datenumber = int(date)
               

                listofx.append(datenumber)
                print('date is: ', date)
                # print(partsofline[3])
                # print(partsofline[7])
                distance = partsofline[7]

                    
import plotly.express as px  
fig = px.scatter(x=listofx, y=listofy, trendline="ols" )       
fig.show() 

filename = event_want.replace(' ', '_') + '.html'
fig.write_html(filename)


