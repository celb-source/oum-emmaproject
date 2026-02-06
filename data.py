# data.py
# Base de données exhaustive "Mission Naturalisation 7 Jours"
# Mise à jour : Février 2026 (Gouvernement Lecornu)
# Profil : Oumaima AKKAD (Mode, Culture, Diplômée)

info_candidat = {
    "nom": "Oumaima AKKAD",
    "specialite": "Mode & Arts",
    "contexte": "Février 2026",
    "objectif": "Naturalisation par Décret"
}

# Programme intensif J-7 à J-1
programme_7_jours = {

    # --- JOUR 7 : IDENTITÉ, MOTIVATIONS & SYMBOLES (40 questions) ---
    "J-7": [
        # MOTIVATION & ANCRAGE
        {"q": "Pourquoi voulez-vous devenir Française ? (Question cruciale)", "r": "Je vis ici, mon travail et mes amis sont ici. Je partage les valeurs de la République et je veux pouvoir voter.", "type": "Orale", "cat": "Perso"},
        {"q": "Êtes-vous prête à renoncer à votre nationalité d'origine ?", "r": "Oui, si la loi l'exigeait, car je me sens Française.", "type": "Orale", "cat": "Perso"},
        {"q": "Depuis combien de temps vivez-vous en France ?", "r": "À adapter (ex: 5 ans, 10 ans...).", "type": "Orale", "cat": "Perso"},
        {"q": "Avez-vous de la famille proche à l'étranger ?", "r": "Non, mon centre de vie est ici (Attention : conjoints/enfants à l'étranger = refus).", "type": "Orale", "cat": "Perso"},
        {"q": "Envoyez-vous de l'argent à l'étranger ?", "r": "Non (ou sommes minimes pour aider, sans impacter mon budget en France).", "type": "Orale", "cat": "Perso"},
        {"q": "Quelle langue parlez-vous chez vous ?", "r": "Le français.", "type": "Orale", "cat": "Perso"},
        {"q": "Quelles sont vos passions ?", "r": "La mode, la culture, les arts...", "type": "Orale", "cat": "Perso"},
        {"q": "Faites-vous partie d'une association ?", "r": "Oui/Non (Si oui, citez-la, c'est un point positif).", "type": "Orale", "cat": "Perso"},
        {"q": "Avez-vous un casier judiciaire ?", "r": "Non.", "type": "Orale", "cat": "Perso"},
        {"q": "Payez-vous vos impôts ?", "r": "Oui, je suis à jour de mes obligations fiscales.", "type": "Orale", "cat": "Perso"},

        # SYMBOLES DE LA RÉPUBLIQUE
        {"q": "Quelle est la devise de la France ?", "r": "Liberté, Égalité, Fraternité.", "type": "Orale", "cat": "Symboles"},
        {"q": "D'où vient la devise ?", "r": "De la Révolution française.", "type": "Orale", "cat": "Symboles"},
        {"q": "Quelles sont les couleurs du drapeau ?", "r": "Bleu, Blanc, Rouge.", "type": "Orale", "cat": "Symboles"},
        {"q": "Que signifie le Bleu et le Rouge ?", "r": "Ce sont les couleurs de la ville de Paris.", "type": "Orale", "cat": "Symboles"},
        {"q": "Que signifie le Blanc ?", "r": "C'est la couleur de la Royauté (symbole de réconciliation).", "type": "Orale", "cat": "Symboles"},
        {"q": "Quel est l'hymne national ?", "r": "La Marseillaise.", "type": "Orale", "cat": "Symboles"},
        {"q": "Qui a écrit La Marseillaise ?", "options": ["Rouget de Lisle", "Victor Hugo", "Napoléon", "Mozart"], "correct": "Rouget de Lisle", "type": "QCM", "cat": "Symboles"},
        {"q": "En quelle année a été écrite La Marseillaise ?", "r": "1792 (À Strasbourg, chant de guerre pour l'armée du Rhin).", "type": "Orale", "cat": "Symboles"},
        {"q": "Qui est Marianne ?", "r": "L'allégorie (le symbole) de la République.", "type": "Orale", "cat": "Symboles"},
        {"q": "Que porte Marianne sur la tête ?", "r": "Un bonnet phrygien.", "type": "Orale", "cat": "Symboles"},
        {"q": "Que signifie le bonnet phrygien ?", "r": "C'est le symbole des esclaves affranchis (la liberté).", "type": "Orale", "cat": "Symboles"},
        {"q": "Où peut-on voir Marianne ?", "r": "Dans les mairies (buste) et sur les timbres.", "type": "Orale", "cat": "Symboles"},
        {"q": "Quel est l'animal symbole de la France ?", "options": ["Le Coq", "Le Lion", "L'Aigle", "Le Renard"], "correct": "Le Coq", "type": "QCM", "cat": "Symboles"},
        {"q": "Quelle est la fête nationale ?", "r": "Le 14 Juillet.", "type": "Orale", "cat": "Symboles"},
        {"q": "Où trouve-t-on la devise de la France ?", "r": "Sur les frontons des mairies, des écoles et sur les pièces de monnaie.", "type": "Orale", "cat": "Symboles"},

        # CULTURE GÉNÉRALE & MODE (Intro)
        {"q": "Quelle ville est la capitale de la mode ?", "r": "Paris.", "type": "Orale", "cat": "Mode"},
        {"q": "Citez un musée célèbre à Paris.", "r": "Le Louvre (ou Musée d'Orsay, Centre Pompidou).", "type": "Orale", "cat": "Culture"},
        {"q": "Qui a construit la Tour Eiffel ?", "r": "Gustave Eiffel (pour l'exposition universelle de 1889).", "type": "Orale", "cat": "Culture"},
        {"q": "Quelle est la plus belle avenue du monde ?", "r": "Les Champs-Élysées.", "type": "Orale", "cat": "Culture"},
        {"q": "Qui est Bernard Arnault ?", "r": "Le PDG de LVMH (Luxe).", "type": "Orale", "cat": "Mode/Éco"},
        {"q": "Citez une marque du groupe LVMH.", "r": "Louis Vuitton, Dior, Givenchy...", "type": "Orale", "cat": "Mode"},
        {"q": "Quel événement mode se tient deux fois par an à Paris ?", "r": "La Fashion Week.", "type": "Orale", "cat": "Mode"},
        {"q": "Qui est Coco Chanel ?", "r": "Une créatrice emblématique qui a libéré le corps de la femme.", "type": "Orale", "cat": "Mode"},
        {"q": "Citez un plat français connu.", "r": "Le Bœuf Bourguignon (ou Coq au Vin, Blanquette).", "type": "Orale", "cat": "Gastronomie"},
        {"q": "Quel est le vin pétillant français célèbre ?", "r": "Le Champagne.", "type": "Orale", "cat": "Gastronomie"},
        {"q": "Citez 3 fromages français.", "r": "Camembert, Roquefort, Brie.", "type": "Orale", "cat": "Gastronomie"},
        {"q": "Combien de sortes de fromages en France ?", "r": "Plus de 1000 (ou dire 'plus de 400').", "type": "Orale", "cat": "Gastronomie"},
        {"q": "Qu'est-ce que le Tour de France ?", "r": "Une grande course cycliste annuelle.", "type": "Orale", "cat": "Sport"},
        {"q": "Qui a gagné la Coupe du monde de foot 1998 et 2018 ?", "r": "L'équipe de France.", "type": "Orale", "cat": "Sport"},
        {"q": "Citez un monument hors de Paris.", "r": "Le Mont-Saint-Michel, le Château de Versailles.", "type": "Orale", "cat": "Culture"},
    ],

    # --- JOUR 6 : VALEURS, LAÏCITÉ & SOCIÉTÉ (35 questions) ---
    "J-6": [
        # LAÏCITÉ (Le plus important)
        {"q": "Qu'est-ce que la Laïcité ?", "r": "C'est la neutralité de l'État et la liberté de conscience. L'État ne reconnaît ni ne finance aucun culte.", "type": "Orale", "cat": "Laïcité"},
        {"q": "De quand date la loi de séparation des Églises et de l'État ?", "options": ["9 décembre 1905", "14 juillet 1789", "4 octobre 1958", "1945"], "correct": "9 décembre 1905", "type": "QCM", "cat": "Laïcité"},
        {"q": "La France est-elle un pays chrétien ?", "r": "Non, c'est une République laïque (mais avec des racines historiques chrétiennes).", "type": "Orale", "cat": "Laïcité"},
        {"q": "A-t-on le droit de croire en n'importe quel Dieu ?", "r": "Oui, ou de ne pas croire (Athéisme).", "type": "Orale", "cat": "Laïcité"},
        {"q": "Mise en situation : Avez-vous le droit de porter un signe religieux dans la rue ?", "r": "Oui, l'espace public est libre (sauf visage dissimulé).", "type": "Orale", "cat": "Laïcité"},
        {"q": "Mise en situation : Avez-vous le droit de porter un signe religieux si vous travaillez à la Mairie ?", "r": "Non, les agents du service public doivent être strictement neutres.", "type": "Orale", "cat": "Laïcité"},
        {"q": "Mise en situation : Les élèves peuvent-ils porter le voile au collège ?", "r": "Non, les signes ostentatoires sont interdits à l'école publique (Loi 2004).", "type": "Orale", "cat": "Laïcité"},
        {"q": "Mise en situation : Les mamans accompagnatrices en sortie scolaire peuvent-elles porter le voile ?", "r": "Oui (selon la jurisprudence actuelle du Conseil d'État).", "type": "Orale", "cat": "Laïcité"},
        {"q": "Mise en situation : Peut-on refuser un médecin homme à l'hôpital ?", "r": "Non, l'hôpital public est laïc et neutre. On ne choisit pas son praticien par religion.", "type": "Orale", "cat": "Laïcité"},
        {"q": "Mise en situation : Un patron privé peut-il interdire la prière au travail ?", "r": "Oui, pour des raisons de sécurité, d'hygiène ou d'organisation.", "type": "Orale", "cat": "Laïcité"},
        {"q": "Qu'est-ce que la loi de 2010 ?", "r": "Interdiction de dissimuler son visage dans l'espace public (Burqa/Niqab interdit pour sécurité).", "type": "Orale", "cat": "Laïcité"},

        # ÉGALITÉ & DROITS
        {"q": "Qu'est-ce que la Démocratie ?", "r": "Le gouvernement du peuple, par le peuple, pour le peuple.", "type": "Orale", "cat": "Valeurs"},
        {"q": "Les femmes ont-elles les mêmes droits que les hommes ?", "r": "Oui, c'est l'Égalité (travail, vote, salaire, autorité parentale).", "type": "Orale", "cat": "Valeurs"},
        {"q": "Le mari est-il le chef de famille ?", "r": "Non, l'autorité parentale est partagée.", "type": "Orale", "cat": "Société"},
        {"q": "Les discriminations sont-elles punies ?", "r": "Oui, le racisme et le sexisme sont des délits punis par la loi.", "type": "Orale", "cat": "Valeurs"},
        {"q": "Qu'est-ce que la Fraternité ?", "r": "La solidarité entre les citoyens (ex: Sécurité sociale, aides aux démunis).", "type": "Orale", "cat": "Valeurs"},
        {"q": "Citez des devoirs du citoyen.", "r": "Respecter la loi, payer ses impôts, défendre la patrie, être juré d'assises.", "type": "Orale", "cat": "Devoirs"},
        {"q": "Citez des droits du citoyen.", "r": "Droit de vote, d'éligibilité, de circulation, de grève.", "type": "Orale", "cat": "Droits"},
        {"q": "Le vote est-il obligatoire ?", "r": "Non.", "type": "Orale", "cat": "Droits"},
        {"q": "A-t-on le droit de faire grève ?", "r": "Oui (sauf militaires et policiers).", "type": "Orale", "cat": "Droits"},
        {"q": "En quelle année le mariage pour tous (homosexuel) a-t-il été voté ?", "options": ["2013", "2000", "1981", "2020"], "correct": "2013", "type": "QCM", "cat": "Société"},
        {"q": "Peut-on battre sa femme ou ses enfants en France ?", "r": "Non, les violences sont strictement interdites et punies.", "type": "Orale", "cat": "Société"},

        # SANTÉ & ÉDUCATION (QCM Civique)
        {"q": "L'école est obligatoire jusqu'à quel âge ?", "options": ["16 ans", "18 ans", "14 ans"], "correct": "16 ans", "type": "QCM", "cat": "Éducation"},
        {"q": "L'école publique est-elle payante ?", "r": "Non, elle est gratuite, laïque et obligatoire.", "type": "Orale", "cat": "Éducation"},
        {"q": "Qui a rendu l'école obligatoire ?", "r": "Jules Ferry (1881-1882).", "type": "Orale", "cat": "Histoire"},
        {"q": "Quel numéro appeler pour le SAMU ?", "options": ["15", "17", "18"], "correct": "15", "type": "QCM", "cat": "Santé"},
        {"q": "Quel numéro appeler pour les Pompiers ?", "options": ["18", "15", "17"], "correct": "18", "type": "QCM", "cat": "Sécurité"},
        {"q": "Quel numéro appeler pour la Police ?", "options": ["17", "15", "18"], "correct": "17", "type": "QCM", "cat": "Sécurité"},
        {"q": "Quel est le numéro d'urgence européen ?", "options": ["112", "911", "15"], "correct": "112", "type": "QCM", "cat": "Sécurité"},
        {"q": "Qui délivre la carte Vitale ?", "r": "L'Assurance Maladie (Sécurité Sociale).", "type": "Orale", "cat": "Santé"},
        {"q": "Avez-vous le droit de brûler des déchets dans votre jardin ?", "r": "Non, c'est interdit (écologie).", "type": "Orale", "cat": "Civisme"},
        {"q": "Peut-on conduire sans assurance ?", "r": "Non, c'est un délit.", "type": "Orale", "cat": "Civisme"},
        {"q": "Quelle est l'infraction la plus grave ?", "options": ["Le Crime", "Le Délit", "La Contravention"], "correct": "Le Crime", "type": "QCM", "cat": "Justice"},
        {"q": "Où sont jugés les crimes ?", "r": "À la Cour d'Assises (avec un jury populaire).", "type": "Orale", "cat": "Justice"},
        {"q": "Où sont jugés les délits ?", "r": "Au Tribunal Correctionnel.", "type": "Orale", "cat": "Justice"},
    ],

    # --- JOUR 5 : HISTOIRE - DES ORIGINES À 1900 (30 questions) ---
    "J-5": [
        # LES ORIGINES & ROIS
        {"q": "Qui sont les ancêtres des Français ?", "r": "Les Gaulois.", "type": "Orale", "cat": "Histoire"},
        {"q": "Qui a battu les Gaulois ?", "r": "Jules César (Les Romains) à Alésia en 52 av. J-C.", "type": "Orale", "cat": "Histoire"},
        {"q": "Qui est Vercingétorix ?", "r": "Le chef des Gaulois.", "type": "Orale", "cat": "Histoire"},
        {"q": "Qui est le premier Roi des Francs ?", "r": "Clovis.", "type": "Orale", "cat": "Histoire"},
        {"q": "Pourquoi Clovis est-il important ?", "r": "Il a unifié le pays et choisi Paris comme capitale.", "type": "Orale", "cat": "Histoire"},
        {"q": "Qui est Charlemagne ?", "r": "Empereur (sacré en l'an 800). On dit qu'il a 'inventé l'école'.", "type": "Orale", "cat": "Histoire"},
        {"q": "Quelle guerre a duré plus de 100 ans ?", "r": "La Guerre de Cent Ans (contre les Anglais).", "type": "Orale", "cat": "Histoire"},
        {"q": "Qui est Jeanne d'Arc ?", "r": "Une héroïne qui a libéré Orléans et fait sacrer le roi, brûlée vive à Rouen.", "type": "Orale", "cat": "Histoire"},
        {"q": "Qui est François 1er ?", "r": "Le Roi de la Renaissance. Il a imposé le français comme langue officielle (1539).", "type": "Orale", "cat": "Histoire"},
        {"q": "Quel château a construit François 1er ?", "r": "Chambord.", "type": "Orale", "cat": "Histoire"},
        {"q": "Qui est Henri IV ?", "r": "Le roi qui a signé l'Édit de Nantes (tolérance protestants/catholiques).", "type": "Orale", "cat": "Histoire"},
        {"q": "Qui est Louis XIV ?", "r": "Le Roi Soleil. Symbole de la monarchie absolue.", "type": "Orale", "cat": "Histoire"},
        {"q": "Quel château a construit Louis XIV ?", "r": "Le Château de Versailles.", "type": "Orale", "cat": "Histoire"},
        {"q": "Où vivait le Roi ?", "r": "À Versailles.", "type": "Orale", "cat": "Histoire"},

        # LA RÉVOLUTION FRANÇAISE (1789)
        {"q": "En quelle année a eu lieu la Révolution Française ?", "options": ["1789", "1799", "1804"], "correct": "1789", "type": "QCM", "cat": "Histoire"},
        {"q": "Quel événement fête-t-on le 14 juillet ?", "r": "La Prise de la Bastille (1789).", "type": "Orale", "cat": "Histoire"},
        {"q": "Qu'était la Bastille ?", "r": "Une prison royale.", "type": "Orale", "cat": "Histoire"},
        {"q": "Qu'est-ce qui a été aboli le 4 août 1789 ?", "r": "Les privilèges (fin de la noblesse).", "type": "Orale", "cat": "Histoire"},
        {"q": "Quel texte fondamental a été écrit en 1789 ?", "r": "La Déclaration des Droits de l'Homme et du Citoyen (DDHC).", "type": "Orale", "cat": "Histoire"},
        {"q": "Qui était le roi pendant la Révolution ?", "r": "Louis XVI.", "type": "Orale", "cat": "Histoire"},
        {"q": "Comment est mort Louis XVI ?", "r": "Guillotiné (ainsi que sa femme Marie-Antoinette).", "type": "Orale", "cat": "Histoire"},
        {"q": "Quand a été proclamée la 1ère République ?", "r": "En 1792.", "type": "Orale", "cat": "Histoire"},

        # XIXe SIÈCLE (NAPOLÉON & RÉPUBLIQUES)
        {"q": "Qui est Napoléon Bonaparte ?", "r": "Général puis Empereur des Français.", "type": "Orale", "cat": "Histoire"},
        {"q": "Citez 3 choses créées par Napoléon.", "r": "Le Code Civil, les Préfets, les Lycées, la Légion d'honneur.", "type": "Orale", "cat": "Histoire"},
        {"q": "Quand Napoléon est-il devenu Empereur ?", "r": "En 1804.", "type": "Orale", "cat": "Histoire"},
        {"q": "Qui a écrit 'Les Misérables' ?", "r": "Victor Hugo.", "type": "Orale", "cat": "Littérature"},
        {"q": "Qui est Victor Hugo ?", "r": "Écrivain et homme politique. Il est enterré au Panthéon.", "type": "Orale", "cat": "Littérature"},
        {"q": "Qu'est-ce qui a été aboli en 1848 ?", "r": "L'esclavage.", "type": "Orale", "cat": "Histoire"},
        {"q": "Qui a aboli l'esclavage ?", "r": "Victor Schœlcher.", "type": "Orale", "cat": "Histoire"},
        {"q": "Que s'est-il passé aussi en 1848 ?", "r": "Le suffrage universel masculin (droit de vote pour tous les hommes).", "type": "Orale", "cat": "Histoire"},
        {"q": "Qui est Jules Ferry ?", "r": "Il a rendu l'école gratuite, laïque et obligatoire (1881).", "type": "Orale", "cat": "Histoire"},
        {"q": "Qui a inventé le cinéma ?", "r": "Les Frères Lumière (en 1895).", "type": "Orale", "cat": "Culture"},
    ],

    # --- JOUR 4 : HISTOIRE CONTEMPORAINE (XXe SIÈCLE) (35 questions) ---
    "J-4": [
        # PREMIÈRE GUERRE MONDIALE (14-18)
        {"q": "Dates de la 1ère Guerre Mondiale ?", "options": ["1914-1918", "1939-1945", "1870-1871"], "correct": "1914-1918", "type": "QCM", "cat": "Histoire"},
        {"q": "Qui étaient les alliés de la France en 14-18 ?", "r": "L'Angleterre, la Russie, puis les États-Unis.", "type": "Orale", "cat": "Histoire"},
        {"q": "Qui était l'ennemi ?", "r": "L'Allemagne.", "type": "Orale", "cat": "Histoire"},
        {"q": "Comment appelait-on les soldats français ?", "r": "Les Poilus.", "type": "Orale", "cat": "Histoire"},
        {"q": "Citez une bataille célèbre de 14-18.", "r": "Verdun (1916).", "type": "Orale", "cat": "Histoire"},
        {"q": "Que s'est-il passé le 11 novembre 1918 ?", "r": "L'Armistice (la fin des combats).", "type": "Orale", "cat": "Histoire"},
        {"q": "Le 11 novembre est-il férié ?", "r": "Oui.", "type": "Orale", "cat": "Histoire"},

        # SECONDE GUERRE MONDIALE (39-45)
        {"q": "Dates de la 2nde Guerre Mondiale ?", "options": ["1939-1945", "1914-1918", "1954-1962"], "correct": "1939-1945", "type": "QCM", "cat": "Histoire"},
        {"q": "Qui a occupé la France ?", "r": "L'Allemagne nazie.", "type": "Orale", "cat": "Histoire"},
        {"q": "Qui dirigeait la France sous l'occupation (Vichy) ?", "r": "Le Maréchal Pétain (qui a collaboré).", "type": "Orale", "cat": "Histoire"},
        {"q": "Qui a refusé la défaite ?", "r": "Le Général de Gaulle.", "type": "Orale", "cat": "Histoire"},
        {"q": "Qu'est-ce que l'Appel du 18 juin 1940 ?", "r": "L'appel à la Résistance lancé par De Gaulle depuis Londres.", "type": "Orale", "cat": "Histoire"},
        {"q": "Qui est Jean Moulin ?", "r": "Le chef de la Résistance, mort torturé par la Gestapo.", "type": "Orale", "cat": "Histoire"},
        {"q": "Quand a eu lieu le débarquement des alliés ?", "r": "Le 6 juin 1944 (en Normandie).", "type": "Orale", "cat": "Histoire"},
        {"q": "Que fête-t-on le 8 mai ?", "r": "La victoire de 1945 (fin de la guerre en Europe).", "type": "Orale", "cat": "Histoire"},
        {"q": "Qu'est-ce que la Shoah ?", "r": "L'extermination des Juifs d'Europe par les nazis (Génocide).", "type": "Orale", "cat": "Histoire"},
        {"q": "Citez une femme célèbre de la Résistance.", "r": "Josephine Baker ou Lucie Aubrac.", "type": "Orale", "cat": "Histoire"},
        {"q": "Qui sont les Justes ?", "r": "Ceux qui ont caché et sauvé des Juifs pendant la guerre.", "type": "Orale", "cat": "Histoire"},

        # Vème RÉPUBLIQUE & SOCIÉTÉ MODERNE
        {"q": "En quelle année les femmes ont-elles eu le droit de vote ?", "options": ["1944", "1905", "1789"], "correct": "1944", "type": "QCM", "cat": "Histoire/Femmes"},
        {"q": "Qui a fondé la Ve République ?", "r": "Charles de Gaulle (en 1958).", "type": "Orale", "cat": "Histoire"},
        {"q": "Qui a donné l'indépendance à l'Algérie ?", "r": "De Gaulle (1962).", "type": "Orale", "cat": "Histoire"},
        {"q": "Qu'est-ce que Mai 68 ?", "r": "Un mouvement de révolte étudiant et ouvrier.", "type": "Orale", "cat": "Histoire"},
        {"q": "Qui a fait voter la loi sur l'IVG (Avortement) ?", "r": "Simone Veil (en 1975).", "type": "Orale", "cat": "Histoire/Femmes"},
        {"q": "Qui a aboli la peine de mort ?", "r": "Robert Badinter (Ministre de Mitterrand) en 1981.", "type": "Orale", "cat": "Histoire"},
        {"q": "Citez les présidents de la Ve République.", "r": "De Gaulle, Pompidou, Giscard d'Estaing, Mitterrand, Chirac, Sarkozy, Hollande, Macron.", "type": "Orale", "cat": "Politique"},
        {"q": "Qui était le premier président socialiste ?", "r": "François Mitterrand.", "type": "Orale", "cat": "Histoire"},

        # FIGURES CULTURELLES & MODE XXe
        {"q": "Qui est Joséphine Baker ?", "r": "Chanteuse, danseuse et résistante. Elle est au Panthéon.", "type": "Orale", "cat": "Culture/Femmes"},
        {"q": "Qui est Marie Curie ?", "r": "Physicienne, double prix Nobel (Radium).", "type": "Orale", "cat": "Science/Femmes"},
        {"q": "Qui est Christian Dior ?", "r": "Grand couturier (Le New Look 1947).", "type": "Orale", "cat": "Mode"},
        {"q": "Qui est Yves Saint Laurent ?", "r": "Couturier, il a créé le smoking pour femme.", "type": "Orale", "cat": "Mode"},
        {"q": "Qui est Édith Piaf ?", "r": "Chanteuse célèbre (La Môme).", "type": "Orale", "cat": "Culture"},
        {"q": "Qui est Coluche ?", "r": "Humoriste, fondateur des Restos du Cœur.", "type": "Orale", "cat": "Société"},
        {"q": "Qui est l'Abbé Pierre ?", "r": "Fondateur d'Emmaüs (aide aux sans-abris).", "type": "Orale", "cat": "Société"},
    ],

    # --- JOUR 3 : GÉOGRAPHIE & TERRITOIRES (35 questions) ---
    "J-3": [
        # GÉOGRAPHIE PHYSIQUE
        {"q": "Quelle est la superficie de la France ?", "r": "551 000 km² (Métropole).", "type": "Orale", "cat": "Géo"},
        {"q": "Quelle est la forme de la France ?", "r": "L'Hexagone.", "type": "Orale", "cat": "Géo"},
        {"q": "Citez les pays qui touchent la France.", "r": "Espagne, Italie, Suisse, Allemagne, Luxembourg, Belgique (et Brésil/Suriname en Guyane).", "type": "Orale", "cat": "Géo"},
        {"q": "Quelles mers bordent la France ?", "r": "La Mer Méditerranée, l'Océan Atlantique, la Manche, la Mer du Nord.", "type": "Orale", "cat": "Géo"},
        {"q": "Citez 3 fleuves français.", "r": "La Seine, La Loire, Le Rhône (aussi Garonne, Rhin).", "type": "Orale", "cat": "Géo"},
        {"q": "Quel est le plus long fleuve ?", "r": "La Loire.", "type": "Orale", "cat": "Géo"},
        {"q": "Quel fleuve traverse Paris ?", "r": "La Seine.", "type": "Orale", "cat": "Géo"},
        {"q": "Quel fleuve traverse Lyon ?", "r": "Le Rhône.", "type": "Orale", "cat": "Géo"},
        {"q": "Citez 3 chaînes de montagnes.", "r": "Les Alpes, les Pyrénées, le Massif Central (aussi Jura, Vosges).", "type": "Orale", "cat": "Géo"},
        {"q": "Quel est le point culminant de la France ?", "r": "Le Mont Blanc (4809 m), dans les Alpes.", "type": "Orale", "cat": "Géo"},

        # GÉOGRAPHIE ADMINISTRATIVE
        {"q": "Quelle est la capitale de la France ?", "r": "Paris.", "type": "Orale", "cat": "Géo"},
        {"q": "Citez 3 grandes villes françaises (hors Paris).", "r": "Marseille, Lyon, Toulouse (Nice, Bordeaux...).", "type": "Orale", "cat": "Géo"},
        {"q": "Combien y a-t-il de régions en métropole ?", "r": "13 régions.", "type": "Orale", "cat": "Géo"},
        {"q": "Dans quelle région habitez-vous ?", "r": "Réponse personnelle (ex: Île-de-France).", "type": "Orale", "cat": "Géo"},
        {"q": "Combien y a-t-il de départements au total ?", "r": "101 départements.", "type": "Orale", "cat": "Géo"},
        {"q": "Dans quel département habitez-vous ?", "r": "Réponse personnelle (ex: Paris 75).", "type": "Orale", "cat": "Géo"},
        {"q": "Qu'est-ce qu'un Préfet ?", "r": "Le représentant de l'État dans le département/région.", "type": "Orale", "cat": "Institutions"},
        {"q": "Où travaille le Préfet ?", "r": "À la Préfecture.", "type": "Orale", "cat": "Institutions"},

        # OUTRE-MER (Important)
        {"q": "Que signifie DROM ?", "r": "Département et Région d'Outre-Mer.", "type": "Orale", "cat": "Géo"},
        {"q": "Citez les 5 DROM.", "r": "Guadeloupe, Martinique, Guyane, La Réunion, Mayotte.", "type": "Orale", "cat": "Géo"},
        {"q": "Où se trouve la Guyane ?", "r": "En Amérique du Sud.", "type": "Orale", "cat": "Géo"},
        {"q": "Où se trouve la Réunion ?", "r": "Dans l'Océan Indien.", "type": "Orale", "cat": "Géo"},
        {"q": "Citez une Collectivité d'Outre-Mer (COM).", "r": "La Polynésie française, Saint-Martin...", "type": "Orale", "cat": "Géo"},

        # L'UNION EUROPÉENNE
        {"q": "Combien y a-t-il de pays dans l'UE ?", "options": ["27", "28", "15"], "correct": "27", "type": "QCM", "cat": "Europe"},
        {"q": "Quel pays a quitté l'UE récemment ?", "r": "Le Royaume-Uni (Brexit).", "type": "Orale", "cat": "Europe"},
        {"q": "Quelle est la devise de l'UE ?", "r": "Unie dans la diversité.", "type": "Orale", "cat": "Europe"},
        {"q": "Quel est l'hymne européen ?", "r": "L'Ode à la Joie (Beethoven).", "type": "Orale", "cat": "Europe"},
        {"q": "Quel est le drapeau européen ?", "r": "Bleu avec 12 étoiles dorées en cercle.", "type": "Orale", "cat": "Europe"},
        {"q": "Où siège le Parlement européen ?", "r": "À Strasbourg.", "type": "Orale", "cat": "Europe"},
        {"q": "Où siège la Commission européenne ?", "r": "À Bruxelles.", "type": "Orale", "cat": "Europe"},
        {"q": "Quelle est la monnaie de la France ?", "r": "L'Euro.", "type": "Orale", "cat": "Europe"},
        {"q": "Qu'est-ce que l'espace Schengen ?", "r": "La zone de libre circulation des personnes en Europe.", "type": "Orale", "cat": "Europe"},
        {"q": "Citez un père fondateur de l'Europe.", "r": "Robert Schuman ou Jean Monnet.", "type": "Orale", "cat": "Europe"},
    ],

    # --- JOUR 2 : INSTITUTIONS, POLITIQUE 2026 & JUSTICE (35 questions) ---
    "J-2": [
        # EXÉCUTIF (ACTUALITÉ FÉVRIER 2026)
        {"q": "Qui est le Chef de l'État ?", "r": "Le Président de la République (Emmanuel Macron).", "type": "Orale", "cat": "Politique"},
        {"q": "Où réside le Président ?", "r": "Au Palais de l'Élysée.", "type": "Orale", "cat": "Politique"},
        {"q": "Pour combien de temps est élu le Président ?", "r": "5 ans (le quinquennat).", "type": "Orale", "cat": "Politique"},
        {"q": "Qui est le Chef du Gouvernement ?", "r": "Le Premier ministre (Sébastien Lecornu).", "type": "Orale", "cat": "Politique"},
        {"q": "Où réside le Premier ministre ?", "r": "À l'Hôtel de Matignon.", "type": "Orale", "cat": "Politique"},
        {"q": "Qui nomme le Premier ministre ?", "r": "Le Président de la République.", "type": "Orale", "cat": "Politique"},
        {"q": "Qui nomme les ministres ?", "r": "Le Président, sur proposition du Premier ministre.", "type": "Orale", "cat": "Politique"},
        {"q": "Qui est le Ministre de l'Intérieur (Fév 2026) ?", "r": "Laurent Nuñez (Chef de la Police et des Préfets).", "type": "Orale", "cat": "Politique"},
        {"q": "Qui est le Ministre de la Justice (Garde des Sceaux) ?", "r": "Didier Migaud.", "type": "Orale", "cat": "Politique"},
        {"q": "Qui commande l'armée ?", "r": "Le Président de la République (Chef des Armées).", "type": "Orale", "cat": "Politique"},

        # LÉGISLATIF (LE PARLEMENT)
        {"q": "Qu'est-ce que le Parlement ?", "r": "C'est l'Assemblée nationale + le Sénat.", "type": "Orale", "cat": "Institutions"},
        {"q": "Quel est le rôle du Parlement ?", "r": "Voter les lois et contrôler le gouvernement.", "type": "Orale", "cat": "Institutions"},
        {"q": "Qui a le dernier mot pour voter une loi ?", "r": "L'Assemblée nationale.", "type": "Orale", "cat": "Institutions"},
        {"q": "Où siègent les députés ?", "r": "Au Palais Bourbon.", "type": "Orale", "cat": "Institutions"},
        {"q": "Combien y a-t-il de députés ?", "r": "577.", "type": "Orale", "cat": "Institutions"},
        {"q": "Comment sont élus les députés ?", "r": "Au suffrage universel direct (par les citoyens).", "type": "Orale", "cat": "Institutions"},
        {"q": "Qui porte l'écharpe tricolore ?", "r": "Les élus (Maires, Députés, Sénateurs).", "type": "Orale", "cat": "Institutions"},
        {"q": "Où siègent les sénateurs ?", "r": "Au Palais du Luxembourg.", "type": "Orale", "cat": "Institutions"},
        {"q": "Combien y a-t-il de sénateurs ?", "r": "348.", "type": "Orale", "cat": "Institutions"},
        {"q": "Comment sont élus les sénateurs ?", "r": "Au suffrage indirect (par les grands électeurs : maires, etc.).", "type": "Orale", "cat": "Institutions"},
        {"q": "Qui est le président du Sénat ?", "r": "Gérard Larcher (C'est le 2ème personnage de l'État).", "type": "Orale", "cat": "Institutions"},

        # JUSTICE & MAIRIE
        {"q": "Qu'est-ce que le Conseil Constitutionnel ?", "r": "Il vérifie que les lois respectent la Constitution.", "type": "Orale", "cat": "Institutions"},
        {"q": "Où sont enregistrés les mariages et naissances ?", "r": "À la Mairie (État Civil).", "type": "Orale", "cat": "Institutions"},
        {"q": "Comment élit-on le Maire ?", "r": "Par le Conseil municipal (élections municipales tous les 6 ans).", "type": "Orale", "cat": "Institutions"},
        {"q": "Qui est le Maire de votre ville ?", "r": "Réponse personnelle (ex: Anne Hidalgo à Paris).", "type": "Orale", "cat": "Perso"},

        # DROIT DU TRAVAIL & SOCIAUX
        {"q": "Qu'est-ce que le SMIC ?", "r": "Le Salaire Minimum Interprofessionnel de Croissance.", "type": "Orale", "cat": "Social"},
        {"q": "Qu'est-ce que la Sécurité Sociale ?", "r": "Le système qui protège les français (Maladie, Retraite, Famille, Chômage).", "type": "Orale", "cat": "Social"},
        {"q": "Qui a créé la Sécurité Sociale ?", "r": "En 1945, après la guerre.", "type": "Orale", "cat": "Histoire"},
        {"q": "Qu'est-ce que les impôts financent ?", "r": "Les services publics (Hôpitaux, Écoles, Routes, Police...).", "type": "Orale", "cat": "Social"},
        {"q": "Qu'est-ce qu'un CDD ?", "r": "Contrat à Durée Déterminée.", "type": "Orale", "cat": "Travail"},
        {"q": "Qu'est-ce qu'un CDI ?", "r": "Contrat à Durée Indéterminée.", "type": "Orale", "cat": "Travail"},
    ],

    # --- JOUR 1 : CULTURE, MODE & SPRINT FINAL (45 questions) ---
    "J-1": [
        # SPÉCIAL MODE & ARTS (PROFIL OUMAIMA)
        {"q": "Qui est Simon Porte Jacquemus ?", "r": "Un créateur de mode français contemporain très populaire.", "type": "Orale", "cat": "Mode"},
        {"q": "Qui est Jean-Paul Gaultier ?", "r": "Grand couturier français (La marinière).", "type": "Orale", "cat": "Mode"},
        {"q": "Qui est Hubert de Givenchy ?", "r": "Couturier français (élégance, Audrey Hepburn).", "type": "Orale", "cat": "Mode"},
        {"q": "Quelle femme a révolutionné la mode au 20e siècle ?", "r": "Coco Chanel (La petite robe noire).", "type": "Orale", "cat": "Mode"},
        {"q": "Qu'est-ce que la Haute Couture ?", "r": "Une appellation protégée française pour le luxe fait main.", "type": "Orale", "cat": "Mode"},
        {"q": "Qui est Karl Lagerfeld ?", "r": "Directeur artistique de Chanel (mort en 2019, icône).", "type": "Orale", "cat": "Mode"},
        {"q": "Qui est Hedi Slimane ?", "r": "Styliste influent (Dior Homme, Saint Laurent, Celine).", "type": "Orale", "cat": "Mode"},
        {"q": "Qui est Philippe Starck ?", "r": "Un designer industriel français célèbre.", "type": "Orale", "cat": "Arts"},
        {"q": "Qui est Claude Monet ?", "r": "Peintre impressionniste (Les Nymphéas).", "type": "Orale", "cat": "Arts"},
        {"q": "Qui est Auguste Rodin ?", "r": "Sculpteur (Le Penseur).", "type": "Orale", "cat": "Arts"},
        {"q": "Qui est Aya Nakamura ?", "r": "La chanteuse francophone la plus écoutée au monde.", "type": "Orale", "cat": "Musique"},
        {"q": "Qui est David Guetta ?", "r": "DJ français mondialement connu.", "type": "Orale", "cat": "Musique"},
        {"q": "Qui est Vanessa Paradis ?", "r": "Chanteuse et actrice (Egérie Chanel).", "type": "Orale", "cat": "Culture"},
        {"q": "Qui est Annie Ernaux ?", "r": "Écrivaine, Prix Nobel de Littérature 2022.", "type": "Orale", "cat": "Littérature"},
        {"q": "Qui est George Sand ?", "r": "Écrivaine du 19e siècle (Aurore Dupin).", "type": "Orale", "cat": "Littérature"},
        {"q": "Qui est Colette ?", "r": "Écrivaine française célèbre.", "type": "Orale", "cat": "Littérature"},
        {"q": "Qui est Sophie Marceau ?", "r": "Actrice française populaire.", "type": "Orale", "cat": "Cinéma"},
        {"q": "Qui est Omar Sy ?", "r": "Acteur français (Intouchables, Lupin).", "type": "Orale", "cat": "Cinéma"},
        {"q": "Qui est Marion Cotillard ?", "r": "Actrice oscarisée (La Môme).", "type": "Orale", "cat": "Cinéma"},
        {"q": "Qui est Zinédine Zidane ?", "r": "Footballeur légendaire (1998).", "type": "Orale", "cat": "Sport"},
        {"q": "Qui est Kylian Mbappé ?", "r": "Footballeur star.", "type": "Orale", "cat": "Sport"},
        {"q": "Qui est Teddy Riner ?", "r": "Judoka multiple champion olympique.", "type": "Orale", "cat": "Sport"},
        {"q": "Qui est Marie-José Pérec ?", "r": "Athlète triple championne olympique.", "type": "Orale", "cat": "Sport"},
        
        # SPRINT FINAL (MÉLANGE RAPIDE)
        {"q": "Nom du Premier ministre ?", "r": "Sébastien Lecornu.", "type": "Flash", "cat": "Politique"},
        {"q": "Ministre de l'Intérieur ?", "r": "Laurent Nuñez.", "type": "Flash", "cat": "Politique"},
        {"q": "Date Révolution ?", "r": "1789.", "type": "Flash", "cat": "Histoire"},
        {"q": "Couleurs Drapeau ?", "r": "Bleu Blanc Rouge.", "type": "Flash", "cat": "Symboles"},
        {"q": "Devise ?", "r": "Liberté Égalité Fraternité.", "type": "Flash", "cat": "Valeurs"},
        {"q": "Laïcité ?", "r": "Neutralité de l'État.", "type": "Flash", "cat": "Valeurs"},
        {"q": "Qui fait la loi ?", "r": "Le Parlement.", "type": "Flash", "cat": "Institutions"},
        {"q": "Capitale ?", "r": "Paris.", "type": "Flash", "cat": "Géo"},
        {"q": "Hymne ?", "r": "La Marseillaise.", "type": "Flash", "cat": "Symboles"},
        {"q": "Année droit de vote femmes ?", "r": "1944.", "type": "Flash", "cat": "Histoire"},
        {"q": "Année abolition peine de mort ?", "r": "1981.", "type": "Flash", "cat": "Histoire"},
        {"q": "Qui a aboli l'esclavage ?", "r": "Victor Schœlcher.", "type": "Flash", "cat": "Histoire"},
        {"q": "Qui a créé l'école laïque ?", "r": "Jules Ferry.", "type": "Flash", "cat": "Histoire"},
        {"q": "Créateur petite robe noire ?", "r": "Coco Chanel.", "type": "Flash", "cat": "Mode"},
        {"q": "PDG LVMH ?", "r": "Bernard Arnault.", "type": "Flash", "cat": "Éco"},
        {"q": "Qui est Jean Moulin ?", "r": "Résistant.", "type": "Flash", "cat": "Histoire"},
        {"q": "Qui est le Président ?", "r": "Emmanuel Macron.", "type": "Flash", "cat": "Politique"},
        {"q": "Numéro Urgence Médicale ?", "r": "15.", "type": "Flash", "cat": "Sécurité"},
        {"q": "Fleuve le plus long ?", "r": "La Loire.", "type": "Flash", "cat": "Géo"},
        {"q": "Montagne la plus haute ?", "r": "Mont Blanc.", "type": "Flash", "cat": "Géo"},
        {"q": "Nombre de régions ?", "r": "13.", "type": "Flash", "cat": "Géo"},
        {"q": "Année loi 1905 ?", "r": "Séparation Églises/État.", "type": "Flash", "cat": "Histoire"},
    ]
}

def get_categories():
    return ["Perso", "Symboles", "Mode", "Culture", "Histoire", "Géo", "Politique", "Laïcité", "Société"]
