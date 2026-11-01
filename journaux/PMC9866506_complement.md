# Complément PMC9866506 — tableaux du texte (2 lus)

- Tableaux lus : Table 1 (paramètres de maille a, b, c, volume, taille de cristallite, contrainte de réseau, pour FV500, FV600, FV700 et la référence « Standard ») et Table 2 (volume et taille de pores, densité tassée, surface BET).
- Ajouté : 30 résultats, 10 par voie (FV500, FV600, FV700), chaque rangée rattachée par le nom de l'échantillon écrit dans la rangée ; propriétés suffixées `_Table1` / `_Table2` pour ne pas se confondre avec les lectures de figure existantes.
- Les lectures sur la figure 2 déjà extraites (cristallite 14/14/16 nm, BET 60/34/25 m2/g, densité tassée 0,1/0,2/1,1 g/ml) concordent avec les valeurs exactes des tableaux (13.802/14.373/15.937 ; 60.030/34.222/24.616 ; 0.105/0.218/1.057). Aucune valeur existante modifiée.
- Unités : l'en-tête du tableau 1 ne donne pas d'unité pour a, b, c, donc `unit` vide ; le volume est « A°3 » tel qu'écrit. Pour le volume de pores, l'en-tête écrit « m3/g » avec des valeurs en 10-8 : unité non corrigée, valeur en `value_text` car le nombre n'apparaît pas tel quel dans la citation.
- Laissé : rangée « Standard » du tableau 1 (6.718, 8.060, 9.254, 462.459), qui est la référence JCPDS et non un échantillon synthétisé.
- Incohérence déjà signalée et confirmée : le tableau 2 donne des tailles de pores (20.8, 5.5, 5.0 nm) alors que le texte parle de nature non poreuse.
- Un doute ajouté (tableaux lus, unités, rangée Standard).
- Contrôle : `load.py check` 0 erreur, 0 avertissement.
