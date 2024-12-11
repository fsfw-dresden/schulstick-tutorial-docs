# Quickstart

Dieser Quickstart zeigt, wie neue Kurse für den Schulstick erstellt werden.


## Markdown

Kurse für den Schulstick werden in [Markdown](../Markdown/markdown.md) oder der Erweiterung [LiaScript](../LiaScript/liascript.md) erstellt.
Im folgenden verwenden wir den Editor LiaEdit. Mit ihm können alle unterstützen Funktionen genutzt werden.

Wenn in diesem Schritt etwas nicht funktioniert, kann aber auch jede andere [Markdown-Editor](../Markdown/markdown.md) verwendet werden.


## LiaEdit

Wir empfehlen den Editor LiaEdit.

> Als erstes müssen wir den [**Editor über diesen Link öffnen**](https://liascript.github.io/LiveEditor/?/edit)

Es sollte sich ein Browserfenster öffnen, dass etwa so aussieht:

`Todo` Screenshot

Auf der linken Seite ist eine schwarzes Texteingabefeld. Dort hinein werden wir LiaScript oder anderes Markdown schreiben.

Auf der rechten Seite sehen wir zunächst einen kurzen Einführungtext, der die Benutzung des Editors erklärt.


### Hallo Welt

Wir wollen jetzt unser erstes LiaScript-Dokument erstellen.

Dafür klicken wir in das **schwarze Texteingabefeld** und fangen an zu tippen. Als Beispiel verwenden wir folgenes:

```md
# Mein erster Kurs

Hallo Welt
```

Die erste Zeile beginnt mit dem Zeichen **`#`**. Zeilen die so anfangen werden in Markdown als Überschrift verstanden.

> Wichtig: LiaScript erwartet, dass unser Dokument mindestens eine Überschrift hat. Nur die Inhalte unterhalb der ersten Überschrift werden angezeigt.

Wir drücken jetzt die Tastenkombination **`Strg + s`**. Wenn auf deiner Tastatur keine Taste mit `Strg` beschriftet ist, dann bestimmt mit `Ctrl`.

Sobald wir gleichzeitig die Tasten `Strg` und `s` gedrückt haben, sollte sich die rechte Hälfte des Fensters ändern und so aussehen:

`Todo` Screenshot


### eigene Inhalte

Wir können jetzt beliebig oft etwas ändern und mit `Strg + s` sehen wie LiaScript es darstellt.

Du kannst dich jetzt hier frei ausprobieren. 

> Mehr [Infos zu LiaScript](../LiaScript/liascript.md)


## Kurse im Portal auf dem Lernstick einbinden

Um selbstgeschriebenen Markdown-Dateien als Kurs im Portal auf dem Lernstick verfügbar zu machen, mussen wir die erstellte Datei herunterladen und in einem Ordner ablegen, wo das Portal es erwartet.

In LiaEdit klicken wir oben rechts auf „**Menu**“ und wählen aus dem Abschnitt „**Download to**“ den Eintrag „README.md“. Indem wir mit Rechtsklick auf „README.md“ klicken, geht ein Kontextmenü des Browsers auf das uns „**Speichern unter**“ anbietet.

`Todo` Screenshot

Wir legen den neuen Ordner `~/.local/share/learning-portal/courses/draft/mein_quckickstart_tutorial/erste_lektion` an und speichern darin die Markdown-Datei. Der Dateiname ist egal, muss aber auf „.md“ enden.


### Portal neu starten

Wir können das Portal aus dem Startmenü auswählen und sollten unseren neuen Kurs sehen.

`Todo` Screenshot

Fertig :)

Später werden wir lernen, wie mit zusätzlichen Konfigurationsdateien weitere Funktionen des Portals genutzt werden können.
