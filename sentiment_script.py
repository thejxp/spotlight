from sentiment_analysis import *
from spotlight_class import *


app = Spotlight()

machine = MachineSpotlight()



machine.manage_data()
machine.build_classifier()

# update_classifier

#######################

a = machine.update_classifier("")
print a

machine.write_data("data.py", "Alisha")