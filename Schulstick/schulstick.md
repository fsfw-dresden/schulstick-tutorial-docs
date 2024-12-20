# Schulstick

Der [**Schulstick**](https://schulstick.org/) ist eine [freie](https://de.wikipedia.org/wiki/Free/Libre_Open_Source_Software) Lern-, und Arbeitsplattform für lernende jeden Alters. Für unterschiedliche Zielgruppen existieren [verschiedene Varianten](https://github.com/fsfw-dresden/usb-live-linux/tree/main/variants.build). 

Ein besonderer Wert des Schulsticks besteht darin, eine einheitliche **Plattform** für eine Vielzahl speziell angepasster und getesteter **Tutorials** zu bieten. Ziel ist es Nutzern (Schülern, Lehrkräften und Autodidakten) einen besonders zuverlässigen, niedrigschwelligen, frustfreien und effizienten Einstieg in neue Themen, Technologien und Softwarelösungen zu ermöglichen.

Lehrninhalte für den Stick sind [freies Wissen](https://fsfw-dresden.de/themen.html) und werden durch eine **Community** gemeisam erstellt und gepflegt.


## Fertige USB-Sticks

Für **SchülerInnen und Lehrkräfte** stellen wir gerne USB-Sticks zur Verfügung, auf denen die Schulstick-Software installiert ist.
Kontaktiert uns bei Bedarf oder anderen Fragen gerne unter **`info@schulstick.org`** oder nutzt unser [Web-Formular](https://survey.opensourceecology.de/index.php?r=survey/index&sid=281135).


## Download

<!-- temporärer Workaround -->
Die aktuellste Version des Schulsticks, die wir im Hackathon verwendet haben und zum Erstellen von Tutorials empfehlen, kann [hier heruntergeladen](https://schulstick.winzlieb.eu/) werden.
Unter der URL gibt es 2 Dateien zur Auswahl:
* Wer weiß, wie ein „**\*.img.gz**“ entpackt wird, kann die **15GB** große Datei herunter laden.
* Ansonsten kann die unkomprimierte „**\*.img**“ Datei (**25GB**) nutzen.

Der letzte stabile Release und die offiziele Anleitung sind auf der Seite der [FSFW-Dresden](https://fsfw-dresden.github.io/schulstick-page/#download-und-bespielen-eines-usb-sticks).

Künftig soll es auf auf der offiziellen Seite aktuelle und deutlich kleinere Images geben.


## Den Schulstick starten

Folgende Anleitung setzt voraus, dass die „**\*.img**“ Datei des Schulsticks (wie im letzten Schritt erklärt) heruntergeladen wurde.
Die Datei wird im folgenden als `$(SCHULSTICK_IMAGE).img` bezeichnet. Nutze statt dessen bitte den Dateinamen und Pfad zu der tatsächlichen Datei.

Wir erklären hier zwei verschiedene Möglichkeiten, den Schulstick zu nutzen:
* Installieren der „**\*.img**“ Datei auf einen **USB Stick** + **Booten**
* Start des Schulsticks in einer **Virtuellen Machine** (VM)


### „Installation“ (einen USB-Stick mit der img-Datei bespielen)

Vorab für Linux-Benutzer, die folgenden Befehl verstehen, kann dieses Kapitel abgekürzt werden:

```sh
sudo dd if=$(SCHULSTICK_IMAGE).img of=/dev/$(USB-STICK) bs=4M status=progress 
```

Für alle, die sich auf der Kommandozeile (noch) nicht wohlfühlen, wird das grafische Programm **[Etcher](https://www.balena.io/etcher/)** empfohlen.
Damit könnt ihr die komprimierte Image-Datei auswählen und auf den Stick „flashen“.

#### USB-Stick

Wir empfehlen USB-Sticks mit mindestens 16 Gigabyte Speicherplatz.

Der USB-Stick enthällt eine „Persistenz-Partition“, auf der Inhalte gespeichert werden, die auch nach einem Neustarten des Betriebssystems auf dem Stick weiter verfügbar sind.
Diese Persistenz-Partition wird beim ersten Start automatisch so weit vergrößert, dass die gesammte auf dem Stick vorhandene Kapazität ausgenutzt wird.


### Starten (Booten) des USB-Sticks

Wenn ihr einen Schulstick von uns bekommen oder wie oben beschrieben selber „installiert habt“, ist es jetzt Zeit ihn zu starten :)

1. Ihr steckt den Stick in einen USB-Anschluss eures Rechners
2. Ihr startet den Rechner bzw. ihr startet ihn neu („Reboot“)

Wenn ihr Glück habt, Startet jetzt der Schulstick oder ihr werdet gefragt ob ihr ihn starten wollt…

Wie sich euer Rechner beim Starten verhält, kann sehr unterschiedlich sein. Hier ein paar allgemeine Hinweise die hoffentlich in vielen Fällen helfen.

Wenn ihr nicht weiterkommt: fragt gerne eure Lehrer, euren Administrator oder uns.

* Möglicherweise öffnet sich ein „**[Boot-Menü](https://de.wikipedia.org/wiki/Bootmen%C3%BC)**“ indem ihr das „Boot-Medium“ auswählen könnt. Wählt hier bitte den „USB“-Stick aus.
  * Bei vielen Computern kann das „Boot-Menü“ beim starten über eine Taste geöffnet werden. Diese wird oft beim starten irgendwo klein in Englisch angezeigt.
* Bei manchen Computern muss die „**[Boot-Reihenfolge](https://duckduckgo.com/?q=boot+reihenfolge)**“ im „**[Bios](https://de.wikipedia.org/wiki/BIOS)**“ geändert werden.
* In manchen Fällen muss im „Bios“ die Option „**[Secure-Boot](https://www.thomas-krenn.com/de/wiki/UEFI_Secure_Boot)**“ deaktiviert werden.
* In manchen Fällen ist es wichtig, ob im „Bios“ „**[UEFI](https://de.wikipedia.org/wiki/Unified_Extensible_Firmware_Interface)**“ oder „Legacy-Boot“ ausgewählt wurde. Der Schulstick sollte eigentlich mit beiden Optionen funktionieren.
* Wie man auf eurem Computer ins Bios kommt, wird meistens beim Start angezeigt. Ansonsten steht es im Handbuch des Rechners bzw ihr findet dazu Informationen, wenn ihr nach dem Modell des Rechners oder der Version des Bios im Internet sucht…
Viel Erfolg ;)

Wenn der Schulstick erstmal bootet (startet) funktioniert hoffentlich alles. Lehnt euch bitte kurz zurück, es kann ein paar Minuten dauern. Bei Problemen, meldet euch gerne bei uns.


### Start per VM

Erstellt euch gerne selber einen Stick oder holt ein einen bei uns ab.

Ein anderer Weg den Schulstick einfach zu testen ist, das Image in einer Virtuelen Machine zu starten.

Unter Linux empfehlen wir folgenden Befehl auf der Kommandozeile:

```sh
qemu-kvm -m 4G $(SCHULSTICK_IMAGE).img
```

Wobei die Variable `$(SCHULSTICK_IMAGE).img` mit dem Pfad zur im verherigen Schritt heruntergeldenen Datei ersetzt wird.



## Lerninhalte Erstellen

Mit dem Wissen aus dieser Dokumentation ist es Lehrkräften möglich, für die eigenen Bedürfnisse angepasste Varianten des Schulsticks zu erstellen.
Zum starten könnt ihr unserer [Quickstart-Anleitung](../Quickstart/quickstart.md) folgen.
<!-- Sie wird künfig auch selbst als Kurs auf den Schulsticks mit ausgeliefert. -->
