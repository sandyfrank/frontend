import streamlit as st
import numpy as np
import requests

# ---------------------------
# Streamlit HTML customization
st.markdown("""
    <style>
        body {
            background-color: #f5f5f5;
            font-family: 'Arial', sans-serif;
        }
        .main-title {
            text-align: center;
            font-size: 3em;
            color: #4CAF50;
            font-weight: bold;
            margin-top: 20px;
        }
        .sub-title {
            text-align: center;
            font-size: 1.5em;
            color: #666;
            margin-bottom: 30px;
        }
        .form-container {
            background: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            margin-top: 20px;
        }
        .button-style {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .button-style:hover {
            background-color: #45a049;
        }
        .result {
            font-size: 1.2em;
            color: #333;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Language selection
language = st.sidebar.selectbox("Select Language / Sélectionnez la langue", ["English", "Français"])

# ---------------------------
# Pages
def home_page(language):
    if language == "English":
        st.markdown("<div class='main-title'>Welcome to KFS AI4Health Diabetes Prediction App</div>", unsafe_allow_html=True)
        st.markdown("<div class='sub-title'>This app predicts the likelihood of diabetes based on risk factors using AI.</div>", unsafe_allow_html=True)
        st.markdown("<div class='sub-title'>Use the sidebar to navigate between the pages.</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='main-title'>Bienvenue sur l'application KFS AI4Health pour la prédiction du diabète</div>", unsafe_allow_html=True)
        st.markdown("<div class='sub-title'>Cette application prédit la probabilité d'un diabète en fonction des facteurs de risque grâce à l'IA.</div>", unsafe_allow_html=True)
        st.markdown("<div class='sub-title'>Utilisez la barre latérale pour naviguer entre les pages.</div>", unsafe_allow_html=True)

def education_page():
    st.title("Education sur le Diabète") 
    # Section 1: General Information
    st.header("1. Généralités")
    st.write("""
    Le diabète se caractérise par une hyperglycémie chronique due à un défaut de sécrétion ou d’assimilation de l’insuline. L’insuline, seule hormone hypoglycémiante, est produite par les cellules béta du pancréas.

    La norme de la glycémie est comprise entre 0,8 et 1,10 g/L. On parle de diabète lorsque la glycémie à jeun est supérieure à 1,26 g/L à 2 reprises, ou par une glycémie supérieure à 2g/L à n’importe quel moment de la journée.

    Il existe trois types de diabète :
    - Le diabète de type 1
    - Le diabète de type 2
    - Le diabète gestationnel
    """)

    # Section 2: Type 1 Diabetes
    st.header("2. Le diabète de type 1")
    st.write("""
    Maladie auto-immune caractérisée par une hyperglycémie chronique due à une destruction progressive des cellules béta du pancréas. Il concerne environ 10 % des patients (environ 150 000 personnes), plutôt les enfants et adolescents ou les adultes de moins de 40 ans.
    
    ### 2.1- Signes cliniques
    Signes d’apparition brutale, qui débutent lorsque que 80% des cellules sont détruites:
    - Polyurie
    - Polydipsie
    - Perte de poids
    - Sensation de faim fréquente = polyphagie
    - Asthénie
    - Troubles visuels
    - Haleine cétonique
    - Acidose retrouvée dans les gaz du sang (pH < 7.3 en artériel, < 7,25 en veineux et bicarbonates < 22 mmol/L)
    - Glycosurie si la glycémie > 1,8 g/L

    ### 2.2- Traitement
    - Insulinothérapie à vie
    - Surveillance glycémique plusieurs fois par jour
    - Surveillance de l’HbA1c (hémoglobine glyquée : norme = < 7%)
    - Régime alimentaire adapté
    - Activité sportive
    """)

    # Section 3: Type 2 Diabetes
    st.header("3. Le diabète de type 2")
    st.write("""
    Maladie d’évolution lente, caractérisée par une insulinorésistance des cellules entraînant une hyperglycémie chronique. Les facteurs favorisants sont : une prédisposition génétique, une mauvaise alimentation, un surpoids, un manque d’activité physique, une mauvaise hygiène de vie, antécédents de diabète gestationnel. Il concerne 90% des patients (environ 3 millions de personnes), d’âge plutôt avancé (entre 40 et 50 ans).
    
    ### 3.1- Signes Cliniques
    Découverte le plus souvent fortuite, ou à l’occasion d’une complication (IDM, AVC…)
    - Hyperglycémie
    - Apparition de complications diverses

    ### 3.2- Traitement
    - Régime alimentaire adapté
    - Activité sportive si possible
    - Antidiabétiques oraux
    - Insulinothérapie
    - Surveillance glycémique plusieurs fois par jour
    - Surveillance de l’HbA1c (hémoglobine glyquée)
    """)

    # Section 4: Diabetes Complications
    st.header("4. Les complications du diabète")
    st.write("""
    - Hypoglycémie (signes : sueurs, pâleur, fringale, tremblements, sensation de malaise, troubles de la vision et de la concentration, somnolence, coma)
    - Hyperglycémie (signes : asthénie, bouche sèche, polyurie, soif intense)
    - La rétinopathie diabétique (cause de cécité)
    - La néphropathie diabétique (entraînant une insuffisance rénale terminale)
    - Infections urinaires plus fréquentes
    - Neuropathies périphérique et végétative diabétique (atteinte des nerfs)
    - Macro angiopathies (coronaropathie, atteinte carotidienne, artériopathie des membres inférieurs,…)
    - Pied diabétique (mal perforant plantaire)
    - Coma diabétique
    """)

    # Section 5: Hygienic-Dietetic Rules
    st.header("5. Règles hygiéno-diététiques")
    st.write("""
    - Alimentation équilibrée où chaque groupe d’aliments doit être représenté
    - Pratique sportive régulière
    - Arrêt du tabac 
    - Eviter la prise de poids
    - Surveillance de toute plaie, même minime
    """)

    # Section 6: Role of Nurses (IDE)
    st.header("6. Rôle IDE")
    st.write("""
    - Réalisation des glycémies capillaires
    - Préparation et injection d’insulines
    - Adaptation des doses d’insulines
    - Education des patients : réalisation des glycémies capillaires, injections d’insuline, adaptation des doses, signes d’hypo et d’hyperglycémie, régime alimentaire, expliquer l’importance de noter les glycémies et doses d’insuline réalisées dans un carnet d’autosurveillance.
    - Réalisation de bandelettes urinaires pour contrôle de la cétonurie
    - Surveillance de l’apparition des complications
    """)

    # Section 7: Gestational Diabetes
    st.header("7. Diabète gestationnel")
    st.write("""
    Selon la définition de l’OMS, le diabète gestationnel est un trouble de la tolérance glucidique conduisant à une hyperglycémie de sévérité variable, débutant ou diagnostiqué pour la première fois pendant la grossesse. Les signes cliniques sont les mêmes que les autres types de diabète. Dans 90% des cas le diabète gestationnel disparaît quelques semaines après l’accouchement.

    ### 7.1- Facteurs de risque
    - Grossesse tardive
    - Obésité ou surpoids de la mère
    - Antécédents de diabète gestationnel
    - Antécédents familiaux de diabète de type 2
    - Antécédents de macrosomie fœtale

    ### 7.2- Complications pour l’enfant
    - Macrosomie (poids de naissance > à 4kg)
    - Accouchement difficile
    - Détresse respiratoire
    - Hypoglycémie néonatale
    - Risque accrue de diabète de type 2 à l’âge adulte 

    ### 7.3- Complications pour la mère
    - Fausses couches
    - Accouchement par césarienne
    - Risque accrue de prééclampsie (prise de poids, œdème, HTA)
    - Risque de développer un diabète de type 2 après la grossesse
    - Risque d’accouchement prématuré

    ### 7.4- Dépistage
    Consiste en la réalisation du test HGPO (Hyperglycémie Provoquée par voie Orale) à 75 g de glucose.

    ### 7.5- Prévention
    - Alimentation équilibrée dès le début de la grossesse
    - Activité physique régulière en l’absence de contre indication
    - Limiter les apports glycémiques trop importants

    ### 7.6- Traitement
    - Régime diététique hypocalorique et limitant l’apport glycémique
    - Insulinothérapie si régime inefficace
    """)


def prediction_page(language):
    # Titles
    if language == "English":
        st.markdown("<div class='main-title'>Diabetes Prediction using AI</div>", unsafe_allow_html=True)
        st.markdown("<div class='sub-title'>Enter your details to predict diabetes risk</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='main-title'>Prédiction du diabète avec l'IA</div>", unsafe_allow_html=True)
        st.markdown("<div class='sub-title'>Entrez vos informations pour prédire le risque de diabète</div>", unsafe_allow_html=True)

    st.markdown("<div class='form-container'>", unsafe_allow_html=True)
    
    # Input widgets
    gender = st.radio("Gender (0: Female, 1: Male)" if language=="English" else "Genre (0: Femme, 1: Homme)", [0,1])
    age = st.slider("Age" if language=="English" else "Âge", 0, 120, 30)
    hypertension = st.radio("Hypertension (0: No, 1: Yes)" if language=="English" else "Hypertension (0: Non, 1: Oui)", [0,1])
    heart_disease = st.radio("Heart Disease (0: No, 1: Yes)" if language=="English" else "Maladie Cardiaque (0: Non, 1: Oui)", [0,1])
    smoking_history = st.selectbox(
        "Smoking History (0: Never, 1: No-info, 2: Former, 3: Current, 4: Not-Current)" 
        if language=="English" else 
        "Historique de Tabagisme (0: Jamais, 1: Sans Info, 2: Ancien, 3: Actuel, 4: Non Actuel)", 
        [0,1,2,3,4]
    )
    bmi = st.number_input("BMI" if language=="English" else "IMC", 0.0, 100.0, 25.0)
    HbA1c_level = st.number_input("HbA1c Level" if language=="English" else "Niveau HbA1c", 0.0, 100.0, 5.7)
    blood_glucose_level = st.number_input(
        "Blood Glucose Level" if language=="English" else "Niveau de Glucose Sanguin", 
        0.0, 1000.0, 100.0
    )

    st.markdown("</div>", unsafe_allow_html=True)

    # Predict button
    if st.button("Predict" if language=="English" else "Prédire"):
        payload = {
            "gender": gender,
            "age": age,
            "hypertension": hypertension,
            "heart_disease": heart_disease,
            "smoking_history": smoking_history,
            "bmi": bmi,
            "HbA1c_level": HbA1c_level,
            "blood_glucose_level": blood_glucose_level
        }

        BACKEND_URL = "https://mybackend.onrender.com/predict"  # ton URL Render

        try:
            response = requests.post(BACKEND_URL, json=payload, timeout=10)
            response.raise_for_status()  # déclenche une exception si status != 200
            result = response.json()

            prediction = result.get("prediction")
            if prediction == 1:
                message = "Diabetic – consult a doctor urgently." if language=="English" else "Diabétique – consultez un médecin rapidement."
            elif prediction == 0:
                message = "Not diabetic." if language=="English" else "Non diabétique."
            else:
                message = "Prediction unavailable." if language=="English" else "Prédiction indisponible."

            st.markdown(f"<p class='result'>{message}</p>", unsafe_allow_html=True)

        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to backend: {e}")
        except Exception as e:
            st.error(f"Unexpected error: {e}")


# ---------------------------
# Main app navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Education", "Prediction"])

if page == "Home":
    home_page(language)
elif page == "Education":
    education_page()
elif page == "Prediction":
    prediction_page(language)
