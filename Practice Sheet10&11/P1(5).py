# Write a class Train which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.
import random


class Train:
    def book(self, trainNo, start, destination):
        print(f"Train is booked in train no. {trainNo} from {start} to {destination}.")

    def getstatus(self, trainNo):
        print(
            f"Train no. {trainNo} is running on time. If there is any delay in the arrival, you will be notified."
        )

    def getfare(self, trainNo, start, destination):
        fare = random.randint(1000, 5000)
        print(
            f"Train fare in train no. {trainNo} from {start} to {destination} is ₹{fare}."
        )


t = Train()

t.book("12345", "Delhi", "Mumbai")
t.getstatus("12345")
t.getfare("12345", "Delhi", "Mumbai")
