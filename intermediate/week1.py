# caian 05/01/2016

class Date(object):
    """
    Simple date object.
    """
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def today(self):
        """
        Return a string date of today.
        """
        return str(self.day + "/" + self.month + "/" + self.year)

class Event():
    """
    Simple event object.
    """
    def __init__(self, name, date, description=None):
        self.name = name
        self.date = date
        self.description = "No description."
        if description != None:
            self.description = description

    @property
    def show(self):
       return self.date.today() + "   " + self.name + "\n" + self.description + "\n"
        
class Calendar(object):
    """
    Simple calendar.
    """
    def __init__(self, date_today):
        self.date = date_today
        self.events = {}
        self.count = 0

    def today(self):
        """
        Return a string date of today.
        """
        return self.date.today

    def schedule(self, name, date, description=None):
        """
        Schedule some event.
        """
        event = Event(name, date, description)
        self.count += 1
        events[self.count] = event
        print("Event: " + self.count + event.show)
        return

    def cancel(self, name):
        """
        Cancel a schedule event.
        """
        pass

def menu():
    pass
