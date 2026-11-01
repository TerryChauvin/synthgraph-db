# Journal de la passe de complément — PMC5746929

Sonde : 7 points. Ajouts faits uniquement dans extractions/PMC5746929.json (aucune valeur existante modifiée).

Points de la sonde écartés ou déjà couverts
- Rampe de chauffe, atmosphère, vide : tous trois relèvent de la TGA (azote, 10 °C/min, 40–700 °C) et du séchage sous vide des échantillons avant TGA. Déjà dans `characterizations.conditions` de la TGA (4 voies matériau). Aucune étape de synthèse chauffée : pas de rampe, pas d'atmosphère de synthèse déclarée.
- Vide (ESEM « low vacuum mode ») : déjà dans les conditions de l'ESEM.
- Mesure catalyse/adsorption : faux positif (mot « degradation » des groupes alkyle en TGA), aucune catalyse ni adsorption dans l'article. Seule retenue la température de début de perte de masse continue (300 °C), ajoutée comme résultat TGA.
- pH : le pH 0,5 de HNO3 était déjà sous le nom `acid_solution_ph` à l'étape 4 ; ajouté à l'étape 6 (sol organique) avec le même nom, par cohérence interne.

Ajouts
- Sample_1_GPTMS étape 1 : `addition_mode` = dropwise et `addition_order` (ZPO ajouté à l'acétoacétate d'éthyle), citation de la phrase de synthèse ; `addition_rate` déclaré non cité (pas de débit en gouttes/min).
- Étape 7 : `addition_order` non cité (on ne sait pas quel sol est versé dans l'autre). Étapes 5 et 9 : `ultrasound_frequency` non cité (déjà fait à l'étape 3).
- Voie de base : `repetitions` (nombre de lots) et `vessel` (récipient) non cités ; cherchés dans 3.1, 3.2 et partout dans le texte.
- Résultats : diamètre moyen ESEM d'environ 150 nm pour les échantillons 3 et 4 (texte, section ESEM) ; début de perte de masse continue après 300 °C pour les échantillons 1 à 4 (la phrase vaut pour tous les matériaux modifiés).
- Film_1_GPTMS : `repetitions` (nombre d'immersions) non cité à l'étape de dépôt ; `wash_volume` non cité à l'étape de nettoyage du substrat.

Non fait
- Échantillon M (ZnO commercial) : DLS 250 nm / P1 162 nm, CA 68°, rugosité 2,69 nm n'ont pas de voie ; déjà signalé dans les doutes existants, pas de nouvelle voie créée.
- Conditions de mesure : toutes les techniques de résultats (DLS, ESEM, TEM, TGA, XRD, FTIR, angle de contact, ellipsométrie) avaient déjà instrument et conditions ; tension de l'ESEM non donnée dans l'article, rien à ajouter.
- Taille de cristallite : sans objet (matériaux modifiés amorphes en DRX).
