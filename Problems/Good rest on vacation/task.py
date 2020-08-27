# put your python code here
d = int(input()) # duration in days
food = int(input()) # total food cost
flight = int(input()) # one way flight cost
hotel = int(input()) # cost of one night in a hotel

total = ((food * d) + (flight * 2) + (hotel * (d-1)))

print(total)
