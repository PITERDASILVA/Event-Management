class Event():
    def __init__(self, eventName, date, local, people_list):
        self.eventName = eventName
        self.date = date
        self.local = local
        self.people_list = people_list
     

        #add participantes
        #remover participantes
        #listar 
    def add_participant(self, person):
        self.people_list.append(person)
        
    def remove_participant(self, person):
        self.people_list.remove(person)
    
    def list_participants(self):
        for i, person in enumerate(self.people_list, 1):
            print({person})


class People():
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

        #inscrição
        #cancelar inscrição
    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Phone Number: {self.phone}"
        
class Local():
    def __init__(self, localName, localAdress, localCapacity):
        self.localName = localName
        self.localAdress = localAdress
        self.localCapacity = localCapacity
        self.working = False

        #verificar disponibilidade do evento
    def avaiable(self):
        if not self.working:
            self.working = True
            return False
        return False
    
    def unavaiable(self):
        if self.working:
            self.working = False
            return True
        return True

class EventManagement():
    def __init__(self):
        self.events = []
        self.people = []
        self.locals = []
 
    def create_event(self, event):
        self.events.append(event)

    def cancel_event(self, event):
        self.events.remove(event)

    def list_events(self):
        for i, event in enumerate(self.events, 1):
            print(f"{event.eventName} - {event.date}")
       
    
    def event_details(self, eventName):
        for event in self.events:
            if event.eventName.lower() == eventName.lower():
                print(f"Event: {event.eventName}")
                print(f"Date: {event.date}")
                print(f"Local {event.local}")
                print("Participants:")
                event.list_participants()
                return
            print("Event not found")

   
        


def options():
    print("Event Options")
    print("1. Buy tickets")
    print("2. Cancel order")
    print("3. Event Details")
    print("4. New Events")
    print("5. Create New Event")
    print("6. Exit")        

def main():
    management = EventManagement()
    

    while True:
        options()
        choice = input("Choose one option: ")

        if choice == '1':
          name = input("Name: ")
          email = input("Email:")
          phone = input("Phone:")

          personDetails = People(name, email, phone)
          eventName = input("Enter the event name")
          for event in management.events:
            if event.eventName.lower() == eventName.lower():
                event.add_participant(personDetails)

        if choice == '2':
          name = input("Name: ")
          email = input("Email:")
          phone = input("Phone:")

          management.remove_participant.remove(personDetails)
          print("Subscription Cancelled")

        if choice == '3':
            eventName = input("Event Name: ")
            print("Event List: ")
            management.event_details(eventName)
        
        if choice == '4':
            management.new_event_detail()

        if choice == '5':
            print("New Event")
            print("-----------")
            eventName = input("Event Name:")
            date = input("Event date: ")
            local = input("Local date: ")
            people_list = []
            eventDetails = Event(eventName, date, local, people_list)
            management.create_event(eventDetails)
            print("Event created successfully")
        
        if choice == '6':
            break

        else:
            print("Not found")

        




if __name__ == '__main__':
    main()