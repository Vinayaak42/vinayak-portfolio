import streamlit as st
import os
import json
from datetime import datetime
import pandas as pd
import plotly.express as px

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Vinayak Kesti | Data Scientist",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# PATHS
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
DATA_DIR = os.path.join(BASE_DIR, "data")

os.makedirs(ASSETS_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)

PROFILE_FILE = os.path.join(DATA_DIR, "profile.json")
PROJECT_FILE = os.path.join(DATA_DIR, "projects.json")

# ============================================================
# DEFAULT PROFILE
# ============================================================

DEFAULT_PROFILE = {
    "name": "Vinayak Kesti",
    "headline": "Data Scientist | Data Analyst | AI & Machine Learning",
    "location": "Bangalore, Karnataka, India",
    "email": "vinayakkesti42@gmail.com",
    "phone": "+91-7676369133",
    "github": "https://github.com/Vinayaak42",
    "linkedin": "https://www.linkedin.com/in/vinayak-kesti",
    "about": (
        "I am passionate about solving business and engineering problems "
        "using data-driven approaches. My background combines manufacturing "
        "quality analytics, Python, SQL, Power BI and Machine Learning. "
        "My focus is on building practical solutions that combine data analytics, "
        "machine learning, artificial intelligence and modern application development."
    )
}

# ============================================================
# DEFAULT PROJECTS
# ============================================================

