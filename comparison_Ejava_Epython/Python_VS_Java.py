import os
# execution the extractors in python
from wikiExtractor.wikiMain import extractor_python
print('---------------------------------PYTHON EXTRACTOR----------------------------------------------')
duration_python = extractor_python()
print('----------------------------------JAVA EXTRACTORS----------------------------------------------')
# execution the extractors in java
# se positionner sur le répertoire du projet Extracteurs Java
os.chdir("../../../IdeaProjects/PDL_1920_groupe-7")
# génération et lancement Jar
command = "mvn clean install"
os.system(command)
print("Duration of the extractor in python: {} s".format(duration_python))
