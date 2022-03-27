# Fenster API

API um Fenster zu erzeugen und Projekte in Hauptprogramm einzubinden.

WARNUNG: Projekt noch in Entwicklung



## Dokumentation


### "Installieren"

Im Projektordner muss die Datei `fenster.json` angelegt werden. Durch anlegen dieser Datei wird das Projekt von `FensterAPI` registriert. Die Datei muss folgenden Kopf haben:
```
"Projektname" : "[Projektname]"
"Projektversion" : "[Version]"
"stable" : true / false
```


## Beispiel

### `fenster.json`

```json
"Projektname" : "Beispiel"
"Projektversion" : "1.0.4.3"
"stable" : true
```