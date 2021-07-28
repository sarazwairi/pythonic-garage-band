from abc import abstractmethod,ABC

class Band(ABC):
    bands=[]
    

    def __init__(self,name,members):
        self.name=name
        self.members=members
        Band.bands.append(self)
    def play_solos(self):
        output=[]
        if len(self.members)!=0:
           for i in self.members:
               output.append(i.play_solo())
           return output
        else:
            return "no one" 

    
    def __str__(self):
        return f"{self.name}"

    @classmethod         
    def to_list(cls):
        return (cls.bands)
    def __repr__(self):
        return f"{self.name}"


class Musician(ABC):

    def __init__(self,name="unknown"):
            self.name=name
                
                
    def __str__(self):
        return f"My name is {self.name} and I play {self.get_instrument()}"
                    
  
    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"
                    
    def to_list(self):
        return Band.members
        

    @abstractmethod
    def play_solo(self):
        output=''
        for i in Band.members:
           output+=f'{i}'
        return output
   

class Guitarist(Musician):

    def get_instrument(self):
        return 'guitar'

    def play_solo(self):
        return 'face melting guitar solo'

class Bassist(Musician):

    def get_instrument(self):
        return 'bass'

    def play_solo(self):
        return 'bom bom buh bom'

class Drummer(Musician):

    def get_instrument(self):
        return 'drums'

    def play_solo(self):
        return 'rattle boom crash'

if __name__=="__main__":
    bassist=Bassist('bass')
    print(bassist)