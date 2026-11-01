# Journal de la critique de fidélité PMC7075151

- Ma liste d'échantillons avant ouverture de l'extraction : CQDs/PC (4 h, protocole 2.2), série 2, 6, 8, 10 h à 453 K (Fig. 5b, c), phtalimide cristallin de référence (FTIR, XRD, XPS), CQDs dissous dans DMF (TEM), échantillon de stabilité à 393 et 423 K (Fig. 7b), LED blanche (2.3). Identique à `sample_inventory` : aucun échantillon manquant.
- Fig. 5c ouverte : étiquettes 17,0 / 20,3 / 16,9 / 15,2 / 2,3 % pour 2, 4, 6, 8, 10 h, conformes à l'extraction (lecture exacte, pas de lecture graphique approximative).
- Fig. 7b ouverte : à 10 h, 393 K vers 98 à 98,5 % et 423 K vers 87 % ; l'extraction (98 et 87 %) est dans la marge de 10 %. Le constat porte sur l'attribution à la voie 4 h (échantillon non identifié) et sur les points 1, 2, 4, 6 h non extraits.
- Fig. 6 ouverte : τ1 2,42 ns, τ2 6,79 ns, α1 75,85 %, α2 24,15 % ; seule α1 est dans le texte, τ1, τ2 et α2 sont absentes de l'extraction (constat mineur sûr).
- Fig. 4a ouverte : le tableau indique « At% » ; le texte dit seulement « element content » ; constat mineur sur l'unité.
- Fig. 8b ouverte : (0.3352, 0.3145), 5340 K, IRC 82 : conforme ; le CCT du résumé (5430 K) est une incohérence de l'article, déjà en doute, pas un constat.
- Pureté : la phrase générale « All chemicals were commercially available and used without further purification » couvre tous les réactifs d'après la règle 6 du RUNBOOK, mais elle ne donne aucun grade. Constat `non_cite_a_tort` en `probable` : l'orchestrateur doit trancher entre `purity` en texte et `not_stated`.
- Fournisseur du glycérol : la phrase « Glycerol OE-625 silicone LED encapsulation AB glue » désigne la colle ; je n'ai pas contesté `not_stated` pour le glycérol (lecture littérale de l'extracteur correcte).
- Héritage des branches 2, 6, 8, 10 h : seul 453 K est écrit dans la phrase de la série ; constat `deduit` en `probable`, car le doute et la limite de reproductibilité existent déjà.
- `method_sources` : refs.txt, aucun renvoi `[[B…]]` dans Méthodes ; ceux des Résultats ([[B31]]-[[B34]] et ceux de l'interprétation du PL) sont des attributions, donc liste vide correcte.
- Écarté : dissolution dans le DMF et solubilité dans l'eau (Fig. 3a), non extraites comme caractérisation ; pas de constat, simple observation qualitative.
- Écarté : propriétés de la voie `device` (`assemble` sans `not_stated`) : l'action n'est pas dans la grille minimale.
- Toutes les citations de l'extraction ont été testées comme sous-chaînes de `corpus/text/PMC7075151.txt` : aucune erreur.
