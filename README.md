# Diplomarbeit_Problem

## First Steps:
### Buildozer Installieren
Buildozer Installation: https://buildozer.readthedocs.io/en/latest/installation.html
### Directory Setup
main.py, main.kv und alle png files in einen Ordner verschieben
## Man benötigt
 * python3
 * kivy
 * kivymd
 * xcamera (von kivy_garden)
## Was dann?
buildozer init
buildozer.spec wird erstellt...
Diese Bearbeiten:
  * Zeile 4: Title
  * Zeile 39: Requirements   
  * Zeile 88: Permissions
    * Permissions siehe [hier](https://developer.android.com/reference/android/Manifest.permission) 
## Wichtigsten Buildozer befehle:
* Buildozer android debug... Kompiliert und erstellt dann im bin-Ordner die apk file
* buildozer android deploy... vorheriges + installiert apk direkt am Handy, wenn es angeschlossen ist + [USB-Debugging](https://mobilsicher.de/ratgeber/usb-debugging-aktivieren) aktiviert ist
* buildozer android deploy run... vorheriges + führt App am Handy direkt aus
* buildozer android deploy run logcat ... vorheriges + startet zusätzlich logcat
* ... Komplette Liste an Befehlen mit buildozer help



  
