import os

# execution the extractors in python

from wikiExtractor.wikiMain import extractor_python

print('---------------------------------PYTHON EXTRACTOR----------------------------------------------')
duration_python = extractor_python()
print('----------------------------------JAVA EXTRACTORS----------------------------------------------')
# execution the extractors in java
os.chdir("C:/Users/anwar/IdeaProjects/out/artifacts/WikipediaMatrix_jar")
command = "java -mx300m -cp WikipediaMatrix.jar fr.istic.pdl1819_grp5.wikiMain"
os.system(command)
print("Duration of the extractor in python: {} s".format(duration_python))
