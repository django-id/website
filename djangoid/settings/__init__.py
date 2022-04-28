from .main_apps import *
from .local import *
from .third_party_apps import *

try:
    from .secrets import *
except:
    pass

# use production if there is a file
try:
    from .production import *
except:
    pass
