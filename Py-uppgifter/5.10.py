# Programmet skriver ut dagens datum och aktuell tid.

# Använder datetime-modulen för att hämta aktuell tid och datum.

import datetime
dt=datetime.datetime.now()
d=dt.date()
t=dt.time()
print("Dagens gatum:", str(d))
print("Klockan är:", str(t)[:8])