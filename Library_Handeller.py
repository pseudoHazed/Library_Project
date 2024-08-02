# Library Project

class Movie_Node():

    def __init__(self, name = None, releaseDate = None, duration = None, genre = None):
        self.name = name
        self.releaseDate = releaseDate
        self.duration = duration
        self.genre = genre
        self.next = None

class Movie_Library():

    def __init__(self):
        self.head = Movie_Node()

    def add_movie(self, name, releaseDate, duration, genre):
        newNode = Movie_Node(name, releaseDate, duration, genre)
        currentNode = self.head
        while currentNode.next is not None:
            currentNode = currentNode.next
        currentNode.next = newNode
        return "Movie Added Successfully"
    def remove_movie(self, name):
        currentNode = self.head
        stat = False
        while currentNode.next is not None:
            while currentNode.next.name != name:
                currentNode = currentNode.next
            currentNode.next = currentNode.next.next
            stat = True
            break
        if stat == True:
            return "Movie deleted Successfully"
        else:
            return "Movie not Found"
        
    
    def search_movie(self, name):
        currentNode = self.head
        while currentNode:
            if currentNode.name == name:
                return self._print_node(currentNode)
            currentNode = currentNode.next
            

    def _print_node(self, node):
        print(f"Name: {node.name} -- Release Date: {node.releaseDate} -- Duration: {node.duration} minutes -- Genre: {node.genre}")
    def filter_movie(self, attribute, query):
        currentNode = self.head
        found = False
        while currentNode:
            if str(getattr(currentNode, attribute , "")).lower() == str(query).lower():
                self._print_node(currentNode)
                found = True
            currentNode = currentNode.next
        if found == False:
            return "No Movies Found"
        
    def display(self):
        currentNode = self.head
        if currentNode.next is None:
            return "Library Is Empty"
        
        while currentNode.next:
            currentNode = currentNode.next
            self._print_node(currentNode)
    
    def read_from_file(self, fileName):
        try:
            with open(fileName, 'r') as file:
                for line in file:
                    line.strip()
                    if line:
                        name, releaseDate, duration, genre = line.split('--')
                    self.add_movie(name, releaseDate, duration, genre)
            print("Import successful")
        except FileNotFoundError:
            print(f"Error: File '{fileName}' not found.")
        except Exception as error:
            print(f"An error occurred: {error}")
    def write_to_file(self):
        try:
            with open("library","w") as file:
                currentNode = self.head
                while currentNode:
                    file.write(f"{currentNode.name}--{currentNode.release_date}--{currentNode.duration}--{currentNode.genre}\n")
                    currentNode = currentNode.next
            print("Library saved Successfully")
        except Exception as error:
            print(f"Error: {error}")
