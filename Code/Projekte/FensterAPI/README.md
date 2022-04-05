# Fenster API

API um Fenster zu erzeugen und Projekte in Hauptprogramm einzubinden.

WARNUNG: Projekt noch in Entwicklung (heißt: funktioniert noch nicht)

## Dokumentation

### "Installieren"

Im Projektordner muss die Datei `data.json` angelegt werden. Durch anlegen dieser Datei wird das Projekt von `FensterAPI` registriert. Die Datei muss folgenden Kopf haben:

```
"Projektname" : "[Projektname]"
"Projektversion" : "[Version]"
"stable" : true / false
"auszuführendeDatei" : "[Dateiname]"
"Terminal" : true / false
```

## Beispiel

### `data.json`

```json
"Projektname" : "Beispiel"
"Projektversion" : "1.0.4.3"
"stable" : true
"auszuführendeDatei" : "Beispiel.py"
"Terminal" : true
```
