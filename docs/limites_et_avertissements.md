<p align="center"><a href="limits_and_warnings.md">English</a> · <b>Français</b></p>

# Limites et avertissements

Chiffres au 17 octobre 2026. À lire avant de refaire une synthèse à partir de la base.

## 1. Ce que la base garantit, et ce qu'elle ne garantit pas

Elle garantit que chaque valeur renvoie à une citation retrouvée mot pour mot dans le texte de l'article (47 059 citations contrôlées à l'audit des paliers 1 à 5, 100 % exactes), et elle rend explicite ce que l'article ne dit pas. Elle **ne garantit pas** qu'un protocole publié fonctionne, ni que l'article ait raison.

## 2. Ce qu'un chimiste ne doit pas croire sans vérifier

- **Annexes absentes.** Les annexes (Supporting Information) sont incluses seulement quand `enrich.py` a pu les récupérer ; les fichiers sources ne sont pas dans le dépôt (`corpus/si/` est ignoré par git, seul leur texte est ajouté à `corpus/text/`). Quand l'article renvoie à une annexe absente, une annotation `limite_reproductibilite` commence par « Annexe absente du dépôt : » : 78 annotations de ce type, sur 77 publications. Une voie incomplète garde un score de complétude bas.
- **Contradictions des articles conservées littéralement.** Une valeur étrange ou incohérente (teneur en cobalt plus lourde que le cobalt pur, « laser HeNe à 532 nm »…) est gardée telle qu'écrite et signalée en `limite_reproductibilite` ; elle n'est jamais corrigée. La critique scientifique a jugé 1 581 voies : 617 cohérentes, 791 douteuses, 56 incohérentes, 117 invérifiables (`plausibility`). Ces problèmes viennent des articles.
- **Mécanismes = hypothèses.** Les annotations `mecanisme_analyse` (476) sont des analyses de Claude, avec recherche web ; `mecanisme_auteurs` (434) rapporte ce que les auteurs avancent, lui aussi souvent non démontré. Ni l'un ni l'autre n'est un résultat de la base.
- **Sécurité.** Les annotations `securite_analyse` (350) sont des rappels de danger ajoutés par l'analyse, pas des consignes validées par un responsable sécurité. Les articles omettent souvent ces précautions (`securite_auteurs` : 39 seulement).
- **Valeurs lues sur figure** (`from_figure`) : approximatives, 2 chiffres significatifs au plus.
- **Les branches ne décrivent que des écarts.** Les paramètres non redéfinis viennent de la voie parente : utiliser `v_route_complete`.
- **DOI et sources non vérifiés.** Les critiques scientifiques citent des sources ; l'API Crossref est bloquée depuis le cloud. 575 DOI restent à vérifier depuis un poste qui y accède : `audits/palier_002_doi_a_verifier.txt` (144), `palier_003` (123), `palier_004` (132), `palier_005` (176) ; au palier 1, 8 DOI sur 10 tirés au hasard ont été confirmés par Crossref (`audits/palier_001_relecture.md`). Dans l'intervalle, tout lien bibliographique d'une critique scientifique est « à contrôler ». Une source inventée serait une anomalie bloquante d'audit ; deux à trois sources par palier ont été ouvertes à la main et conformes.
- **14 doutes ouverts** (`doubts.status = 'open'`) et des publications du palier 6 encore en cours de critique (2 sans critique au 17/10/2026) : leurs fiches peuvent évoluer. Seuls les paliers 1 à 5 (250 publications) sont audités.
- **Couverture.** 270 publications extraites sur une cible de 500 ; 12 articles rejetés à l'extraction (pas de synthèse exploitable). La base ne représente pas la littérature entière.

## 3. Licences : question ouverte

Les articles sont en accès libre sous licences Creative Commons, dont certaines sont NC (non commerciale) ou ND (pas de modification). Sur les 270 publications extraites : 191 CC BY, 49 CC BY-NC, 29 CC BY-NC-ND, 1 CC BY-NC-SA.

Le dépôt contient aussi `corpus/` (≈ 368 Mo, versionné : `text/`, `xml/`, `refs/`, `fig/`) : textes intégraux aplatis, XML d'origine, références et figures. Ces fichiers restent sous la licence de chaque article. Leur republication dans un dépôt public pose deux questions :

- les textes **ND** ont été transformés (aplatis, annexes ajoutées) ; selon la lecture de la licence, une adaptation distribuée n'est pas permise ;
- les textes **NC** ne peuvent être rediffusés dans un cadre commercial.

Les citations conservées dans la base sont de courts extraits (usage de citation) ; les fichiers `fiches/` et `synthese_dump.sql` en reprennent.

**Proposition (non tranchée) :** retirer `corpus/` du dépôt public (ajouter `corpus/` à `.gitignore`, le garder en local ou dans un dépôt privé) et fournir un script qui le reconstruit depuis Europe PMC (`fetch.py`, `sections.py`, `enrich.py`) à partir des PMCID. Contrepartie : les positions de caractères des citations dépendent du texte aplati, donc le script de reconstruction doit être déterministe, et `load.py` ne vérifierait plus les citations sans lui. L'autre option est de ne garder en public que les articles CC BY. Cette décision appartient à l'utilisateur ; elle n'est pas prise ici. Cette note n'est pas un avis juridique.
