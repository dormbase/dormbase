from dormbase.core.populate import *
from dormbase.package.populate import *
from dormbase.movie.populate import *

def import_test_database():
    import_test_directory()
    import_test_packages()
    import_test_movies()
    
