# Journal d'extraction PMC8140147

- Article de physique (spectroscopie pompe-sonde, effet Autler-Townes) dont la seule synthèse est celle des nanocristaux de CsPbBr3 décrite dans « Methods, Sample preparation », avec toutes les quantités : accepté (pas de REJET), une seule voie de base `CsPbBr3-NC`, aucune branche car les auteurs ne font varier aucun paramètre de synthèse.
- L'oléate de césium (étapes 1-2) est préparé dans la même voie puis injecté (« 0.8 mL of the Cs-oleate solution ») : gardé comme réactif de rôle `intermediate` sans voie séparée, car il n'est pas isolé ni caractérisé à part (doute consigné).
- Deux lots d'acide oléique et d'octadécène (mélange du Cs et mélange du Pb) : deux entrées de réactif distinctes avec leurs quantités (0,5 mL / 6 mL puis 1 mL / 10 mL), la citation de la phrase correspondante.
- « A mixture of Cs2CO3 … was heated at 150 °C for 30 min and then cooled to 100 °C » : coupé en deux étapes (chauffage, refroidissement à 100 °C) avec la même phrase pour citation.
- « After this mixture was heated to 150 °C » : durée et vitesse de chauffe non citées, déclarées `not_stated` ; la durée de 5 s appartient à l'étape suivante (« held at 150 °C for 5 s »).
- Étape de dégazage : l'action `degas` n'entre pas dans la grille ; température et durée (100 °C, 30 min) extraites, pression « vacuum » en `value_text`.
- Purification : « precipitation fractionation with centrifugation in dried n-hexane » ne donne ni antisolvant, ni vitesse, ni durée ; une seule étape `centrifuge`, le n-hexane en réactif de rôle `wash`, cases déclarées non citées.
- Pureté et fournisseur : aucune phrase générale sur les réactifs dans l'article, donc `not_stated` pour tous.
- Résultats de matériau repris : arête 6,9 ± 0,7 nm (Méthodes, citée par la phrase du TEM ; le Résultats dit « average NC size of 6.9 nm »), E0 = 2,519 eV et largeur 0,079 eV, dipôles 19 D et 25 D, Δso = 0,58 eV. Ce sont des propriétés mesurées sur l'échantillon, pas des tests de dispositif.
- Figures (Fig. 1 ouverte) : spectres et dynamiques de pompe-sonde, sans résultat de synthèse comparé ; aucune valeur lue sur figure. Les Figs. 2-4 portent les mêmes mesures de décalage d'énergie en fonction de Δ ; non extraites car ce n'est pas une variation de synthèse.
- Annexe : le SI est présent dans le texte (S1-S7 et légendes) ; la figure S1 (TEM, histogramme) n'est qu'une légende sans données lisibles, mentionné dans `limite_reproductibilite`.
- Renvois de méthode : CR22 (Protesescu 2015) et CR39 (Yarita 2017) cités pour « previously reported hot-injection method », rôle `protocole_adapte` ; les renvois d'analyse (SWT, correction de champ local) ne sont pas des sources de méthode.
- Échantillons hors voie : l'échantillon de référence hexane (soustraction du fond) et la dilution du même lot pour la mesure UV de S4.
