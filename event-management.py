
from datetime import datetime

class Event():
    def __init__(self, eventName, date, local, ticket_available, ticket_price ,people_list):
        self.eventName = eventName
        self.date = date
        self.local = local
        self.ticket_available = int(ticket_available)
        self.ticket_price = int(ticket_price)
        self.people_list = people_list
     

        #add participantes
        #remover participantes
        #listar 

    def add_participant(self, person):
        if self.ticket_available > 0:
            self.people_list.append(person)
            self.ticket_available -= 1
            print(f"Ticket purchased successfully.")
        else:
            print("No tickets available")
        
    def remove_participant(self, person):
        self.people_list.remove(person)
        self.ticket_available += 1
    
    def list_participants(self):
        for i, person in enumerate(self.people_list, 1):
            print(f"{i} - {person}")

    def number_of_participants(self):
        return len(self.people_list)

class People():
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = float(phone)

        #inscrição
        #cancelar inscrição
    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Phone Number: {self.phone}"

    def __eq__(self, other):
        if isinstance(other, People):
            return self.email == other.email
        return False 
    
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
            print(f"{i} - {event.eventName} - {event.date.strftime('%d/%m/%Y')}")
       
    
    def event_details(self, eventName):
        for event in self.events:
            if event.eventName.lower().startswith(eventName.lower()):
                print(f"Event: {event.eventName}")
                print(f"Date: {event.date.strftime('%d/%m/%Y')}")
                print(f"Local: {event.local}")
                print(f"Price: ${event.ticket_price} ")
                print(f"Tickets Available: {event.ticket_available}")
                print(f"Participants: {event.number_of_participants()}")
                return   
        print("Event not found")

   

def options():
    print("Event Options")
    print("1. Buy tickets")
    print("2. Cancel order")
    print("3. Event Details")
    print("4. All Events")
    print("5. Create New Event")
    print("6. Exit")        

def main():
    management = EventManagement()
    

    while True:
        options()
        choice = input("Choose one option: ")

        if choice == '1':
          
          eventName = input("Enter the event name: ")
          event_found = False
          for event in management.events:
              if event.eventName.lower().startswith(eventName.lower()):
                event_found = True
                management.event_details(eventName)
                break
                
          if not event_found:
                print("Event Not Found")
                continue
          
          
          print("Personal Details: ")
          name = input("Name: ")
          email = input("Email:")
          phone = float(input("Phone:"))
          personDetails = People(name, email, phone)
          event.add_participant(personDetails)
          


        if choice == '2':
          eventName = input("Enter the event name: ")
          event_found = False
          
          for event in management.events:
              if event.eventName.lower().startswith(eventName.lower()):
                  event_found = True
                  break

          if not event_found:
                print("Event not found.")
                continue

          name = input("Name: ")
          email = input("Email:")
          phone = input("Phone:")
          personDetails = People(name, email, phone)

          if personDetails in event.people_list:
                event.remove_participant(personDetails)  
                print("Subscription Cancelled")  
          else:
              print("Participant not found in the event")
            

        if choice == '3':
            eventName = input("Event Name: ")
            print("Event List: ")
            management.event_details(eventName)
        
        if choice == '4':
            print("* Events *")
            management.list_events()

        if choice == '5':
            print("New Event")
            print("-----------")
            eventName = input("Event Name:")
            while True:
                date_str = input("Event Date: ")
                try:
                    date = datetime.strptime(date_str, "%d/%m/%Y")
                    if date < datetime.now():
                        print("Invalid date format. Try again.")
                    else:
                        break
                except ValueError:
                    print("Invalid date format. Try again.")

            local = input("Local : ")
            ticket_price = int(input("Price:" ))
            ticket_available = int(input("Tickets Available: "))
            people_list = []
            eventDetails = Event(eventName, date, local, ticket_available ,ticket_price,people_list)
            management.create_event(eventDetails)
            print("Event created successfully")
        
        if choice == '6':
            break


if __name__ == '__main__':
    main()