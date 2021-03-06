
.. _l-feuille-de-route-2018-2A:

Feuille de route 2018 (2A)
==========================

.. contents::
    :local:
    :depth: 1

:ref:`Page principale du cours <l-td2a>`

Plan
++++

Les cours et séances se déroulent sur 8 séances de 3h
mardi matin. Le cours est divisé en deux pistes
*Stat* et *Eco* qui correspondent aux profils décrits
dans :ref:`l-td2a-notions`. Un compte **slack**
`python-ensae-2a.slack.com <https://python-ensae-2a.slack.com/>`_
a été créé pour faciliter les échanges, annonces et questions.
Une compétition sera ouverte le premier jour et
fermée à la dernière session où les résultas et les idées seront
discutées.

+---------------------------+---------------------------------------------------+-----------------------------------------------+
| Séance                    | Voie stat                                         | Voie éco                                      |
+===========================+===================================================+===============================================+
| 11/9 (1) *amphi*          | * Présentation du cours, évaluation                                                               |
|                           | * Rappels sur le langage :epkg:`Python`, les modules les plus utilisés                            |
| :ref:`l-route2018-stat1`  | * Classification binaire, régression logistique, régression linéaire                              |
|                           | * Apprentissage test, validation croisée                                                          |
|                           | * **A faire** : exécuter trois notebooks                                                          |
|                           |   :ref:`structuresdonneesconversionrst`, :ref:`histogrammerapiderst`, :ref:`mlfeaturesmodelrst`   |
+---------------------------+---------------------------------------------------+-----------------------------------------------+
| 18/9 (2) *TD/amphi*       | Rappels et exercices sur la manipulation des      | Rappels et exercices sur le langage           |
|                           | données avec :epkg:`pandas`, :epkg:`numpy`,       | :epkg:`Python`, manipulation des données avec |
| :ref:`l-route2018-stat2`, | :epkg:`matplotlib`, :epkg:`scikit-learn`,         | :epkg:`pandas`                                |
| :ref:`l-route2018-eco2`   | notion de prédicteur, transformeurs, pipelines,   |                                               |
|                           | stacking                                          |                                               |
+---------------------------+---------------------------------------------------+-----------------------------------------------+
| 25/9 (3) *TD/amphi*       | ACP, réduction de dimension                       | Suite et fin des exercices pandas et          |
|                           | variables catégorielles, textuelles,              | représentations graphiques variées, fin des   |
| :ref:`l-route2018-stat3`, | mention de :epkg:`catboost`                       | exercices sur :epkg:`pandas`, :epkg:`numpy`,  |
| :ref:`l-route2018-eco3`,  |                                                   | visualisation avec :epkg:`matplotlib`,        |
| **deux exposés**          |                                                   | cartographie                                  |
+---------------------------+---------------------------------------------------+-----------------------------------------------+
| 2/10 (4) *TD/amphi*       | Ranking, détection d'anomalies, clustering,       | Premiers pas avec :epkg:`scikit-learn`,       |
|                           | valeurs manquantes, imbalanced classification,    | ACP, Regréssion linéaire, Logit,              |
| :ref:`l-route2018-stat4`, | recommandation, test A/B                          | classification binaire, scraping avec un      |
| :ref:`l-route2018-eco4`   |                                                   | exemple sur la récupération d'image           |
| **deux exposés**          |                                                   | :ref:`2018-10-02_scraping_recuperer_images`   |
+---------------------------+---------------------------------------------------+-----------------------------------------------+
| 9/10 (5) *TD/amphi*       | Machine learning crypté, séries temporelles,      | Variables textuelles, clustering,             |
|                           | apprentissage par renforcement,                   | détection d'anomalies, graphes et             |
| :ref:`l-route2018-stat5`, | algorithme du bandit, auto-learning               | recommandations                               |
| :ref:`l-route2018-eco5`,  |                                                   |                                               |
| **deux exposés**          |                                                   |                                               |
+---------------------------+---------------------------------------------------+-----------------------------------------------+
| 16/10 (6) *TD/amphi*      | * Propriétés des modèles mathématiques, modèles linéaires, modèles ensemblistes, modèles          |
|                           |   dérivables, gradient, feature importance, parallélisme, boosting (*Xavier Dupré*)               |
| :ref:`l-route2018-stat6`, | * Interprétation des modèles de machine learning (*Gaël Varoquaux*), notes :                      |
| **deux exposés**          |   `Understanding and diagnosing your machine-learning models                                      |
|                           |   <http://gael-varoquaux.info/interpreting_ml_tuto/>`_                                            |
+---------------------------+---------------------------------------------------+-----------------------------------------------+
| 23/10 (7) *amphi*         | * notion de deep learning sans en faire, application au texte, et aux images,                     |
|                           |   transfer learning, exemples avec un moteur de recherche d'images (*Xavier Dupré*)               |
| :ref:`l-route2018-stat7`, | * *Ethique et algorithmes* avec (*Frédéric Bardolle*)                                             |
| **deux exposés**          |                                                                                                   |
+---------------------------+---------------------------------------------------+-----------------------------------------------+
| 6/11 (8) *TD*             | Notion d'algorithmes, écrire du code efficace en  | Travailler le texte, de la récupération à     |
|                           | :epkg:`Python`, avec :epkg:`pandas`,              | l'exploitation (2/2), Exercice de             |
| :ref:`l-route2018-stat8`, | :epkg:`numpy`, discussion sur les projets         | webscraping, API, NLP                         |
| :ref:`l-route2018-eco8`,  |                                                   |                                               |
| **deux exposés**          |                                                   |                                               |
+---------------------------+---------------------------------------------------+-----------------------------------------------+

