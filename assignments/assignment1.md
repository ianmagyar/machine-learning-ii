# Zadanie 1

V prvom zadaní budete aplikovať známe metódy učenia posilňovaním pri riešení štandardných problémov z knižnice `Gymnasium`. Zámerom zadania je získať skúsenosti s aplikáciou algoritmov na riešenie jednoduchých problémov, s vyhodnotením výsledkov, s ladením hyperparametrov a s porovnávaním rôznych prístupov.

## Úloha
Vašou úlohou je implementovať a aplikovať základné algoritmy učenia posilňovaním pre riešenie štandardných problémov, ktoré slúžia ako benchmarky pre takéto algoritmy. V prvom týždni vám bude pridelený problém, ktorý musíte vyriešiť minimálne dvomi algoritmami: jedným TD-algoritmom a jedným Monte Carlo algoritmom. Výber algoritmov je na vás, po konzultácii s cvičiacim si môžete upraviť zadanie tak, aby ste mohli použiť aj pkoročilejšie algoritmy (ak je to opodstatnené). Následne naimplementujete vybrané algoritmy, aplikujete ich pri riešení problému, a vyhodnotíte ich. K tomu musíte vykonať niekoľko experimentov s rôznymi nastaveniami hyperparametrov, výsledky vyhodnotiť a takto prispôsobiť hodnoty hyperparametrov. **Pri jednom nastavení hyperparametrov vykonajte niekoľko testovacích behov**, a výsledky spriemerujte. Vaše výsledky následne potrebujete zhrnúť v tabuľke. Pri vyhodnocovaní algoritmov môžete použiť rôzne metriky, ako napríklad rýchlosť trénovania, miera konvergencie, najlepšia dosiahnutá politika (*policy*), stabilita natrénovanej politiky, atď.

### Prostredia
* Mountain Car - [pôvodná](https://gymnasium.farama.org/environments/classic_control/mountain_car/)
* Mountain Car - [spojitá](https://gymnasium.farama.org/environments/classic_control/mountain_car_continuous/)
* [Acrobot](https://gymnasium.farama.org/environments/classic_control/acrobot/)
* [Pendulum](https://gymnasium.farama.org/environments/classic_control/pendulum/)
* [Inverted Pendulum](https://gymnasium.farama.org/environments/mujoco/inverted_pendulum/)
* [Inverted Double Pendulum](https://gymnasium.farama.org/environments/mujoco/inverted_double_pendulum/)
* [Lunar Lander](https://gymnasium.farama.org/environments/box2d/lunar_lander/)
* prípadne môžete použiť vlastné prostredie po konzultácii s cvičiacim (okrem Gridworld a Cart Pole; vybrať si musíte do konca piateho týždňa)

### Algoritmy
Pri vypracovaní zadania môžete použiť ľubovoľný algoritmus pre učenie posilňovaním, ktorý nevyužíva neurónovú sieť. Musíte porovnať aspoň jeden algoritmus TD-učenia a jeden Monte Carlo algoritmus. Ak si nie ste istí, výber algoritmov prekonzultuje s vyučujúcimi.

## Štruktúra riešenia
Vaše riešenie musí mať nasledovnú štruktúru:

1. kódová implementácia algoritmov - skripty v Python 3, jeden súbor na každý algoritmus. Kód musí byť spustiteľný a okomentovaný. Ak používate pomocné knižnice, všetky musíte uviesť v osobitnom súbore `requirements.txt` s príslušnou verziou knižnice. Skript musí podporiť aj načítanie uloženého agenta. Pri implementácii môžete použiť už existujúce ukážkové riešenia, zdroj ale musíte uviesť v komentároch.
2. uložení natrénovaní agenti - minimálne jeden (najlepší) agent natrénovaný pre každý algoritmus. Môžete odovzdať aj viac riešení, tieto ale musia byť jednoznačne označené.
3. dokumentácia - súbor s porovnávaním implementovaných algoritmov a dokumentáciou vašej práce. Obsah dokumentácie:

    * úvod a popis riešeného problému (stavový priestor, možné akcie, podmienky vyriešenia problému) - uveďte všetky zmeny, ktoré ste urobili, napr. diskretizácia stavového priestoru a pod.
    * použitá funkcia odmeny (*reward function*)
    * pseudokódy implementovaných algoritmov a spôsob ich aplikácie na riešený problém (či ste potrebovali upraviť algoritmus, a ak áno, ako) - všetky informácie, ktoré človek potrebuje k zreprodukovaniu vášho riešenia. Ak ste uvažovali nad použitím ďalších algoritmov, ale napokon ste ich nedokázali aplikovať, tiež ich spomeňte spolu s dôvodom, prečo neboli použiteľné.
    * dokumentácia experimentov - s akými hodnotami hyperparametrov ste testovali jednotlivé algoritmy spolu s výsledkami. Výsledky uveďte v tabuľkovej forme, musíte vykonať minimálne desať pokusov s každým algoritmom.
    * porovnanie algoritmov na základe vami zvolených kritérií - tabuľková alebo grafová podoba.

## Odovzdávanie
Vaše riešenia odovzdávate cez MS Teams ako jeden zip súbor s hore uvedenou štruktúrou. Termín odovzdania je **5. 4. 2024** (piatok). Po odovzdaní vaše riešenie musíte aj obhájiť - termíny budú vypísané pre posledné dva týždne semestra.

## Hodnotenie
Za zadanie môžete získať maximálne 10 bodov, pričom bodové rozdelenie je nasledovné:

* **použité metódy a algoritmy**: 2 x 3 body - hodnotí sa správnosť prístupu a riešenia
* **dokumentácia**: 2 body - hodnotí sa kvalita dokumentácie vašej práce
* **obhajoba**: 2 body - hodnotí sa pochopenie kódu, obhajoba slúži aj ako kontrola originality; pri riešení môžete vychádzať z dostupných tutoriálov a ukážok, avšak predpoklad je, že kódu budete aj rozumieť a budete ho vedieť vysvetliť
