"""
Ian, Amelie, and Autumn
10/28/24
This program runs a class schedule builder from Monday to Friday with classes you choose during the day.
Just put it in geany to run it since we cant run it here.
"""
class ClassSchedule:
    def __init__(self):
        self.schedule = {day: [] for day in ["Monday", "tuesday", "Wednesday", "Thursday", "Friday"]} # make the list of days for day
        
    def add_class(self, class_name, day, start_time, duration): #class name, day, start time, then duration of that class
        if day in self.schedule:
            end_time = self.calculate_end_time(start_time, duration)
            if not self.check_conflict(day, start_time, end_time):
                self.schedule[day].append({"class_name": class_name, "start_time": start_time, "end_time": end_time}) #appends the name, time, and end time to new list
                print(f'Added: {class_name} on {day} from {start_time} to {end_time}.') # will print the right things if all goes wel
            else:
                print(f"There's a conflict of {class_name} on {day}.") #doesnt print if the day and start/end time dont match
        else:
            print("Invalid day") #just prints if the day is not in Mon-Fri or anything other random thing
    
    # start a new function for duration
    def calculate_end_time(self, start_time, duration):
        start_hour, start_minute = map(int, start_time.split(':')) #splits it into two parts with the :, so 14,30 goes 14:30, map(int) converts string into integers
        end_hour = start_hour + duration // 60 #calculates if the time is 130 mins then 130 // 60 would be 2 hours
        end_minute = start_minute + duration % 60 #calculates remaining mins
        if end_minute >= 60: #this checks if the time goes over an hour(60 mins)
            end_hour += 1
            end_minute -= 60
        return f"{end_hour}:{end_minute}" #this return it as many times as needed

    # start a new function for the conflict
    def check_conflict(self, day, start_time, end_time): #check for conflicts in schedule!!!
        for word in self.schedule[day]: #iterates through day
            if (start_time < word['end_time']) and (end_time > word['start_time']): #checks before and after the scheduled time
                return True
        return False
        
    # display the actual schedule itself
    def display_schedule(self):
        print("Class Schedule:")
        for day, classes in self.schedule.items(): #day is the key and classes is the value hence .items()
            print(f'{day}:')
            if not classes:
                print("No classes scheduled") #if no classes have been scheduled
            for word in classes:
                print(f"{word['class_name']} from {word['start_time']} to {word['end_time']}")
                print() #prints a line
#the main program here
def main():
    gen = ClassSchedule()

    while True:
        class_name = input("Enter in class name or type 'exit' to stop: ")
        if class_name.lower() == 'exit': #lower makes the words lowercase
            break
        
        day = input("Enter the day of the week (Monday - Friday): ")
        start_time = input("Enter in the start time of class (HH:MM): ")
        duration = int(input("Enter the duration in minutes of class: " ))
        gen.add_class(class_name, day, start_time, duration)
    gen.display_schedule()

if __name__ == "__main__":
    main()