Prérequis
+++++++++

* *Voix stat* : maîtrise du langage :epkg:`Python`, connaissance des modules :epkg:`pandas`,
  :epkg:`numpy`, voir
  `quelques rappels <http://www.xavierdupre.fr/app/papierstat/helpsphinx/rappel.html>`_
* *Voix éco* : maîtrise du langage :epkg:`Python`, :ref:`td2ecorappels1arst`

Intervenants
++++++++++++

`Xavier Dupré <mailto:xavier.dupre AT gmail.com>`_,
Anne Muller, Elodie Royant,
Antoine Ly, Eliot Barril,
Frédéric Bardolle,
`Gaël Varoquaux <http://gael-varoquaux.info/>`_.

Notes
+++++

Liens, notebooks prévus pour les séances pratiques.

.. contents::
    :local:

.. _l-route2018-stat1:

Séance 1
^^^^^^^^

* Précision sur le cours, évaluation, exposés, ressources, TD, amphi,
* notebook, :epkg:`python`, prérequis
* `Rappels de mathématiques <http://www.xavierdupre.fr/app/papierstat/helpsphinx/rappel.html>`_
* :ref:`td2ecorappels1arst`
* :ref:`mlcmachinelearningproblemsrst`
* Lectures `Lectures sur le machine learning <http://www.xavierdupre.fr/app/papierstat/helpsphinx/lectures/index.html>`_
* principe de la prédiction
* plus proches voisins
* base d'apprentissage et de tests, découpage stratifié
* hyperparamètres
* définition de la régression et de la classification
* score et ROC
* **A faire pour la prochaine fois** : exécuter trois notebooks,
  :ref:`structuresdonneesconversionrst`, :ref:`histogrammerapiderst`,
  :ref:`mlfeaturesmodelrst`

.. _l-route2018-stat2:

Séance 2 - stat
^^^^^^^^^^^^^^^

*8h30 - TD*

* Vérifier que les trois notebooks ont été exécutés,
  **A faire pour la prochaine fois** : exécuter trois notebooks,
  :ref:`structuresdonneesconversionrst`, :ref:`histogrammerapiderst`,
  :ref:`mlfeaturesmodelrst`
* Début du TD : :ref:`mlscikitlearnsimplerst` (:ref:`mlscikitlearnsimplecorrectionrst`)

*Lectures conseillées*

Les cours de Gaël Varoquaux :ref:`l-ml-skgael`,
les notebooks d'exercices associées à ces lectures.

