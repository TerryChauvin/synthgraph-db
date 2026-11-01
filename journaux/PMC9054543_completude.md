# Journal du test de complétude — PMC9054543

- Contrôle cellule par cellule des Tables 1 à 5 contre les `outcomes` de chaque voie : tout ce qui n'est pas « — » était déjà présent. La liste A ne signalait donc que les temps de rétention (colonne RT de la Table 5), que l'extraction avait ignorés.
- Temps de rétention : rangés non pas en `outcomes` d'un échantillon (ce sont des propriétés de l'analyse, pas du matériau) mais en entrées `characterizations` de MZ-27, technique « GC-MS (identification des pics, Table 5) », une par composé (42), temps dans `conditions`, citation = la rangée de la table. MZ-27 porte déjà les 4 colonnes de la Table 5 ; HZ-27 n'a pas reçu de doublon.
- Cellules « — » (non détecté, note de table) : non ajoutées, l'absence est déjà lisible par l'absence de valeur ; 36 cellules, aucune information de synthèse.
- Les nombres de l'introduction ne sont pas dans la liste A (non balayée) : ajoutés d'après ma lecture complète, dans `comparisons`. Nishino : l'introduction cite cit14, la discussion répète « >80% » avec cit15 ; une seule entrée (cit14), doute écrit.
- Valeur de littérature « >90 », « >50 », « >80 » : `value_text` avec le signe, unité `%`, car le nombre seul perdrait la borne.
- Énergies de dissociation PP/HDPE (cit38) : en `comparisons` avec `route` MZ-27, car l'article s'en sert pour expliquer le rendement liquide plus élevé du PP.
- Artetxe (58 wt%) rattaché à la route HZ-150, car l'article le compare à son rendement maximal de 37.6 % obtenu sur HZ-150.
- Équations de rendement : citation = la phrase de définition des variables (les équations sont collées au texte avec leurs numéros, 1TGP…2YL…, mauvaise citation). Les équations dans `conditions` sont retranscrites depuis le texte ; incohérences d'unité (TGP en mL g−1 × 100 %, YG en fraction) signalées en doute, non corrigées.
- `not_stated` de route sur MZ-27 pour les conditions de mesure introuvables (dégazage BET, tension SEM, rayonnement XRD, vitesse de chauffe TGA, dimensions du réacteur) : cherchés par mot-clé (degas, kV, Cu K, heating rate, diameter), absents. Pas de champ `not_stated` sur les caractérisations, d'où le niveau route.
- Branches HZ-27, HZ-80, etc. sans entrée `characterizations` propre : conditions de mesure communes, portées par la voie de base MZ-27, pas dupliquées.
- Aucune figure ouverte : toutes les valeurs chiffrées des figures (TGA) étaient déjà lues par l'extraction d'origine ; rien de chiffré absent du texte n'est porté par les Fig. 1–5, 7.
- Ajouts seulement : comparaison structurelle avec la version précédente du JSON, aucune valeur perdue ni modifiée.
