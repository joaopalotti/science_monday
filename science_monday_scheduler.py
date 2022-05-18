
################################################################################
#                                                                              #
#       Science Monday Organizer                                               #
#       Author: Joao Palotti                                                   #
#                                                                              #
################################################################################

import random
import pandas as pd

def insert_social_gathering(names):

    result = []
    for i, name in enumerate(names):
        result.append(name)

        if i % 6 == 5:
            result.append("Social Computing Group Meeting")

    return result

start_date = '01/Aug/2022'


names = ["Abdelkader Baggag", "Abdulaziz Al Homaid", "Ferda Ofli", "Masoomali Fatehkia", "Michaël Aupetit",
         "Muhammad Imran",  "Soon-Gyo Jung", "Syed Moosavi", "Umair Qazi", "Zainab Akhtar",
         "Noora Al-Emadi", "Rizwan Sadiq", "Reham Al tamime", "Bernard Jansen", "Abdelkader Lattab", 
         "Marie-Christine Rufener", "Aya Ali Tawfiq Elsaqa",
         ]
         
# In case you want to force some names to be at the end of the random list (e.g., because they have just presented recently),
# just move their names from the list above to the list below:
have_recently_presented = []

random.seed(42)

names = sorted(names)
have_recently_presented = sorted(have_recently_presented)

# Shuffle names and merge them together
random.shuffle(names)
random.shuffle(have_recently_presented)
result = names + have_recently_presented

result = insert_social_gathering(result)

print("Final List (%d): %s" % (len(result), result))

# Generate a data series
dates = pd.date_range(start_date, periods=len(result), freq="7D")

# Copy and paste these results in our wiki
for date, name in list(zip(dates, result))[::-1]:
    print("%s:\t%s" % (date.strftime("%d %b %Y"), name))



