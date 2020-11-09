# PDL_2021
Projet d'extraction de tableaux sur une page wikipédia avec python


Before run you must install the following libraries :
- pandas
- html5lib (pandas need to solve some problem)
- lxml (pandas need to solve some problem)
- requests
- bs4
- os
------------------------------------------------------------------------------------------
to be able to launch the script Python_VS_Java.py if you don't have jar file for java extractors:
you must generate a file. jar from the java project with IntelliJ IDEA including dependencies
by following these steps :

- "File | Project Structure ... | Artifacts";
- click on the "+";
- select "JAR -> From modules with dependencies ...";
- select the "Main Class" (entry point of the application);
- click on "OK";
- in the following window, click on "Apply", then "OK";
- in the menu bar, do "Build | Build Artifacts ...";
 - in the "Action" list, select "Build";
 - the "jar" file is generated in the "out / artifacts / nom_du_projet_jar /" directory
 
 Then replace the jar file path obtained in the script (Python_VS_Java.py)

