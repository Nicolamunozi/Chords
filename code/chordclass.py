
class Intervals():
    
    def __init__(self, note: str()) -> None:
        
        self.note = note.upper()
        self.intervals_distance = [0,1,2,3,4,5,6,7,8,9,10,11,12]
        self.intervals_names = [
                           'Fundamental',
                           'Minor Second', 'Mayor Second',
                           'Minor Third', 'Mayor Third',
                           'Perfect Fourth',
                           'Tritone',
                           'Perfect Fifth',
                           'Minor Sixth','Mayor Sixth',
                           'Minor Seventh', 'Mayor Seventh',
                           'Octave'
                           ]
        self.main_scale = ["A", "B", "C", "D","E","F","G"]
        self.has_sharp = [True,False,True,True,False,True,True]
        self.has_flat = [True, True,False,True,True,False,True]
        self.sharp_flat = {"sharp":"#", "Flat":"b"} 
        self.chords_names = "TODO: here to put M m M7 M9, etc..."
        
    def chromatic_scale(self):
        '''This function is for return the chromatic scale
            (12 notes) for a certain note'''
            
        #Initializations:
        current_note_index = self.main_scale.index(self.note)
        index_range = len(self.main_scale)
        sharp_mode = list()
        flat_mode = list()
        intervals = [{"Name": self.intervals_names[index], "Distance": self.intervals_distance[index]}for index in range(13)]
        last_flat_note = None
        #The function:
        for index in range(index_range):            
            note_index = (index + current_note_index) % index_range
            current_note= self.main_scale[note_index]
            sharp_bool = self.has_sharp[note_index]
            flat_bool = self.has_flat[note_index]            
            #1: Sharp view
            sharp_mode.append(current_note)
            if sharp_bool:
                sharp_mode.append(f"{current_note}#")
            #2: Flat view 
            if flat_bool:
                if index!=0:
                    flat_mode.append(f"{current_note}b")
                else:
                    last_flat_note = f"{current_note}b"
            flat_mode.append(current_note)
        if not not last_flat_note:
            flat_mode.append(last_flat_note)
            
        print(f'Intervals for {self.note} Chromatic Scale are:\n Note || Distance from Fundamental || Name of the Interval')
        n=0
        for interval in intervals:
            if n==12:
                break
            print(f'{sharp_mode[n]}|{flat_mode[n]} -> {interval["Distance"]} -> {interval["Name"]}')
            n+=1