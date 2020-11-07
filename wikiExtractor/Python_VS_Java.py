import os

# execution the extractors in python
from wikiExtractor import wikiMain

print('---------------------------------PYTHON EXTRACTOR----------------------------------------------')
duration_python = wikiMain
print('----------------------------------JAVA EXTRACTORS----------------------------------------------')
# execution the extractors in java
os.chdir("replace it by your java file jar")
command = "java -mx300m -cp WikipediaMatrix.jar fr.istic.pdl1819_grp5.wikiMain"
os.system(command)
print("Duration of the extractor in python: {} s".format(duration_python))