#Reflex agent Vaccum Cleaner Agent

room = {
    'A': 'Clean',
    'B': 'Dirty'
}

position = 'A'
while 'Dirty' in room.values():
    print("Agent is in Room", position)
    
    if room[position] == 'Dirty':
        print("Room is Dirty")
        print("Action: Suck")
        room[position] = "Clean"
    else: 
        print("Room is Clean")

    if position == 'A':
        position = 'B'
    else: 
        position = 'A'

print("Final Status: ", room)
print("All Rooms are clean")