*10h15 - modèle complexe avec scikit-learn*

* :ref:`2018-09-18sklearnapirst`
* Présentation de l'API de scikit-learn
* Notion de pipeline
* Implémentation d'un modèle avec l'API de *scikit-learn*
  `Contributing <http://scikit-learn.org/stable/developers/contributing.html#contributing-code>`_,
  `sklearn.base <http://scikit-learn.org/stable/modules/classes.html#module-sklearn.base>`_
* :epkg:`*py:pickle`
* `Stacking <http://www.xavierdupre.fr/app/papierstat/helpsphinx/notebooks/wines_multi_stacking.html>`_
* `Régression polynômiale et pileline <http://www.xavierdupre.fr/app/papierstat/helpsphinx/notebooks/wines_reg_poly.html>`_
* `Prédicteur pour chaque catégorie <http://www.xavierdupre.fr/app/papierstat/helpsphinx/notebooks/wines_color_linear.html>`_

.. _l-route2018-eco2:

Séance 2 - éco
^^^^^^^^^^^^^^

*8h30 - amphi*

* Rappels sur le langage :epkg:`python`,
  `Cheat sheet: Python <http://www.xavierdupre.fr/app/teachpyx/helpsphinx/c_resume/python_sheet.html>`_,
  variable, listes, dictionnaires, boucles, fonctions
* Introduction à :epkg:`pandas`, notion de table,
  lecture, écriture de fichiers texte, :epkg:`Excel`,
  ajout de colonne, opérations entre colonne, *apply*,
  opérations standard (sort, filter, group by, join),
* Introduction à :epkg:`numpy`, opérations standard,
  calcul matriciel, différences avec un dataframe
* :ref:`2018-09-18rappelspythonrst`
* :ref:`2018-09-18rappelspythonpandasmatplotlibrst`

*10h15 - TD*

Vérifier que les trois notebooks ont été exécutés,
exécuter trois notebooks,
:ref:`structuresdonneesconversionrst`, :ref:`histogrammerapiderst`,
:ref:`mlfeaturesmodelrst`

* :ref:`td2ecorappels1arst`
* :ref:`td2acenoncesession2arst`
* :ref:`td2acorrectionsession2arst`

.. _l-route2018-stat3:

Séance 3 - stat
^^^^^^^^^^^^^^^

*8h30 - TD*

* Début du TD : :ref:`mlscikitlearnsimplerst` (:ref:`mlscikitlearnsimplecorrectionrst`)

*10h30 - amphi*

* `Régression logistique et convexité <http://www.xavierdupre.fr/app/papierstat/helpsphinx/notebooks/logreg_kmeans.html>`_,
  `Régression logistique, diagramme de Voronoï, k-Means <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_ml/lr_voronoi.html>`_
  (maths)
* `Variables textuelles <http://www.xavierdupre.fr/app/papierstat/helpsphinx/lectures/preprocessing.html>`_
  (machine learning)
* Mesure du temps de calcul pour différentes tailles de jeu de données,
  étude pour une régression logistique
  :ref:`cffilinearregressionrst`
  (info)
* :ref:`td1acenoncesession12carterst`
* `tokenisation <http://www.xavierdupre.fr/app/papierstat/helpsphinx/notebooks/artificiel_tokenize.html>`_
* `de la tokenisation aux features <http://www.xavierdupre.fr/app/papierstat/helpsphinx/notebooks/artificiel_tokenize_features.html>`_
* `word2vec <http://www.xavierdupre.fr/app/papierstat/helpsphinx/notebooks/text_sentiment_wordvec.html>`_
* :ref:`l-ml2a-text-features`

.. _l-route2018-eco3:

Séance 3 - éco
^^^^^^^^^^^^^^

*8h30 - amphi*

* :ref:`td1acenoncesession12plotrst`, :ref:`td1acenoncesession12carterst`,
  :ref:`td1acenoncesession12jsrst`
* `Etude statistique <http://www.xavierdupre.fr/app/actuariat_python/helpsphinx/notebooks/enonce_2017.html#enonce2017rst>`_,
  `correction <http://www.xavierdupre.fr/app/actuariat_python/helpsphinx/notebooks/solution_2017.html>`_

