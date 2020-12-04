import os
# execution the extractors in python
from wikiExtractor.wikiMain import extractor_python
print('---------------------------------PYTHON EXTRACTOR----------------------------------------------')
duration_python = extractor_python()
print('----------------------------------JAVA EXTRACTORS----------------------------------------------')
# execution the extractors in java
# se positionner sur le répertoire du projet Extracteurs Java
java_extractor_path = "../../../PDL_1920_groupe-7"
os.chdir(java_extractor_path)
# génération et lancement Jar
command = "mvn clean install"
os.system(command)
print("Duration of the extractor in python: {} s".format(duration_python))
