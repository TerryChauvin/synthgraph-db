# Où prendre les constantes, et quoi recalculer

Pour le critique scientifique. But : ne pas refaire une recherche web pour une grandeur de manuel, et toujours citer la même source. Les valeurs ne sont pas copiées ici de mémoire : une valeur n'entre dans la table du bas qu'avec sa source, après lecture.

## Source à utiliser, par grandeur

| Grandeur | Source de référence (citer titre, éditeur, année, URL) |
|---|---|
| Point d'ébullition, de fusion, pression de vapeur (Antoine), densité, enthalpies | NIST Chemistry WebBook, https://webbook.nist.gov/chemistry/ |
| Solubilité dans l'eau, pKa, masse molaire, densité, fiche d'identité | PubChem (NIH), https://pubchem.ncbi.nlm.nih.gov/ (section « Chemical and Physical Properties », avec la source primaire indiquée par PubChem) |
| Réactivité dangereuse, incompatibilités (DMSO + halogénures d'acyle, HF, peroxydes, hydrazine) | NOAA CAMEO Chemicals, https://cameochemicals.noaa.gov/ ; fiche de données de sécurité du fournisseur (Sigma-Aldrich, Fisher) |
| Classification CLP/REACH (reprotoxique, CMR) | ECHA, https://echa.europa.eu/ |
| Définitions (mésopore, micro-émulsion, nucléophile, rendement quantique) | IUPAC Gold Book, https://goldbook.iupac.org/ ; rapports techniques IUPAC (voir `fondateurs.md`) |
| Longueurs d'onde X (Cu Kα1 = 1,540 56 Å), facteurs de diffusion | NIST X-ray Transition Energies Database, https://physics.nist.gov/PhysRefData/XrayTrans/ |
| Fiches de diffraction (phase, paramètres de maille) | Crystallography Open Database, http://www.crystallography.net/cod/ ; fiche JCPDS/ICDD citée par l'article |
| Diagrammes de phase, solubilité à chaud, transitions (anatase → rutile, etc.) | revues citées dans `fondateurs.md` ; à défaut, recherche web avec DOI vérifié |
| Pression de vapeur de l'eau en autoclave, masse volumique en température | NIST WebBook (fluide « water »), tables de vapeur |
| Fiche produit d'un réactif ou d'un équipement (pureté commerciale, solubilité dans le DMSO d'un fournisseur) | page du fabricant ; dire que c'est une fiche fournisseur |

## À recalculer systématiquement (sans source : arithmétique)

- **Moles** : chaque quantité (g, mL × densité, M × V) convertie en moles ; rapports comparés à la formule visée, au rôle annoncé (réducteur, ligand, gabarit) et au mot employé (« excès », « riche en plomb »).
- **Concentration impossible** : comparer à la solubilité (PubChem) et à la concentration du réactif pur (ex. HF anhydre ≈ 49,5 mol/L : une « solution 48 mol/L » n'existe pas).
- **Volume et pression en autoclave** : somme des volumes de liquide vs capacité du récipient ; taux de remplissage ; pression de vapeur à la température (NIST).
- **Température vs point d'ébullition** : récipient ouvert, à reflux ou fermé ? Bain à ultrasons, plaque, étuve : la consigne dépasse-t-elle le point d'ébullition du solvant ou de décomposition d'un réactif ?
- **Bragg** : d = λ / (2 sin θ) avec la longueur d'onde déclarée ; comparer aux distances annoncées.
- **Pores** : diamètre moyen 4V/S à comparer au diamètre BJH annoncé ; classes IUPAC (micro < 2 nm, méso 2–50 nm, macro > 50 nm).
- **Décalages spectraux** : vers les nombres d'onde ou longueurs d'onde plus bas = rouge pour λ, bleu pour ν̃ ; vérifier le mot employé.
- **Thermodynamique d'adsorption** : signe de ΔS cohérent avec ΔG(T) = ΔH − TΔS ; K adimensionnel ou non.
- **Rendement et conversion** : masse de produit possible à partir du réactif limitant.

## Valeurs vérifiées avec leur source (à compléter par les critiques)

| Grandeur | Valeur | Source (titre, éditeur, année, URL) | Vérifiée dans |
|---|---|---|---|
| Point d'ébullition du chlorure de thionyle | 76 °C (169 °F à 760 mmHg) | NOAA CAMEO Chemicals, « Thionyl chloride », https://cameochemicals.noaa.gov/chemical/1600 | PMC9043336 |
| Solubilité de Ca(OH)2 dans l'eau | 1,89 g/L à 0 °C ; 1,73 g/L à 20 °C | Wikipedia « Calcium hydroxide » (infobox), https://en.wikipedia.org/wiki/Calcium_hydroxide — source secondaire, à confirmer sur PubChem | PMC6928996 |