DEFAULT_PROJECTS = [
    {
        "id": "ai-data-analyst",
        "title": "AI Data Analyst",
        "emoji": "🤖",
        "category": "Generative AI",
        "description": (
            "AI-powered data analysis platform for dataset profiling, "
            "automatic EDA, pattern detection, machine learning and "
            "natural-language interaction with data."
        ),
        "technologies": [
            "Python",
            "Streamlit",
            "Pandas",
            "Scikit-learn",
            "Generative AI"
        ],
        "github": "https://github.com/Vinayaak42",
        "demo": "",
        "created_at": "2026-09-07T10:00:00"
    },
    {
        "id": "healthcare-readmission",
        "title": "Healthcare Readmission Prediction",
        "emoji": "🏥",
        "category": "Machine Learning",
        "description": (
            "Machine learning system for predicting hospital readmission "
            "risk using patient and healthcare information."
        ),
        "technologies": [
            "Python",
            "TensorFlow",
            "Keras",
            "Scikit-learn",
            "Streamlit"
        ],
        "github": "https://github.com/Vinayaak42",
        "demo": "",
        "created_at": "2026-09-06T10:00:00"
    },
    {
        "id": "secureguard-ai",
        "title": "SecureGuard AI Risk Platform",
        "emoji": "🛡️",
        "category": "AI Platform",
        "description": (
            "Intelligent risk analysis platform combining machine learning "
            "and AI-based insights for automated risk assessment."
        ),
        "technologies": [
            "Python",
            "Machine Learning",
            "FastAPI",
            "Streamlit"
        ],
        "github": "https://github.com/Vinayaak42",
        "demo": "",
        "created_at": "2026-09-05T10:00:00"
    },
    {
        "id": "ml-cloud-lab",
        "title": "ML Cloud Lab",
        "emoji": "☁️",
        "category": "Machine Learning",
        "description": (
            "Interactive platform for experimenting with machine learning "
            "algorithms through a modern cloud-ready application."
        ),
        "technologies": [
            "Python",
            "FastAPI",
            "React",
            "Scikit-learn",
            "Docker"
        ],
        "github": "https://github.com/Vinayaak42",
        "demo": "",
        "created_at": "2026-09-04T10:00:00"
    },
    {
        "id": "medical-cost",
        "title": "Medical Cost Prediction",
        "emoji": "💰",
        "category": "Machine Learning",
        "description": (
            "Regression-based machine learning application for predicting "
            "medical insurance costs."
        ),
        "technologies": [
            "Python",
            "Pandas",
            "Scikit-learn",
            "Matplotlib"
        ],
        "github": "https://github.com/Vinayaak42",
        "demo": "",
        "created_at": "2026-09-03T10:00:00"
    },
    {
        "id": "heart-disease",
        "title": "Heart Disease Prediction",
        "emoji": "❤️",
        "category": "Machine Learning",
        "description": (
            "Classification model designed to predict heart disease risk "
            "using supervised machine learning."
        ),
        "technologies": [
            "Python",
            "Pandas",
            "Scikit-learn",
            "Streamlit"
        ],
        "github": "https://github.com/Vinayaak42",
        "demo": "",
        "created_at": "2026-09-02T10:00:00"
    },
    {
        "id": "employee-turnover",
        "title": "Employee Turnover Prediction",
        "emoji": "👥",
        "category": "Data Science",
        "description": (
            "Predictive analytics solution for identifying employees "
            "who may be at risk of leaving an organization."
        ),
        "technologies": [
            "Python",
            "SQL",
            "Scikit-learn",
            "Power BI"
        ],
        "github": "https://github.com/Vinayaak42",
        "demo": "",
        "created_at": "2026-09-01T10:00:00"
    },
    {
        "id": "home-loan",
        "title": "Home Loan Default Prediction",
        "emoji": "🏦",
        "category": "Machine Learning",
        "description": (
            "Credit risk prediction model for identifying potential "
            "loan default cases."
        ),
        "technologies": [
            "Python",
            "Pandas",
            "Scikit-learn",
            "Machine Learning"
        ],
        "github": "https://github.com/Vinayaak42",
        "demo": "",
        "created_at": "2026-08-30T10:00:00"
    },
    {
        "id": "pan-tampering",
        "title": "PAN Card Tampering Detection",
        "emoji": "🪪",
        "category": "Computer Vision",
        "description": (
            "Computer vision application for detecting possible "
            "document modifications and tampering."
        ),
        "technologies": [
            "Python",
            "OpenCV",
            "Computer Vision",
            "Flask"
        ],
        "github": "https://github.com/Vinayaak42",
        "demo": "",
        "created_at": "2026-08-29T10:00:00"
    },
    {
        "id": "powerbi-quality",
        "title": "Advanced Power BI Quality Dashboard",
        "emoji": "📊",
        "category": "Power BI",
        "description": (
            "Advanced business intelligence dashboard for quality KPIs, "
            "production trends, defect analysis and operational performance."
        ),
        "technologies": [
            "Power BI",
            "DAX",
            "Excel",
            "SQL"
        ],
        "github": "https://github.com/Vinayaak42",
        "demo": "",
        "created_at": "2026-08-28T10:00:00"
    },
    {
        "id": "ai-sql-assistant",
        "title": "AI SQL Assistant",
        "emoji": "🧠",
        "category": "Generative AI",
        "description": (
            "Natural-language SQL assistant for schema understanding, "
            "SQL generation, query explanation and data analysis."
        ),
        "technologies": [
            "Python",
            "SQL",
            "LangChain",
            "Streamlit",
            "NLP"
        ],
        "github": "https://github.com/Vinayaak42",
        "demo": "",
        "created_at": "2026-08-27T10:00:00"
    }
]

# ============================================================
# SKILLS
# ============================================================

SKILLS = {
    "Python": 92,
    "SQL": 90,
    "Data Analysis": 90,
    "Machine Learning": 88,
    "Power BI": 88,
    "Data Visualization": 87,
    "Scikit-learn": 87,
    "Streamlit": 86,
    "TensorFlow / Keras": 82,
    "Deep Learning": 82,
    "Flask": 80,
    "Generative AI": 80,
    "Computer Vision": 78,
    "FastAPI": 75,
    "Docker": 70
}

# ============================================================
# TECHNOLOGY STACK
# ============================================================

