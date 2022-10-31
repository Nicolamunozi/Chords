
class Intervals():
    
    def __init__(self) -> None:
        
        self.intervals = [0,1,2,3,4,5,6,7,8,9,10,11]
        self.main_scale = ["A", "B", "C", "D","E","F","G"]
        self.has_sharp = [True,False,True,True,False,True,True]
        self.has_flat = [True, True,False,True,True,False,True]
        self.sharp_flat = {"sharp":"#", "Flat":"b"} 
        self.chords_names = "TODO: here to put M m M7 M9, etc..."
        
    def chromatic_scale(self):
        pass 