*10h30 - TD*

* :ref:`td2acenoncesession1rst`
* `Tracer une carte en Python <http://www.xavierdupre.fr/app/papierstat/helpsphinx/notebooks/enedis_cartes.html>`_

.. _l-route2018-stat4:

Séance 4 - stat
^^^^^^^^^^^^^^^

*8h30 - cours*

* :ref:`l-mlbasic-anomaly`
* :ref:`l-ml2a-ranking`
* :ref:`l-imbalanced-classification`
* :ref:`l-td2a-missing-values`
* :ref:`td2aclusteringrst`, :ref:`td2aclusteringcorrectionrst`
* `Ranking et système de recommandations <http://www.xavierdupre.fr/app/papierstat/helpsphinx/lectures/otherml.html>`_
* :ref:`l-ml2a-testab` (ou `Test A/B sur wikipedia <https://en.wikipedia.org/wiki/A/B_testing>`_)
* `Liens entre factorisation de matrices, ACP, k-means <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_ml/missing_values_mf.html>`_
* :ref:`l-td2a-sys-recommandation`

*10h15 - TD*

* Traitement des variables catégorielles et textuelles.
* :ref:`td2asentimentanalysisrst`, :ref:`td2asentimentanalysiscorrectionrst`

Lectures pour ce TD :

* `tokenisation <http://www.xavierdupre.fr/app/papierstat/helpsphinx/notebooks/artificiel_tokenize.html>`_
* `de la tokenisation aux features <http://www.xavierdupre.fr/app/papierstat/helpsphinx/notebooks/artificiel_tokenize_features.html>`_
* `word2vec <http://www.xavierdupre.fr/app/papierstat/helpsphinx/notebooks/text_sentiment_wordvec.html>`_
* :ref:`l-ml2a-text-features`

.. _l-route2018-eco4:

Séance 4 - éco
^^^^^^^^^^^^^^

*8h30 - TD*

Notebooks pour s'exercer :

* Regardez différentes options disponibles pour faire les graphiques et
  passez un peu de temps sur l'exemple :ref:`td2avisualisationrst`
* :ref:`ACP <td2acenoncesession3arst>` (s'arrêter à l'exercice 1)
* :ref:`Régression linéaire <td2aecoregressionslineairesrst>`
* :ref:`Logit <td2aecocompetitionmodeleslogistiquesrst>`

*10h15 - cours*

Expression régulière et scrapping, :ref:`2018-10-02scrapingrecupererimagesrst`.

.. _l-route2018-stat5:

Séance 5 - stat
^^^^^^^^^^^^^^^

*8h30 - cours*

* :ref:`l-td2a-ml-crypted`
* :ref:`mltimeseriesbaserst`, :ref:`timeseriesssarst`
* :ref:`l-td2a-hyperparametre` et :ref:`l-ml2a-autolearning`
* `Counterfactual Reasoning and Learning Systems: The Example of Computational Advertising <http://jmlr.org/papers/v14/bottou13a.html>`_
* `Making Contextual Decisions with Low Technical Debt <https://arxiv.org/pdf/1606.03966.pdf>`_
* `Apprentissage par renforcement <https://fr.wikipedia.org/wiki/Apprentissage_par_renforcement>`_ :
  :math:`V(s) \leftarrow V(s) + \alpha \pa{r + \gamma V(s') - V(s)}`
* `SARSA <https://en.wikipedia.org/wiki/State%E2%80%93action%E2%80%93reward%E2%80%93state%E2%80%93action>`_ :
  :math:`Q(s_t, a_t) \leftarrow \alpha\pa{r_t + \gamma Q(s_{t+1}, a_{t+1} - Q(s_t, a_t)}`
* `Markov Decision Process <https://en.wikipedia.org/wiki/Markov_decision_process>`_
* deep reinforcement learning, `Alpha Go Zero <https://deepmind.com/blog/alphago-zero-learning-scratch/>`_

*10h15 - TD*

