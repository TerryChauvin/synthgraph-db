# Journal d'extraction PMC5302706

- Découpage : deux voies de base seulement, `ZnO_HT` (matériau, section 2.1) et `ZnO_IDT_sensor` (dispositif, sections 2.3 à 2.6). L'article ne balaie aucun paramètre de synthèse ; ce qui varie (gaz, concentration, gaz porteur air/azote, température ambiante ou 200 °C, UV, humidité) est une condition d'essai du capteur, donc des `outcomes` et non des branches (règle « tests du matériau fini »).
- Résultats de capteur rangés sur la voie `device` et pas sur le matériau (pas de doublon) ; XRD, Raman, FE-SEM restent sur `ZnO_HT`.
- Réponses à NO2 à 1 ppm : le texte donne « c.a. 600 % / 230 % » et « 430 % / 340 % », la Table 1 donne 600/232 et 431/341. Rangées entières de la Table 1 retenues en citation (valeurs plus précises) ; l'écart est noté en doute.
- Réponse à NO2 à température ambiante dans l'obscurité (« first cycle … 50% in N2 and 30% in air », Fig. 8a) : phrase citée telle quelle, deux résultats (azote 50, air 30), « c.a. » non recopié dans la valeur.
- Les t90 (880 s air, 700 s azote) : la phrase ne donne pas la température ; le nom de la propriété ne la contient donc pas (doute noté).
- Sélectivité « more than 105 times » : exposant perdu dans le texte source ; recopié en `value_text` sans rétablir 10^5, doute noté.
- Figure 16 (histogramme de synthèse) lue pour quatre valeurs absentes du texte : H2 1 % à 200 °C (≈ −95 % azote, ≈ −85 % air) et variation d'humidité 8–20 % à 200 °C (≈ −23 % azote, ≈ −41 % air), 2 chiffres significatifs, `from_figure`, citation = légende. NH3 à 10 ppm non lu (barres de moins de 10 %, peu lisibles) ; NO2 non lu (valeurs écrites dans le texte). Figure 2 consultée pour la morphologie (plaquettes et longs fils), non utilisée pour une valeur.
- Morphologie contradictoire entre résumé (nanoparticules et nanowires), Table 1 (nanotubes et nanoparticles) et section 3.1 (nanobars, nanotubes, nanolumps) : section 3.1 retenue, doute noté.
- Durée de réaction « two hours » : `value_text`, pas de nombre (le nombre ne figure pas dans la citation).
- Séchage du ZnO « at a RT » sous 15 mbar : température en `value_text` « RT », pression 15 mbar en paramètre.
- Fournisseur « Simga Aldrich » recopié tel quel (faute de frappe de l'article) ; phrase « Materials » citée en `supplier_quote` pour NaOH, éthanol (POCH), nitrate de zinc, EDA. Pureté non donnée : `not_stated`.
- Hexane « pure hexane (produced by POCH) » : `purity: "pure"` recopié tel quel.
- `method_sources` : seul B39 (serveur de gaz, « described in an earlier paper ») retenu, rôle `autre`. B38 (équation du complexe Zn-EDA) écarté : renvoi d'interprétation du mécanisme, l'article ne dit pas avoir suivi cette méthode. B40 (Scherrer), B6 (Raman), B21 (travail antérieur sur ZnO en fleurs) écartés : analyse de données ou contexte.
- Échantillons sans voie : ZnO « flower-like » de l'article antérieur et les neuf matériaux de la Table 1, non synthétisés ici.
- Trois capteurs fabriqués, un seul présenté : une seule voie device.
- Aucune annexe (pas de section Supporting Information dans le fichier ; l'article n'en cite pas). Aucune étape de refroidissement chiffrée : `cooling_rate` déclaré non cité.
