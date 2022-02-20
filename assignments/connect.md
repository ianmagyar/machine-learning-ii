# Connect Four

Connect Four je hra, v ktorej hráči striedavo umiestňujú červené a žlté znaky na hracie pole 7x6, pričom znaky vkladajú zhora, a tie padnú na najnižšiu voľnú pozíciu v danom stĺpci. Tým pádom aj keď hracie pole je väčšie v porovnaní s hrou TicTacToe, počet akcií hráča je stále limitovaný - sú to stĺpce s voľným miestom. Ak agent vyberie stĺpec, v ktorom už nie sú voľné pozície, svoj krok nevyužije a nasleduje jeho protihráč. Hru vyhrá ten, ktorému sa skôr podarí prepojiť štyri znaky, pričom tieto znaky môžu byť v tom istom riadku, v tom istom stĺpci alebo na rovnakej diagonále.

[Hru si môžete zahrať tu](https://www.cbc.ca/kids/games/play/connect-4).

## Štruktúra projektu
V kostre riešenia nájdete priečinok s názvom *connectfour*, ktorý obsahuje nasledovné súbory:

* `connectfour.py` - implementácia hry Connect Four s rozhraním, ktoré poznáte z OpenAI gym. Vaši agenti môžu komunikovať s týmto prostredím cez funkcie `reset` (pre získanie počiatočného stavu - prázdne hracie pole) a `step` (pre aktualizáciu prostredia na základe akcie agenta - vkladanie znaku danej farby do istého stĺpca).
* `bots.py` - niekoľko botov, ktorých môžete ale nemusíte využiť pri trénovaní, resp. pri vyhodnocovaní vášho riešenia. `RandomBot` vždy vyberie náhodnú pozíciu a svoj znak umiestní na danú pozíciu. `OneStepBot` vyberie výhernú akciu, ak taká existuje, v opačnom prípade svoj znak umiestní náhodne. `TwoStepBot` vždy vyberie výhernú akciu, alebo zablokuje možnú výhernú akciu protihráča, v opačnom prípade svoj znak umiestní náhodne.
* `main.py` - obsahuje ukážkové testovanie hry s dvomi agentami. Nasimuluje sa 1000 hier, a určí sa, v koľkých vyhrá hráč 1, hráč 2, a koľkokrát nastane remíza.
* `solution_connect.py` - skript pre vaše riešenie, zadefinujte vlastným spôsobom agenta, teda triedu `StudentAgent`.

## Vyhodnotenie agentov
Pre túto hry vaše riešenia sa budú vyhodnocovať tak, že si agenti dvoch študentov zahrajú proti sebe 1000 nasimulovaných hier. Ak viac, ako 500 hier končí remízou, tak body za zápas sa delia, teda obaja študenti dostanú 1 bod. Ak agent niektorého študenta vyhrá minimálne 501 simulovaných hier, získa 3 body, a jeho protihráč žiadne body nezíska. Pre férovosť po 500 hrách sa poradie hráčov vymení, teda nikto nebude mať výlučnú výhodu prvého hráča.
