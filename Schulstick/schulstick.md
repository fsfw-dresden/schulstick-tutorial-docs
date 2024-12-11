# Schulstick

Der [**Schulstick**](https://schulstick.org/) ist eine [freie](https://de.wikipedia.org/wiki/Free/Libre_Open_Source_Software) Lern-, und Arbeitsplattform für lernende jeden Alters. Für unterschiedliche Zielgruppen existieren [verschiedene Varianten](https://github.com/fsfw-dresden/usb-live-linux/tree/main/variants.build). 

Ein besonderer Wert des Schulsticks besteht darin, eine einheitliche **Plattform** für eine Vielzahl speziell angepasster und getesteter **Tutorials** zu bieten. Ziel ist es Nutzern (Schülern, Lehrkräften und Autodidakten) einen besonders zuverlässigen, niedrigschwelligen, frustfreien und effizienten Einstieg in neue Themen, Technologien und Softwarelösungen zu ermöglichen.

Lehrninhalte für den Stick sind [freies Wissen](https://fsfw-dresden.de/themen.html) und werden durch eine **Community** gemeisam erstellt und gepflegt.


## Download

Die aktuellste Version des Schulsticks, die wir im Hackathon verwenden möchten, kann [hier heruntergeladen](https://schulstick.winzlieb.eu/) werden.

Der letzte stabile Release und die offiziele Anleitung sind auf der Seite der [FSFW-Dresden](https://fsfw-dresden.github.io/schulstick-page/#download-und-bespielen-eines-usb-sticks).


## Start per VM

Erstellt euch gerne selber einen Stick oder holt ein einen bei uns ab.

Ein anderer Weg den Schulstick einfach zu testen ist, das Image in einer Virtuelen Machine zu starten.

Unter Linux empfehlen wir folgenden Befehl auf der Kommandozeile:

```sh
qemu-kvm -m 4G $(SCHULSTICK_IMAGE).img
```

Wobei die Variable `$(SCHULSTICK_IMAGE).img` mit dem Pfad zur im letzten Schritt veruntergeldenen Datei ersetzt wird.



## Lerninhalte Erstellen

Mit dem Wissen aus dieser Dokumentation ist es Lehrkräften möglich, für die eigenen Bedürfnisse angepasste Varianten des Schulsticks zu erstellen.
Zum starten könnt ihr unserer [Quickstart-Anleitung](../Quickstart/quickstart.md) folgen. Sie wird künfig auch selbst als Kurs auf den Schulsticks mit ausgeliefert.