TECH_STACK = {
    "Programming": [
        "Python",
        "SQL",
        "Git",
        "REST APIs"
    ],
    "Data Analytics": [
        "Pandas",
        "NumPy",
        "Excel",
        "SQL"
    ],
    "Machine Learning": [
        "Scikit-learn",
        "Regression",
        "Classification",
        "Clustering"
    ],
    "Deep Learning": [
        "TensorFlow",
        "Keras",
        "Neural Networks",
        "Computer Vision"
    ],
    "Visualization": [
        "Power BI",
        "DAX",
        "Matplotlib",
        "Plotly"
    ],
    "Deployment": [
        "Streamlit",
        "Flask",
        "FastAPI",
        "Docker"
    ]
}

# ============================================================
# LOAD / SAVE
# ============================================================

def load_json(file_path, default_value):
    try:
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                return json.load(file)
    except Exception:
        pass

    return default_value


def save_json(file_path, data):
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )
        return True
    except Exception:
        return False


profile = load_json(PROFILE_FILE, DEFAULT_PROFILE.copy())
projects = load_json(PROJECT_FILE, DEFAULT_PROJECTS.copy())

if not os.path.exists(PROFILE_FILE):
    save_json(PROFILE_FILE, profile)

if not os.path.exists(PROJECT_FILE):
    save_json(PROJECT_FILE, projects)

# ============================================================
# PROFILE PHOTO
# ============================================================

def find_profile_photo():

    file_names = [
        "profile.jpg",
        "profile.jpeg",
        "profile.png",
        "profile.webp"
    ]

    for file_name in file_names:

        path = os.path.join(
            ASSETS_DIR,
            file_name
        )

        if os.path.exists(path):
            return path

    return None


profile_photo = find_profile_photo()

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("🚀 Vinayak Kesti")

    st.caption(
        "Data Scientist • Data Analyst • AI/ML"
    )

    st.divider()

    page = st.radio(
        "Navigate",
        [
            "🏠 Home",
            "👨‍💻 About",
            "🚀 Projects",
            "🧠 Skills",
            "🛠️ Technology",
            "📩 Contact"
        ]
    )

    st.divider()

    st.subheader("🔗 Connect")

    st.link_button(
        "💻 GitHub",
        profile.get(
            "github",
            DEFAULT_PROFILE["github"]
        ),
        use_container_width=True
    )

    st.link_button(
        "💼 LinkedIn",
        profile.get(
            "linkedin",
            DEFAULT_PROFILE["linkedin"]
        ),
        use_container_width=True
    )

    st.divider()

    st.caption("© 2026 Vinayak Kesti")

# ============================================================
# SORT PROJECTS
# ============================================================

projects = sorted(
    projects,
    key=lambda project: project.get(
        "created_at",
        ""
    ),
    reverse=True
)

# ============================================================
# HOME
# ============================================================

if page == "🏠 Home":

    left, right = st.columns(
        [1.8, 1],
        gap="large"
    )

    with left:

        st.success(
            "🚀 Open to Data Science, Data Analytics & AI opportunities"
        )

        st.title(
            "Vinayak Kesti"
        )

        st.subheader(
            "Data Scientist | Data Analyst | AI & Machine Learning"
        )

        st.write(
            f"📍 {profile.get('location', '')}"
        )

        st.write("")

        st.write(
            "I build data-driven applications, predictive machine "
            "learning systems, AI solutions and business intelligence dashboards."
        )

        st.write("")

        c1, c2 = st.columns(2)

        with c1:
            st.link_button(
                "💼 LinkedIn",
                profile["linkedin"],
                use_container_width=True
            )

        with c2:
            st.link_button(
                "💻 GitHub",
                profile["github"],
                use_container_width=True
            )

    with right:

        if profile_photo:

            st.image(
                profile_photo,
                width=250
            )

        else:

            st.info(
                "📷 Add your profile photo here:\n\n"
                "assets/profile.jpg"
            )

    st.divider()

    # ========================================================
    # METRICS
    # ========================================================

    m1, m2, m3, m4 = st.columns(4)

    with m1:
        st.metric(
            "Core Skills",
            "15+"
        )

    with m2:
        st.metric(
            "Projects",
            f"{len(projects)}+"
        )

    with m3:
        st.metric(
            "Primary Focus",
            "AI / ML"
        )

    with m4:
        st.metric(
            "Analytics",
            "BI"
        )

    st.divider()

    st.header("🔥 Featured Projects")

    featured_projects = projects[:3]

    for project_index in range(
        0,
        len(featured_projects),
        3
    ):

        row = featured_projects[
            project_index:project_index + 3
        ]

        columns = st.columns(3)

        for index, project in enumerate(row):

            with columns[index]:

                st.subheader(
                    f"{project.get('emoji', '🚀')} "
                    f"{project.get('title', 'Project')}"
                )

                st.caption(
                    project.get(
                        "category",
                        "Data Science"
                    )
                )

                st.write(
                    project.get(
                        "description",
                        ""
                    )
                )

                st.write(
                    " • ".join(
                        project.get(
                            "technologies",
                            []
                        )
                    )
                )

                if project.get("github"):

                    st.link_button(
                        "💻 GitHub",
                        project["github"],
                        use_container_width=True
                    )

