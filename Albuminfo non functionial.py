#this is not a properly functioning piece of code, but saving it so i remember the mistake i made with while loops

notDone = True

allAlbums = []

while notDone:
    

    albumName = input("Enter album name ")
    albumArtist = input("Enter artist name ")
    albumDate = input("Enter release date (M,D,YYYY) ")


    albumList = []
    print("Album title: ", albumName)
    albumList.append(albumName)
    print("Artist: ", albumArtist)
    albumList.append(albumArtist)
    print ("Release date: ", albumDate)
    albumList.append(albumDate)
    allAlbums.append(albumList)
    
    print ("Are you done?")
 
    answer = input("Enter yes or no: ")

    if answer == "yes":
        
        notDone = False
    elif answer == "no":
        
        break
    else:
        print ("Please answer yes or no.")
    
print(allAlbums)


