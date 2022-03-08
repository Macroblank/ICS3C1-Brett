class Album:
  def __init__(self, title, artist, releaseYear,):
    self.title = title
    self.artist = artist
    self.releaseYear = int(releaseYear)
  
  def __str__(self):
    line = "\n\n**************************************\n"
    line += f"Title: {self.title}\n"
    line += f"Artist: {self.artist}\n"
    line += f"Year of release: {self.releaseYear}\n"
    line += f"How many years the album has been out {int(2022) - self.releaseYear}\n"
    line += "**************************************\n"
    return line

def getAlb(listIn):
  titleIn = input("What is the albums title?:  ")
  artistIn = input("Who is the artist who made the album?:   ")
  releaseYearIn = input("What year was it released?:    ")
  newAlbum = Album (titleIn, artistIn, releaseYearIn)
  listIn.append(newAlbum)
  print('\n'*4)

def printMenu():
  print('Please enter what you would like to do:')
  print('a. Enter a new album')
  print('b. Print the previously entered album')
  print('c. Exit')

albumList = []
numberOfAlbums = len(albumList)
while True:
  printMenu()
  choice = str(input(":"))
  if choice == "a":
    getAlb(albumList)
  elif choice == "b":
    print(albumList[-1])
  elif choice == "c":
    break
  else:
    print("Please enter a valid answer", '\n'*3)
    #This is what I wanted to do with my first attempt at this project but grouped it wrong