# ============================================================
# ABOUT
# ============================================================

elif page == "👨‍💻 About":

    st.title("👨‍💻 About Me")

    st.divider()

    left, right = st.columns(
        [2, 1],
        gap="large"
    )

    with left:

        st.header(
            "Turning Data Into Decisions"
        )

        st.write(
            "I am passionate about solving business and engineering "
            "problems using data-driven approaches. My background combines "
            "manufacturing quality analytics, Python, SQL, Power BI and "
            "Machine Learning."
        )

        st.write(
            "My focus is on building practical solutions that combine "
            "data analytics, machine learning, artificial intelligence "
            "and modern application development."
        )

        st.write(
            "I enjoy transforming raw data into meaningful insights, "
            "developing predictive models and building applications that "
            "solve practical real-world problems."
        )

    with right:

        st.header("📌 Profile")

        st.write(
            f"**📍 Location:** {profile.get('location', '')}"
        )

        st.write(
            f"**📧 Email:** {profile.get('email', '')}"
        )

        st.write(
            f"**📱 Phone:** {profile.get('phone', '')}"
        )

    st.divider()

    st.header("🎯 Professional Focus")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.subheader("📊 Data Analytics")

        st.write(
            "SQL, Excel, Power BI, EDA, KPI analysis "
            "and business insights."
        )

    with c2:

        st.subheader("🤖 Machine Learning")

        st.write(
            "Regression, classification, clustering, "
            "feature engineering and model evaluation."
        )

    with c3:

        st.subheader("🧠 AI & GenAI")

        st.write(
            "Generative AI, NLP, intelligent applications "
            "and AI-powered automation."
        )

# ============================================================
# PROJECTS
# ============================================================

elif page == "🚀 Projects":

    st.title("🚀 Projects")

    st.write(
        "Projects are automatically arranged from newest to oldest."
    )

    st.divider()

    search = st.text_input(
        "🔎 Search Projects",
        placeholder="Search project name, technology or category..."
    )

    categories = sorted(
        set(
            project.get(
                "category",
                "Other"
            )
            for project in projects
        )
    )

    selected_category = st.selectbox(
        "📂 Filter by Category",
        ["All"] + categories
    )

    filtered = []

    for project in projects:

        searchable_text = (
            project.get("title", "")
            + " "
            + project.get("category", "")
            + " "
            + project.get("description", "")
            + " "
            + " ".join(
                project.get(
                    "technologies",
                    []
                )
            )
        ).lower()

        search_match = (
            not search
            or search.lower() in searchable_text
        )

        category_match = (
            selected_category == "All"
            or project.get("category") == selected_category
        )

        if search_match and category_match:
            filtered.append(project)

    st.write(
        f"### {len(filtered)} project(s) found"
    )

    for start in range(
        0,
        len(filtered),
        3
    ):

        row_projects = filtered[
            start:start + 3
        ]

        columns = st.columns(3)

        for index, project in enumerate(row_projects):

            with columns[index]:

                st.subheader(
                    f"{project.get('emoji', '🚀')} "
                    f"{project.get('title', 'Project')}"
                )

                st.caption(
                    project.get(
                        "category",
                        "Project"
                    )
                )

                st.write(
                    project.get(
                        "description",
                        ""
                    )
                )

                st.write("**Technologies:**")

                technologies = project.get(
                    "technologies",
                    []
                )

                for technology in technologies:

                    st.write(
                        f"• {technology}"
                    )

                if project.get("github"):

                    st.link_button(
                        "💻 GitHub",
                        project["github"],
                        use_container_width=True
                    )

                if project.get("demo"):

                    st.link_button(
                        "🚀 Live Demo",
                        project["demo"],
                        use_container_width=True
                    )

                else:

                    st.caption(
                        "🚀 Live demo coming soon"
                    )

        st.divider()

