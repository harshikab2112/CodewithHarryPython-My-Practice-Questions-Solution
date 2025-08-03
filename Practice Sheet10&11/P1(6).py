# Can you change the self-parameter inside a class to something else (say "harry"). Try changing self to "slf" or "harry" and see the effect.

import random


class Train:
    def book(slf, trainNo, start, destination):
        print(f"Train is booked in train no. {trainNo} from {start} to {destination}.")

    def getstatus(slf, trainNo):
        print(
            f"Train no. {trainNo} is running on time. If there is any delay in the arrival, you will be notified."
        )

    def getfare(slf, trainNo, start, destination):
        fare = random.randint(1000, 5000)
        print(
            f"Train fare in train no. {trainNo} from {start} to {destination} is ₹{fare}."
        )


t = Train()

t.book("12345", "Delhi", "Mumbai")
t.getstatus("12345")
t.getfare("12345", "Delhi", "Mumbai")

"""
works but,
Not recommended for production code if you rename self,
as it breaks Pythonic readability.
"""
