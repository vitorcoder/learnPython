imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
    
album, artist, year, tracks = imelda

print (artist)
print (album)
print (year)

for track in tracks:
    number, music = track
    print("\t {} - {}".format(number, music))