* :ref:`td2asentimentanalysisrst`, :ref:`td2asentimentanalysiscorrectionrst`
* :ref:`td2aenoncesession4Arst`, :ref:`correction <td2acorrectionsession4Arst>`

.. _l-route2018-eco5:

Séance 5 - éco
^^^^^^^^^^^^^^

*8h30 - TD*

* :ref:`TD2AEcoWebScrapingrst` (:ref:`correction <TD2AEcoWebScrapingcorrigerst>`)
* :ref:`td2aeco5dTravaillerdutextelesexpressionsregulieresrst`
  (:ref:`correction <td2aeco5dTravaillerdutextelesexpressionsregulierescorrectionrst>`)

*10h15 - cours*

* ACP
* Traitement des variables catégorielles
* Graphes et recommandations

.. _l-route2018-stat6:

Séance 6
^^^^^^^^

Propriétés des modèles mathématiques

* Thèmes : modèles linéaires, modèles ensemblistes, modèles dérivables,
  gradient, feature importance, parallélisme, boosting,
  binning, minibatch
* :ref:`mlatreeoverfittingrst`
* En cas de sparsité, idée de LightGBM (feature non conflictuelle),
  :ref:`correction <knnhighdimensioncorrectionrst>`,
  `Nearest Neighbours and Sparse Features <http://www.xavierdupre.fr/app/ensae_projects/helpsphinx/notebooks/nearest_neighbours_sparse_features.html>`_

*Autour du linéaire*

* `Régression linéaire par morceaux <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/notebooks/regression_lineaire.html>`_
* `Corrélations non linéaires <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/notebooks/correlation_non_lineaire.html>`_
* `Régression logistique, diagramme de Voronoï, k-Means <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_ml/lr_voronoi.html>`_

*Illustrations des propriétés mathématiques*

* `AdaBoost <https://fr.wikipedia.org/wiki/AdaBoost>`_,
  :ref:`2018-10-09ensemblegradientboostingrst`
* :ref:`mlcccmachinelearninginterpretabiliterst` (feature importance)

*Lectures annexes*

* :ref:`mlccmachinelearningproblems2rst`
* :ref:`l-ml2a-selvar`

*Librairies random forest*

* `XGBoost: A Scalable Tree Boosting System <https://arxiv.org/pdf/1603.02754.pdf>`_,
  sparsité et valeurs manquantes
* `LightGBM: A Highly Efficient Gradient Boosting Decision Tree <https://papers.nips.cc/paper/6907-lightgbm-a-highly-efficient-gradient-boosting-decision-tree.pdf>`_,
  sélection des splits, combinaison de features sparses
* `CatBoost: gradient boosting with categorical features support <http://learningsys.org/nips17/assets/papers/paper_11.pdf>`_,
  ajout de combinaisons de variables

*10h15 - Gaël Varoquaux*

Interprétation des modèles de machine learning

Notes : `Understanding and diagnosing your machine-learning models <http://gael-varoquaux.info/interpreting_ml_tuto/>`_.

.. _l-route2018-stat7:

Séance 7
^^^^^^^^

* `Réseaux de neurones <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_ml/rn/rn.html>`_
* :ref:`l-nolabel`
* `Galleries de problèmes résolus ou presque <http://www.xavierdupre.fr/app/ensae_teaching_dl/helpsphinx/chapters/dl_resolus.html>`_
* `Transfer Learning <http://www.xavierdupre.fr/app/ensae_teaching_dl/helpsphinx/chapters/deep_transfer_learning.html>`_
* `Search images with deep learning <http://www.xavierdupre.fr/app/mlinsights/helpsphinx/notebooks/search_images.html>`_
* `GAN <http://www.xavierdupre.fr/app/ensae_teaching_dl/helpsphinx/chapters/deep_generative_adversarial_network_gan.html>`_

*Ethique dans les données par Frédéric Bardolle*

