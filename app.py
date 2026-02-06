import streamlit as st
import data

# Configuration de la page principale
st.set_page_config(
    page_title="Mission Naturalisation Oumaima 2026",
    page_icon="🇫🇷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS PERSONNALISÉ POUR UN LOOK MODERNE ---
st.markdown("""
<style>
    [data-testid="stSidebar"] {
        background-color: #f8f9fa;
    }
    .stButton button {
        width: 100%;
        border-radius: 10px;
        font-weight: bold;
    }
    .stProgress > div > div > div > div {
        background-color: #002654; /* Bleu France */
    }
    h1, h2, h3 {
        color: #002654;
    }
    .highlight-box {
        padding: 20px;
        border-radius: 15px;
        background-color: #ffffff;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border-left: 5px solid #ED2939; /* Rouge France */
    }
    .correct-answer {
        background-color: #d4edda;
        color: #155724;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #c3e6cb;
        margin-top: 10px;
    }
    .wrong-answer {
        background-color: #f8d7da;
        color: #721c24;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #f5c6cb;
        margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- GESTION DES ÉTATS (SESSION STATE) ---
# Initialisation des variables pour suivre la progression
if 'jour_selectionne' not in st.session_state:
    st.session_state.jour_selectionne = "J-7" # On commence au jour 7
if 'index_question_par_jour' not in st.session_state:
    st.session_state.index_question_par_jour = {jour: 0 for jour in data.programme_7_jours}
if 'reponse_affichee' not in st.session_state:
    st.session_state.reponse_affichee = False

# --- BARRE LATÉRALE (SIDEBAR) ---
with st.sidebar:
    # MISE À JOUR : Chargement de ton image logo.jpg
    try:
        st.image("logo.jpg", width=150)
    except:
        st.warning("Image 'logo.jpg' introuvable. Vérifiez qu'elle est dans le dossier.")
    
    st.caption("Objectif : Devenir Française !")

    st.title(f"👋 Bonjour {data.info_candidat['nom']}")
    st.info(f"🎯 Contexte : {data.info_candidat['contexte']}")
    st.success(f"✨ Spécialité incluse : {data.info_candidat['specialite']}")

    st.markdown("---")
    st.header("🗓️ Planning d'Entraînement")
    
    # Sélecteur de jour
    jours_dispo = list(data.programme_7_jours.keys())
    choix_jour = st.radio("Choisir votre mission du jour :", jours_dispo, index=jours_dispo.index(st.session_state.jour_selectionne))

    # Si on change de jour, on reset l'état d'affichage de la réponse
    if choix_jour != st.session_state.jour_selectionne:
        st.session_state.jour_selectionne = choix_jour
        st.session_state.reponse_affichee = False
        st.rerun()

    # Bouton Reset global
    if st.button("🔄 Recommencer la journée à zéro"):
        st.session_state.index_question_par_jour[st.session_state.jour_selectionne] = 0
        st.session_state.reponse_affichee = False
        st.rerun()

    st.markdown("---")
    # Aide-mémoire permanent dans la sidebar
    with st.expander("📌 Pense-bête 2026"):
        st.markdown("""
        * **PM :** Sébastien Lecornu
        * **Intérieur :** Laurent Nuñez
        * **14 Juillet :** Prise de la Bastille (1789)
        * **Devise :** Liberté, Égalité, Fraternité
        * **Laïcité :** Neutralité de l'État, liberté de croire ou non.
        * **LVMH :** Bernard Arnault
        """)

# --- LOGIQUE PRINCIPALE ---
# Récupération des données du jour choisi
questions_du_jour = data.programme_7_jours[st.session_state.jour_selectionne]
total_questions = len(questions_du_jour)
index_actuel = st.session_state.index_question_par_jour[st.session_state.jour_selectionne]
q_actuelle = questions_du_jour[index_actuel]

# --- AFFICHAGE DE LA PAGE PRINCIPALE ---
col1, col2 = st.columns([3, 1])
with col1:
    st.title(f"🚀 Mission {st.session_state.jour_selectionne}")
with col2:
    st.metric(label="Objectif Jour", value=f"{total_questions} Questions")

# Barre de progression
progression = (index_actuel + 1) / total_questions
st.progress(progression, text=f"Progression : Question {index_actuel + 1} sur {total_questions}")

# --- BOÎTE DE QUESTION ---
st.markdown(f"""
<div class="highlight-box">
    <p style="color: grey; margin-bottom: 5px;">🏷️ Thème : {q_actuelle['cat']}</p>
    <h2>❓ {q_actuelle['q']}</h2>
</div>
""", unsafe_allow_html=True)

# --- ZONE DE RÉPONSE ---
# Cas 1 : C'est un QCM
if q_actuelle['type'] == "QCM":
    st.subheader("👉 Sélectionnez la bonne réponse :")
    
    # Création d'une clé unique pour le widget radio pour éviter les conflits
    widget_key = f"radio_{st.session_state.jour_selectionne}_{index_actuel}"
    
    # Affichage des options
    choix_utilisateur = st.radio("Options :", q_actuelle['options'], key=widget_key, label_visibility="collapsed")
    
    # Bouton de validation
    if st.button("Valider ma réponse 🎯", type="primary", disabled=st.session_state.reponse_affichee):
        st.session_state.reponse_affichee = True
        st.rerun()

    # Affichage du résultat après validation
    if st.session_state.reponse_affichee:
        if choix_utilisateur == q_actuelle['correct']:
            st.markdown(f"""<div class="correct-answer">✅ <b>BRAVO !</b> C'est une excellente réponse : {q_actuelle['correct']}</div>""", unsafe_allow_html=True)
            st.balloons()
        else:
            st.markdown(f"""<div class="wrong-answer">❌ <b>Aïe, erreur.</b><br>La bonne réponse était : <b>{q_actuelle['correct']}</b></div>""", unsafe_allow_html=True)

# Cas 2 : C'est une question Orale ou Flash
else:
    st.subheader("🗣️ Entraînement Oral")
    st.info("Répondez à voix haute, de manière claire et convaincante, comme devant l'agent.")
    
    # Bouton pour révéler la réponse
    if st.button("👀 Voir la réponse attendue", disabled=st.session_state.reponse_affichee):
        st.session_state.reponse_affichee = True
        st.rerun()

    # Affichage de la réponse
    if st.session_state.reponse_affichee:
         st.markdown(f"""<div class="correct-answer">✅ <b>Réponse type :</b><br>{q_actuelle['r']}</div>""", unsafe_allow_html=True)

# --- BOUTON QUESTION SUIVANTE ---
st.markdown("---")
col_next_1, col_next_2 = st.columns([4, 1])

with col_next_2:
    # Le bouton n'apparaît que si la réponse est affichée
    if st.session_state.reponse_affichee:
        # Si ce n'est pas la dernière question
        if index_actuel < total_questions - 1:
            if st.button("Question Suivante ➡️", type="primary"):
                # On incrémente l'index pour ce jour
                st.session_state.index_question_par_jour[st.session_state.jour_selectionne] += 1
                # On cache la réponse pour la prochaine question
                st.session_state.reponse_affichee = False
                st.rerun()
        # Si c'est la dernière question
        else:
            st.success("🎉 FÉLICITATIONS ! Vous avez terminé la session d'aujourd'hui.")
            st.write("Passez au jour suivant via le menu latéral.")

# --- FOOTER (PIED DE PAGE) ---
st.markdown("<br><br><br>", unsafe_allow_html=True) # Espace
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #555555; font-family: sans-serif;'>
        <p>🇫🇷 Prép'Naturalisation 2026 - Objectif Décret pour Oumaima AKKAD</p>
        <p style='font-size: 0.9em; margin-top: 15px;'>
            <b>© Tous droits réservés à Cherif le bg</b> 😎
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
