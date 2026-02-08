import streamlit as st
import data
import random
import time

# --- 1. CONFIGURATION DE LA PAGE (L'AMBIANCE) ---
st.set_page_config(
    page_title="Mission Naturalisation : Édition Oumaima",
    page_icon="🐓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. CSS "FRENCH TOUCH" (LE STYLE) ---
st.markdown("""
<style>
    /* FOND GÉNÉRAL */
    .stApp {
        background: linear-gradient(to right, #f0f8ff, #ffffff);
    }
    
    /* SIDEBAR (BLEU FRANCE) */
    [data-testid="stSidebar"] {
        background-color: #f0f4f8;
        border-right: 5px solid #002654;
    }
    
    /* TITRES & TEXTES */
    h1 { 
        color: #002654; 
        font-family: 'Garamond', serif; 
        text-align: center;
        text-shadow: 2px 2px 0px #eee;
    }
    h2, h3 { color: #ED2939; font-family: 'Arial', sans-serif; }
    
    /* BOITE QUESTION (CARTE TRICOLORE) */
    .question-card {
        background-color: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.15);
        border-top: 10px solid #002654;   /* Bleu */
        border-bottom: 10px solid #ED2939; /* Rouge */
        text-align: center;
        margin-bottom: 20px;
        transition: transform 0.3s;
    }
    .question-card:hover {
        transform: scale(1.02);
    }

    /* BOUTONS STYLISÉS */
    .stButton button {
        background: linear-gradient(45deg, #002654, #0055A4);
        color: white;
        border-radius: 50px;
        height: 55px;
        font-size: 18px;
        font-weight: bold;
        border: none;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
    }
    .stButton button:hover {
        background: linear-gradient(45deg, #ED2939, #ff5e6c);
        color: white;
    }

    /* MESSAGES DE RÉPONSE */
    .reponse-box {
        padding: 20px;
        border-radius: 15px;
        margin-top: 20px;
        font-size: 1.2em;
        animation: fadeIn 0.5s;
    }
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    
    /* FOOTER */
    .footer-bg {
        text-align: center;
        padding: 20px;
        color: grey;
        font-family: 'Courier New', monospace;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. FONCTIONS UTILITAIRES (LA LOGIQUE DRÔLE) ---

def get_french_reaction(is_correct):
    """Renvoie une réaction typiquement française aléatoire"""
    if is_correct:
        return random.choice([
            "🇫🇷 Cocorico ! C'est gagné !",
            "🥐 Magnifique ! Aussi bon qu'un croissant chaud.",
            "🍷 Excellent ! On ouvre le Champagne ?",
            "🥖 C'est un sans-faute, chef !",
            "✨ Oumaima, tu es plus française que Louis XIV !"
        ])
    else:
        return random.choice([
            "🧀 Sacré bleu ! C'est raté...",
            "🐓 Aïe aïe aïe... Napoléon se retourne dans sa tombe.",
            "🍷 C'est pas grave, reprends un peu de fromage.",
            "🤔 Bof bof... L'agent de la préfecture ne va pas aimer.",
            "🥖 Encore un effort pour la République !"
        ])

def get_icon_for_category(cat):
    """Associe une icône cliché à la catégorie"""
    if "Histoire" in cat: return "🏰"
    if "Géo" in cat: return "🗺️"
    if "Mode" in cat: return "👠"
    if "Gastronomie" in cat: return "🧀"
    if "Politique" in cat: return "⚖️"
    if "Symbole" in cat: return "🐓"
    if "Laïcité" in cat: return "🤝"
    return "🇫🇷"

# --- 4. GESTION DE L'ÉTAT (MÉMOIRE) ---
if 'mode_selectionne' not in st.session_state:
    st.session_state.mode_selectionne = "J-7"
if 'index_q' not in st.session_state:
    st.session_state.index_q = 0
if 'reponse_visible' not in st.session_state:
    st.session_state.reponse_visible = False

# --- 5. SIDEBAR (LE MENU) ---
with st.sidebar:
    # Logo
    try:
        st.image("logo.jpg", width=200)
    except:
        st.header("📸 [Logo Oumaima]")
    
    st.markdown("<h2 style='text-align: center; color:#002654;'>Objectif Décret</h2>", unsafe_allow_html=True)
    
    # Badge Profil
    st.info(f"👤 **Candidat :** {data.info_candidat['nom']}")
    st.warning(f"🧵 **Atout Majeur :** {data.info_candidat['specialite']}")
    
    st.markdown("---")
    
    # Sélecteur de mode
    st.markdown("### 📅 Planning de Révision")
    
    options = list(data.programme_7_jours.keys()) + ["🏆 CHALLENGE EXPERT"]
    
    # Gestion de l'index pour éviter les bugs
    try:
        idx = options.index(st.session_state.mode_selectionne)
    except:
        idx = 0
        
    choix = st.radio("Mission du jour :", options, index=idx)
    
    if choix != st.session_state.mode_selectionne:
        st.session_state.mode_selectionne = choix
        st.session_state.index_q = 0
        st.session_state.reponse_visible = False
        st.rerun()

    st.markdown("---")
    st.markdown("### 🥖 Pense-Bête Express")
    st.markdown("""
    - **PM :** Sébastien Lecornu
    - **14 Juillet :** Bastille 🏰
    - **Devise :** L.E.F.
    """)

# --- 6. PAGE PRINCIPALE ---

# Chargement des questions
est_expert = (st.session_state.mode_selectionne == "🏆 CHALLENGE EXPERT")
if est_expert:
    questions = data.questions_experts
    titre = "🤯 MODE EXPERT : L'ÉLITE DE LA NATION"
    sous_titre = "Attention, questions pièges niveau Bac+5 !"
else:
    questions = data.programme_7_jours[st.session_state.mode_selectionne]
    titre = f"🚀 MISSION {st.session_state.mode_selectionne}"
    sous_titre = "En route vers la naturalisation..."

# Sécurité index
if st.session_state.index_q >= len(questions):
    st.session_state.index_q = 0

q_data = questions[st.session_state.index_q]
cat_icon = get_icon_for_category(q_data['cat'])

# Affichage Titre
col_logo_1, col_logo_2, col_logo_3 = st.columns([1, 4, 1])
with col_logo_1:
    st.markdown("# 🇫🇷")
with col_logo_2:
    st.markdown(f"<h1>{titre}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center; color:gray;'>{sous_titre}</p>", unsafe_allow_html=True)
with col_logo_3:
    st.markdown("# 🐓")

# Barre de progression
progression = (st.session_state.index_q + 1) / len(questions)
st.progress(progression)

# --- CARTE DE LA QUESTION ---
st.markdown(f"""
<div class="question-card">
    <p style="color:#888; text-transform:uppercase; letter-spacing:2px; font-size:0.8em;">
        {cat_icon} Thème : {q_data['cat']} {cat_icon}
    </p>
    <h2 style="color:#002654; font-size:1.8em; margin-top:10px;">{q_data['q']}</h2>
</div>
""", unsafe_allow_html=True)

# --- ZONE D'INTERACTION ---
col_main_1, col_main_2, col_main_3 = st.columns([1, 2, 1])

with col_main_2:
    # ---------------- CAS QCM ----------------
    if q_data['type'] == "QCM":
        st.write("👉 **Votre réponse finale ?**")
        
        # Widget Radio avec clé unique
        key_radio = f"qcm_{st.session_state.mode_selectionne}_{st.session_state.index_q}"
        user_response = st.radio("Options", q_data['options'], key=key_radio, label_visibility="collapsed")
        
        if st.button("Valider ma réponse 🥖", disabled=st.session_state.reponse_visible):
            st.session_state.reponse_visible = True
            st.rerun()
            
        # Résultat QCM
        if st.session_state.reponse_visible:
            if user_response == q_data['correct']:
                st.markdown(f"""
                <div class="reponse-box" style="background-color:#d4edda; border:2px solid #28a745; color:#155724;">
                    <h3>✅ {get_french_reaction(True)}</h3>
                    <p>Bonne réponse : <b>{q_data['correct']}</b></p>
                </div>
                """, unsafe_allow_html=True)
                st.balloons()
            else:
                st.markdown(f"""
                <div class="reponse-box" style="background-color:#f8d7da; border:2px solid #dc3545; color:#721c24;">
                    <h3>❌ {get_french_reaction(False)}</h3>
                    <p>La bonne réponse était : <b>{q_data['correct']}</b></p>
                </div>
                """, unsafe_allow_html=True)

    # ---------------- CAS ORAL / FLASH ----------------
    else:
        st.info("🗣️ Entraînement Oral : Répondez à voix haute !")
        
        if st.button("👀 Voir la réponse", disabled=st.session_state.reponse_visible):
            st.session_state.reponse_visible = True
            st.rerun()
            
        if st.session_state.reponse_visible:
            st.markdown(f"""
            <div class="reponse-box" style="background-color:#fff3cd; border:2px solid #ffc107; color:#856404;">
                <h3>💡 La Réponse de l'Expert :</h3>
                <p style="font-size:1.1em;">{q_data['r']}</p>
            </div>
            """, unsafe_allow_html=True)

# --- NAVIGATION ---
st.markdown("<br>", unsafe_allow_html=True)

if st.session_state.reponse_visible:
    col_nav_1, col_nav_2, col_nav_3 = st.columns([1, 2, 1])
    with col_nav_2:
        if st.session_state.index_q < len(questions) - 1:
            if st.button("Question Suivante ➡️"):
                st.session_state.index_q += 1
                st.session_state.reponse_visible = False
                st.rerun()
        else:
            st.success("🎉 BRAVO CITOYENNE ! SESSION TERMINÉE !")
            st.snow()

# --- FOOTER ---
st.markdown("---")
st.markdown("""
<div class="footer-bg">
    <p>🇫🇷 République Française - Ministère de l'Entraînement Intensif 🇫🇷</p>
    <p style="font-size: 0.8em;">© Tous droits réservés à <b>Cherif le bg</b> 😎 | Fait avec amour et du bon vin</p>
</div>
""", unsafe_allow_html=True)
