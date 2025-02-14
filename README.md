# python_games
Schoolproject V5. Gemaakt door Sonja Raijer

voor deze applicatie moet je de PILLOW (PIL) library downloaden, hiervoor kun je de volgende code gebruikten in je terminal:
pip install pillow

If you are using Thonny, make sure that the library is added to Thonny aswell.

 Evaluatie:
 - Wat heb ik gedaan?
 Ik heb een python-applicatie met een General-User-Interface gemaakt.
 De applicatie die ik heb gekozen is een journaling-prompt list/generator waarbij je kunt afstrepen welke prompts je al hebt gedaan.
 In de app kun je af-vinken welke prompts je al hebt gedaan, zelf meer prompts invoegen en entries opslaan.
 - Wat heb ik geleerd?
 Ik heb geleerd met python en SQLite3 te werken, dit was om een database te kunnen maken die de prompts opslaat, ook als je zelf meer toevoegt.
 OOk heb ik geleerd over de basics van Python, zoals loops, gegevens validatie, User-Defined Functions en databases.
 - Waar ben ik tegen aan gelopen en hoe heb ik dit opgelost?
 Ik ben tegen veel obstakels gelopen tijdens het schrijven van de code voor de applicatie. Onderanderen tijdens de opzet van de database (DB). Ik heb Youtube video's gekeken om te leren hoe je een database met een list kan opzetten, vervolgens een beejte geprobeert en nagevraagd bij mensen die ook python kennen.
 Daarna kwam ik tegen mijn tweede probleem aan, een nieuwe prompt toevoegen.
 Ik kon niet een prompt toevoegen aan de lijst met list.append(), doordat ik niet zeker wist of de prompt dan zou worden opgeslagen in de DB. Ik ben op forums zoals stackoverflow gegaan om te leren hoe je dit kan doen.
 Hierna kwam ik tegen een paar problemen met de userguide-button tegen, maar gelukkig kwam stackoverflow weer te hulp. Ik heb het probleem - het niet openen op een ander device - opgelost door ook os te importeren, wat het pad op een pc bepaalt van een bepaalde file. Na dit toe te voegen werkt het gelukkig wel.
 Tot slot kwam ik tegen een probleem met de eisen van het PO. Ik moest een while-loop toevoegen, maar als je dit in de root-window deed, zou het in de knel raken met mailoop(). Om toch een while-loop te hebben, heb ik een nieuwe functie gemaakt om de window te sluiten.

 Al met al heb ik geleerd over veel verschillende bibliotheken en modules van python zoals datetime, sqlite3, random, tkinter, PIL en os.

Bij de getPrompt had ik een     ^^^^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'config'
error.
Om dit op te lossen heb ik ChatGPT gebruikt. Deze raadde me aan om de volgorde van code te veranderen.

