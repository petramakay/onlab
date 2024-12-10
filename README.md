# Önálló laboratórium projekt

Az egyetemi laborban található egy UR3e típusú robotkar, mely .svg fájlokat tud kirajzolni az előtte lévő papírlapra. Feladatom az volt, hogy egy olyan programot készítsek, mely felismeri az adott képen lévő alakzatokat, majd azoknak megfelelő pozícióba és méretben lerajzolja a felismert obkejtumokat. A feladatom csak a macska illetve kutya objektumok megvalósítása volt, azonban a programot könnyű kiegészíteni úgy, hogy több más objektumra is működjön.

A kimenet egyetlen .svg fájl, melyet a robotkarnak átadnva, az ki tud rajzolni.

A "catanddog" mappában lévő catanddog.py maga a program, amely a képfelismerést elvégzi, majd előállítja a felismert objektumoknak megfelelő .svg fájlt. A programban mindent kommenteztem.

A cat.svg és dog.svg a két fájl, amelyet a program átméretez, majd a background.svg fájlt felhasználva előállítja az output.svg fájlt. A repositoryban található több jpg fájl, amelyeken a feladatot teszteltem.

A képfelismeréshez az Ultralytics YOLOv8 modelljét használtam, mely egy előre elkészített algoritmust ad az objektumfelismerés megvalósításához.
Ultralytics hivatalos oldala: https://docs.ultralytics.com/