# ============================================================
# SKILLS
# ============================================================

elif page == "🧠 Skills":

    st.title("🧠 Skills")

    st.divider()

    skill_df = pd.DataFrame(
        {
            "Skill": list(SKILLS.keys()),
            "Proficiency": list(SKILLS.values())
        }
    )

    skill_df = skill_df.sort_values(
        "Proficiency",
        ascending=True
    )

    fig = px.bar(
        skill_df,
        x="Proficiency",
        y="Skill",
        orientation="h",
        text="Proficiency"
    )

    fig.update_traces(
        texttemplate="%{text}%",
        textposition="outside"
    )

    fig.update_layout(
        height=650,
        xaxis=dict(
            range=[0, 100],
            title="Proficiency (%)"
        ),
        yaxis_title=""
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ============================================================
# TECHNOLOGY
# ============================================================

elif page == "🛠️ Technology":

    st.title("🛠️ Technology Stack")

    st.divider()

    categories = list(
        TECH_STACK.keys()
    )

    for start in range(
        0,
        len(categories),
        2
    ):

        columns = st.columns(2)

        row_categories = categories[
            start:start + 2
        ]

        for index, category in enumerate(
            row_categories
        ):

            with columns[index]:

                st.subheader(
                    category
                )

                for technology in TECH_STACK[category]:

                    st.write(
                        f"• {technology}"
                    )

# ============================================================
# CONTACT
# ============================================================

elif page == "📩 Contact":

    st.title("📩 Let's Connect")

    st.divider()

    left, right = st.columns(
        [1, 1.5],
        gap="large"
    )

    with left:

        st.header(
            "Let's Work Together"
        )

        st.write(
            "I am interested in opportunities involving Data Science, "
            "Data Analytics, Machine Learning, AI and intelligent automation."
        )

        st.write("")

        st.write(
            f"📧 **Email:** {profile.get('email', '')}"
        )

        st.write(
            f"📱 **Phone:** {profile.get('phone', '')}"
        )

        st.write(
            f"📍 **Location:** {profile.get('location', '')}"
        )

        st.write("")

        st.link_button(
            "💼 LinkedIn",
            profile["linkedin"],
            use_container_width=True
        )

        st.link_button(
            "💻 GitHub",
            profile["github"],
            use_container_width=True
        )

    with right:

        st.header("Send a Message")

        with st.form("contact_form"):

            name = st.text_input(
                "Your Name"
            )

            email = st.text_input(
                "Your Email"
            )

            subject = st.text_input(
                "Subject"
            )

            message = st.text_area(
                "Message",
                height=180
            )

            submitted = st.form_submit_button(
                "🚀 Send Message",
                use_container_width=True
            )

            if submitted:

                if (
                    name.strip()
                    and email.strip()
                    and message.strip()
                ):

                    st.success(
                        "Thank you! Your message has been captured."
                    )

                    st.info(
                        f"Please send the message to {profile.get('email', '')}."
                    )

                else:

                    st.warning(
                        "Please fill in Name, Email and Message."
                    )

# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🚀 Vinayak Kesti | Data Science • Data Analytics • AI • Machine Learning"
)
