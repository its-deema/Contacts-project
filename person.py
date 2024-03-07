class Person :
    
    def __init__(self, name , numbers , email ):
        self.name = name 
        self.numbers = numbers 
        self.email = email 

    def __eq__(self, other : "Person" ) -> bool:
        if ( self.name == other.name and self.numbers == other.numbers and self.email == other.email):
            return True
        return False
    
    def __str__(self) -> str:
        numbers_str = '\n'.join(f"\t{k}: [{v}]" for k, v in self.numbers.items())
        return f"{self.name}:\n{numbers_str}\n\temail: {self.email}"
    
    def __lt__(self , other : "Person") -> bool :
        return self.name < other.name
    
    def __le__(self , other : "Person") -> bool :
        return self.name <= other.name
    
    def __gt__(self , other : "Person") -> bool :
        return self.name > other.name
    
    def __ge__(self , other : "Person") -> bool :
        return self.name >= other.name