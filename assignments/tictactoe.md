# Tic-Tac-Toe

Tic-Tac-Toe je jednoduchá hra, v ktorej hráči striedavo umiestňujú znaky `O` a `X` na hracie pole 3x3, a vyhrá ten, ktorému sa skôr podarí umiestniť vedľa seba tri rovnaké znaky, pričom tieto znaky môžu byť v tom istom riadku, v tom istom stĺpci alebo na rovnakej diagonále. Pre hru neexistuje výherná politika, existuje ale spôsob, ako predísť prehre (aspoň  pre prvého hráča).

Agent má k dispozícii deväť akcií: umiestnenie znaku na danú pozíciu, pričom začíname číslovať v ľavom hornom rohu. Ak agent chce dať na pozíciu, na ktorej sa znak už nachádza, svoj krok nevyužije a nasleduje jeho protihráč.

[Hru si môžete zahrať tu](https://playtictactoe.org).

## Štruktúra projektu
V kostre riešenia nájdete priečinok s názvom *tictactoe*, ktorý obsahuje nasledovné súbory:

* `tictactoe.py` - implementácia hry Tic-Tac-Toe s rozhraním, ktoré poznáte z OpenAI gym. Vaši agenti môžu komunikovať s týmto prostredím cez funkcie `reset` (pre získanie počiatočného stavu - prázdne hracie pole) a `step` (pre aktualizáciu prostredia na základe akcie agenta - umiestnenie daného znaku na pozíciu).
* `bots.py` - niekoľko botov, ktorých môžete ale nemusíte využiť pri trénovaní, resp. pri vyhodnocovaní vášho riešenia. `RandomBot` vždy vyberie náhodnú pozíciu a svoj znak umiestní na danú pozíciu. `OneStepBot` vyberie výhernú akciu, ak taká existuje, v opačnom prípade svoj znak umiestní náhodne. `TwoStepBot` vždy vyberie výhernú akciu, alebo zablokuje možnú výhernú akciu protihráča, v opačnom prípade svoj znak umiestní náhodne.
* `main.py` - obsahuje ukážkové testovanie hry s dvomi agentami. Nasimuluje sa 1000 hier, a určí sa, v koľkých vyhrá hráč 1, hráč 2, a koľkokrát nastane remíza.
* `solution_tictactoe.py` - skript pre vaše riešenie, zadefinujte vlastným spôsobom agenta, teda triedu `StudentAgent`.

## Vyhodnotenie agentov
Pre túto hry vaše riešenia sa budú vyhodnocovať tak, že si agenti dvoch študentov zahrajú proti sebe 1000 nasimulovaných hier. Ak viac, ako 500 hier končí remízou, tak body za zápas sa delia, teda obaja študenti dostanú 1 bod. Ak agent niektorého študenta vyhrá minimálne 501 simulovaných hier, získa 3 body, a jeho protihráč žiadne body nezíska. Pre férovosť po 500 hrách sa poradie hráčov vymení, teda nikto nebude mať výlučnú výhodu prvého hráča.
