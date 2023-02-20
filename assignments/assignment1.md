# Zadanie 1

V prvom zadaní budete aplikovať známe metódy učenia posilňovaním pri riešení štandardných problémov z knižnice `gym`. Zámerom zadania je získať skúsenosti s aplikáciou algoritmov na riešenie jednoduchých problémov, s vyhodnotením výsledkov, s ladením hyperparametrov a s porovnávaním rôznych prístupov.

## Úloha
Vašou úlohou je implementovať a aplikovať základné algoritmy učenia posilňovaním pre riešenie štandardných problémov, ktoré slúžia ako benchmarky pre takéto algoritmy. V druhom týždni vám bude pridelený problém, ktorý musíte vyriešiť minimálne tromi algoritmami. Výber algoritmov je na vás, nesmiete však použiť algoritmy s neurónovými sieťami. Následne naimplementujete vybrané algoritmy, aplikujete ich pri riešení problému, a vyhodnotíte ich. K tomu musíte vykonať niekoľko experimentov s rôznymi nastaveniami hyperparametrov, výsledky vyhodnotiť a takto prispôsobiť hodnoty hyperparametrov. Pri jednom nastavení hyperparametrov vykonajte niekoľko testovacích behov, a výsledky spriemerujte. Vaše výsledky následne potrebujete zhrnúť v tabuľke. Pri vyhodnocovaní algoritmov môžete použiť rôzne metriky, ako napríklad rýchlosť trénovania, miera konvergencie, najlepšia dosiahnutá politika (*policy*), stabilita natrénovanej politiky, atď.

### Prostredia
* Mountain Car - [pôvodná](https://gym.openai.com/envs/MountainCar-v0/) alebo [spojitá](https://gym.openai.com/envs/MountainCarContinuous-v0/) verzia
* Frozen Lake - verzia [4x4](https://gym.openai.com/envs/FrozenLake-v0/), resp. [8x8](https://gym.openai.com/envs/FrozenLake8x8-v0/)
* [Cart Pole](https://gym.openai.com/envs/CartPole-v1/)
* [Acrobot](https://gym.openai.com/envs/Acrobot-v1/)
* [Pendulum](https://gym.openai.com/envs/Pendulum-v0/)
* [Taxi](https://gym.openai.com/envs/Taxi-v3/)
* prípadne môžete použiť vlastné prostredie po konzultácii s cvičiacim (okrem Gridworld; vybrať si musíte do konca piateho týždňa)

### Algoritmy
Pri vypracovaní zadania môžete použiť ľubovoľný algoritmus pre učenie posilňovaním, ktorý nevyužíva neurónovú sieť. Ak si nie ste istí, výber algoritmov prekonzultuje s vyučujúcimi. Nápady pre algoritmy:

* policy iteration
* value iteration
* Monte Carlo metódy
* hierarchické učenie
* Q-learning
* SARSA
* Double Q-learning
* ...

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
Vaše riešenia odovzdávate cez MS Teams ako jeden zip súbor s hore uvedenou štruktúrou. Termín odovzdania je **6. 4. 2022** (štvrtok). Po odovzdaní vaše riešenie musíte aj obhájiť - termíny budú vypísané pre posledné dva týždne semestra.

## Hodnotenie
Za zadanie môžete získať maximálne 10 bodov, pričom bodové rozdelenie je nasledovné:

* **použité metódy a algoritmy**: 3 x 2 body - hodnotí sa správnosť prístupu a riešenia
* **dokumentácia**: 2 body - hodnotí sa kvalita dokumentácie vašej práce
* **obhajoba**: 2 body - hodnotí sa pochopenie kódu, obhajoba slúži aj ako kontrola originality; pri riešení môžete vychádzať z dostupných tutoriálov a ukážok, avšak predpoklad je, že kódu budete aj rozumieť a budete ho vedieť vysvetliť
