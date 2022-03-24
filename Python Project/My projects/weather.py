#import pyowm


#github
#from pyowm import OWM
#from pyowm.utils import config
#from pyowm.utils import timestamps


#owm = OWM('e66d5c6c121e6c55415d65b99cd010e6')
#mgr = owm.weather_manager()

#place = input("В каком городе/стране? ")


#observation = mgr.weather_at_place('place')
#w = observation.weather

#print(w)




from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

# ---------- FREE API KEY examples ---------------------

owm = OWM('e66d5c6c121e6c55415d65b99cd010e6')
mgr = owm.weather_manager()


# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place('London,GB')
w = observation.weather

print(w)