import importlib
lib1 = importlib.import_module('mod1')
lib2 = importlib.import_module('mod2')
lib3 = importlib.import_module('pack1.mod3')
lib1.run()
lib2.run()
lib3.run()