* `Les fossoyeurs de l’innovation <https://salon.thefamily.co/les-fossoyeurs-de-l-innovation-6a754d1e8e35>`_ par Nicolas Colin
* `Tristan Harris : «Beaucoup de ficelles invisibles dans la tech nous agitent comme des marionnettes» <http://www.lefigaro.fr/secteur/high-tech/2018/05/31/32001-20180531ARTFIG00004-tristan-harris-beaucoup-de-ficelles-invisibles-dans-la-tech-nous-agitent-comme-des-marionnettes.php>`_
* Netflix 98% du contenu visionné est recommandé par un algorithme,
  fonction objectif pour Netflix : le temps passé sur le site,
  Netflix préfère une personne qui reste 10h plutôt que 10 personne qui reste 1h,
  polarisation des contenus
* `How AI Designers will Dictate Our Civic Future  <https://vimeo.com/238221677>`_
* `AlgoTranspency <https://algotransparency.org/>`_
* `L'efficacité d'un logiciel censé prédire la récidive à nouveau critiquée <https://www.lemonde.fr/pixels/article/2018/01/17/l-efficacite-d-un-logiciel-cense-predire-la-recidive-a-nouveau-critiquee_5243218_4408996.html>`_
* Google Translate biais sexiste : *A doctor, a nurse* traduit en *un docteur, une infirmière* et non *une docteure, un infirmier*
* `Serment d'Hippocrate pour Data Scientist <https://www.hippocrate.tech/>`_
* `Un monde d'automatisation ? <https://www.editions-eres.com/ouvrage/4222/un-monde-d-automatisation>`_,
  avec entre autres Alexeï Grinbaum
* `Ethique de la vertu <https://fr.wikipedia.org/wiki/%C3%89thique_de_la_vertu>`_ (`Aristote <https://fr.wikipedia.org/wiki/Aristote>`_,
  ne fais pas à autrui ce que tu ne voudrais pas qu'on te fasse),
  `éthique utilitariste <https://fr.wikipedia.org/wiki/Utilitarisme>`_
  (`Bentham <https://fr.wikipedia.org/wiki/Jeremy_Bentham>`_,
  maximiser le plaisir, diminuer les peines en apposant une échelle de valeur,
  l'action est jugée sur la conséquence),
  `éthique déontologique <https://fr.wikipedia.org/wiki/%C3%89thique_d%C3%A9ontologique>`_
  (`Kant <https://fr.wikipedia.org/wiki/Emmanuel_Kant>`_,
  `impératif catégorique <https://fr.wikipedia.org/wiki/Imp%C3%A9ratif_cat%C3%A9gorique>`_,
  je peux faire quelque chose si
  tout le monde peut le faire sans mettre le monde en danger, action en fonction de l'intention
  quelque soit le résultat),

*Dilemmes*

* `Dilemme du tramway <https://fr.wikipedia.org/wiki/Dilemme_du_tramway>`_
* `L'utilitarisme et les problèmes de tramways <https://minarchiste.wordpress.com/2013/12/06/lutilitarisme-et-les-problemes-de-tramways/>`_
* `Théorie du développement moral de Kohlberg <https://fr.wikipedia.org/wiki/Th%C3%A9orie_du_d%C3%A9veloppement_moral_de_Kohlberg>`_

.. _l-route2018-stat8:

Séance 8 - stat
^^^^^^^^^^^^^^^

* :ref:`knnhighdimensionrst`, :ref:`knnhighdimensioncorrectionrst`
* :ref:`BJKSTrst`
* :ref:`td2acenoncesession6Arst`, :ref:`td2acorrectionsession6Arst`
* :ref:`td2acenoncesession6Brst`, :ref:`td2acorrectionsession6Brst`

.. _l-route2018-eco8:

Séance 8 - éco
^^^^^^^^^^^^^^

*Notebook*

* :ref:`td2asentimentanalysisrst`
  (:ref:`correction <td2asentimentanalysiscorrectionrst>`),
  lien vers le jeu de données :
  `Project 1: Spooky Data Analysis <https://github.com/GU4243-ADS/spring2018-project1-ginnyqg/tree/master/data>`_
* :ref:`td2aeconlptfidfngramsldaword2vecsurdesextraitslitterairesrst`

*Lectures*

* :ref:`td2amltextfeaturesrst`
* :ref:`td2asomenlprst`
