import streamlit as st
import json
import os
import uuid
from datetime import datetime


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Admin Panel | Vinayak Kesti",
    page_icon="🔐",
    layout="wide",
)


# ============================================================
# PATHS
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

DATA_FILE = os.path.join(
    BASE_DIR,
    "portfolio_data.json"
)


# ============================================================
# ADMIN PASSWORD
# ============================================================

ADMIN_PASSWORD = "Vinayak@123"


# ============================================================
# DATA FUNCTIONS
# ============================================================

def load_data():

    if not os.path.exists(DATA_FILE):

        return {
            "profile": {},
            "projects": [],
            "skills": {},
            "tech_stack": {}
        }

    with open(
        DATA_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def save_data(data):

    with open(
        DATA_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )


# ============================================================
# SESSION
# ============================================================

if "admin_logged_in" not in st.session_state:

    st.session_state.admin_logged_in = False


# ============================================================
# LOGIN
# ============================================================

if not st.session_state.admin_logged_in:

    st.markdown(
        """
        <style>

        .login-box {
            max-width: 500px;
            margin: 80px auto;
            padding: 35px;
            border-radius: 20px;
            border: 1px solid #263244;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("🔐 Portfolio Admin")

    st.subheader(
        "Vinayak Kesti"
    )

    st.caption(
        "Manage your portfolio content"
    )

    st.divider()

    password = st.text_input(
        "🔑 Admin Password",
        type="password"
    )

    if st.button(
        "🚀 Login",
        use_container_width=True
    ):

        if password == ADMIN_PASSWORD:

            st.session_state.admin_logged_in = True

            st.success(
                "Login successful!"
            )

            st.rerun()

        else:

            st.error(
                "❌ Incorrect password."
            )

    st.stop()


# ============================================================
# LOAD DATA
# ============================================================

DATA = load_data()

PROFILE = DATA.setdefault(
    "profile",
    {}
)

PROJECTS = DATA.setdefault(
    "projects",
    []
)

SKILLS = DATA.setdefault(
    "skills",
    {}
)

TECH_STACK = DATA.setdefault(
    "tech_stack",
    {}
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("🔐 Admin Panel")

    st.caption(
        "Vinayak Kesti Portfolio"
    )

    st.divider()

    page = st.radio(
        "Navigation",
        [
            "📊 Dashboard",
            "👤 Profile",
            "🚀 Projects",
            "🧠 Skills",
            "🛠️ Technology Stack",
        ]
    )

    st.divider()

    if st.button(
        "🚪 Logout",
        use_container_width=True
    ):

        st.session_state.admin_logged_in = False

        st.rerun()


# ============================================================
# DASHBOARD
# ============================================================

if page == "📊 Dashboard":

    st.title("📊 Portfolio Dashboard")

    st.caption(
        "Manage your professional portfolio from one place."
    )

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "🚀 Projects",
        len(PROJECTS)
    )

    col2.metric(
        "🧠 Skills",
        len(SKILLS)
    )

    col3.metric(
        "🛠️ Tech Categories",
        len(TECH_STACK)
    )

    col4.metric(
        "👤 Profile",
        "Active"
    )

    st.divider()

    st.subheader(
        "🕒 Recent Projects"
    )

    sorted_projects = sorted(
        PROJECTS,
        key=lambda x: x.get(
            "created_at",
            ""
        ),
        reverse=True
    )

    for project in sorted_projects[:5]:

        created = project.get(
            "created_at",
            ""
        )

        st.write(
            f"{project.get('emoji', '🚀')} "
            f"**{project.get('title', 'Untitled')}**"
        )

        st.caption(
            f"{project.get('category', '')} · {created}"
        )


# ============================================================
# PROFILE MANAGEMENT
# ============================================================

elif page == "👤 Profile":

    st.title("👤 Profile Management")

    st.caption(
        "Update your professional information."
    )

    st.divider()

    with st.form(
        "profile_form"
    ):

        name = st.text_input(
            "Full Name",
            value=PROFILE.get(
                "name",
                ""
            )
        )

        headline = st.text_input(
            "Professional Headline",
            value=PROFILE.get(
                "headline",
                ""
            )
        )

        location = st.text_input(
            "Location",
            value=PROFILE.get(
                "location",
                ""
            )
        )

        email = st.text_input(
            "Email",
            value=PROFILE.get(
                "email",
                ""
            )
        )

        phone = st.text_input(
            "Phone",
            value=PROFILE.get(
                "phone",
                ""
            )
        )

        github = st.text_input(
            "GitHub URL",
            value=PROFILE.get(
                "github",
                ""
            )
        )

        linkedin = st.text_input(
            "LinkedIn URL",
            value=PROFILE.get(
                "linkedin",
                ""
            )
        )

        about = st.text_area(
            "About Me",
            value=PROFILE.get(
                "about",
                ""
            ),
            height=120
        )

        about_extended = st.text_area(
            "Extended About",
            value=PROFILE.get(
                "about_extended",
                ""
            ),
            height=120
        )

        save_profile = st.form_submit_button(
            "💾 Save Profile",
            use_container_width=True
        )

        if save_profile:

            DATA["profile"] = {
                "name": name,
                "headline": headline,
                "location": location,
                "email": email,
                "phone": phone,
                "github": github,
                "linkedin": linkedin,
                "about": about,
                "about_extended": about_extended,
            }

            save_data(DATA)

            st.success(
                "✅ Profile updated successfully!"
            )

            st.rerun()


# ============================================================
# PROJECT MANAGEMENT
# ============================================================

elif page == "🚀 Projects":

    st.title("🚀 Project Management")

    st.caption(
        "Add, edit or remove portfolio projects."
    )

    st.divider()

    tab1, tab2, tab3 = st.tabs(
        [
            "➕ Add Project",
            "✏️ Edit Project",
            "🗑️ Delete Project",
        ]
    )


    # ========================================================
    # ADD PROJECT
    # ========================================================

    with tab1:

        st.subheader(
            "➕ Add New Project"
        )

        with st.form(
            "add_project_form"
        ):

            emoji = st.text_input(
                "Project Emoji",
                value="🚀"
            )

            title = st.text_input(
                "Project Title"
            )

            category = st.text_input(
                "Category",
                placeholder="Machine Learning · Data Science"
            )

            tech_text = st.text_input(
                "Technologies",
                placeholder="Python, Pandas, Scikit-learn"
            )

            description = st.text_area(
                "Description",
                height=140
            )

            demo = st.text_input(
                "Live Demo URL",
                value="#"
            )

            github = st.text_input(
                "GitHub URL",
                value="https://github.com/Vinayaak42"
            )

            add_project = st.form_submit_button(
                "🚀 Add Project",
                use_container_width=True
            )

            if add_project:

                if not title.strip():

                    st.error(
                        "Project title is required."
                    )

                elif not description.strip():

                    st.error(
                        "Project description is required."
                    )

                else:

                    project = {

                        "id": str(
                            uuid.uuid4()
                        ),

                        "emoji": emoji,

                        "title": title.strip(),

                        "category": category.strip(),

                        "tech": [
                            item.strip()
                            for item in tech_text.split(",")
                            if item.strip()
                        ],

                        "description": description.strip(),

                        "demo": demo.strip(),

                        "github": github.strip(),

                        "created_at":
                            datetime.now().isoformat(),
                    }

                    DATA["projects"].append(
                        project
                    )

                    save_data(DATA)

                    st.success(
                        "🎉 Project added successfully!"
                    )

                    st.info(
                        "The new project will automatically "
                        "appear at the top of the portfolio."
                    )

                    st.rerun()


    # ========================================================
    # EDIT PROJECT
    # ========================================================

    with tab2:

        st.subheader(
            "✏️ Edit Project"
        )

        if not PROJECTS:

            st.info(
                "No projects available."
            )

        else:

            project_titles = [
                f"{p.get('emoji', '🚀')} "
                f"{p.get('title', 'Untitled')}"
                for p in PROJECTS
            ]

            selected_index = st.selectbox(
                "Select Project",
                range(len(PROJECTS)),
                format_func=lambda i:
                    project_titles[i]
            )

            project = PROJECTS[
                selected_index
            ]

            with st.form(
                "edit_project_form"
            ):

                emoji = st.text_input(
                    "Project Emoji",
                    value=project.get(
                        "emoji",
                        "🚀"
                    )
                )

                title = st.text_input(
                    "Project Title",
                    value=project.get(
                        "title",
                        ""
                    )
                )

                category = st.text_input(
                    "Category",
                    value=project.get(
                        "category",
                        ""
                    )
                )

                tech_text = st.text_input(
                    "Technologies",
                    value=", ".join(
                        project.get(
                            "tech",
                            []
                        )
                    )
                )

                description = st.text_area(
                    "Description",
                    value=project.get(
                        "description",
                        ""
                    ),
                    height=140
                )

                demo = st.text_input(
                    "Live Demo URL",
                    value=project.get(
                        "demo",
                        "#"
                    )
                )

                github = st.text_input(
                    "GitHub URL",
                    value=project.get(
                        "github",
                        ""
                    )
                )

                update_project = st.form_submit_button(
                    "💾 Update Project",
                    use_container_width=True
                )

                if update_project:

                    DATA["projects"][
                        selected_index
                    ] = {

                        "id": project.get(
                            "id",
                            str(uuid.uuid4())
                        ),

                        "emoji": emoji,

                        "title": title.strip(),

                        "category": category.strip(),

                        "tech": [
                            item.strip()
                            for item in tech_text.split(",")
                            if item.strip()
                        ],

                        "description":
                            description.strip(),

                        "demo": demo.strip(),

                        "github": github.strip(),

                        # Keep original creation date
                        "created_at":
                            project.get(
                                "created_at",
                                datetime.now().isoformat()
                            ),
                    }

                    save_data(DATA)

                    st.success(
                        "✅ Project updated successfully!"
                    )

                    st.rerun()


    # ========================================================
    # DELETE PROJECT
    # ========================================================

    with tab3:

        st.subheader(
            "🗑️ Delete Project"
        )

        if not PROJECTS:

            st.info(
                "No projects available."
            )

        else:

            delete_titles = [
                f"{p.get('emoji', '🚀')} "
                f"{p.get('title', 'Untitled')}"
                for p in PROJECTS
            ]

            delete_index = st.selectbox(
                "Select Project to Delete",
                range(len(PROJECTS)),
                format_func=lambda i:
                    delete_titles[i],
                key="delete_project_select"
            )

            selected_project = PROJECTS[
                delete_index
            ]

            st.warning(
                f"You are about to delete: "
                f"**{selected_project.get('title')}**"
            )

            confirm = st.checkbox(
                "I understand that this project will be permanently deleted."
            )

            if st.button(
                "🗑️ Delete Project",
                type="primary",
                disabled=not confirm,
                use_container_width=True
            ):

                DATA["projects"].pop(
                    delete_index
                )

                save_data(DATA)

                st.success(
                    "🗑️ Project deleted successfully!"
                )

                st.rerun()


# ============================================================
# SKILLS MANAGEMENT
# ============================================================

elif page == "🧠 Skills":

    st.title("🧠 Skills Management")

    st.caption(
        "Add, edit or remove technical skills."
    )

    st.divider()

    tab1, tab2 = st.tabs(
        [
            "➕ Add / Update",
            "🗑️ Delete"
        ]
    )


    # ========================================================
    # ADD / UPDATE SKILL
    # ========================================================

    with tab1:

        with st.form(
            "skill_form"
        ):

            skill_name = st.text_input(
                "Skill Name",
                placeholder="Python"
            )

            proficiency = st.slider(
                "Proficiency (%)",
                0,
                100,
                80
            )

            save_skill = st.form_submit_button(
                "💾 Save Skill",
                use_container_width=True
            )

            if save_skill:

                if not skill_name.strip():

                    st.error(
                        "Skill name is required."
                    )

                else:

                    DATA["skills"][
                        skill_name.strip()
                    ] = proficiency

                    save_data(DATA)

                    st.success(
                        "✅ Skill saved successfully!"
                    )

                    st.rerun()


    # ========================================================
    # DELETE SKILL
    # ========================================================

    with tab2:

        skill_list = list(
            DATA["skills"].keys()
        )

        if skill_list:

            selected_skill = st.selectbox(
                "Select Skill",
                skill_list
            )

            confirm_skill = st.checkbox(
                "Confirm skill deletion"
            )

            if st.button(
                "🗑️ Delete Skill",
                disabled=not confirm_skill,
                use_container_width=True
            ):

                del DATA["skills"][
                    selected_skill
                ]

                save_data(DATA)

                st.success(
                    "Skill deleted."
                )

                st.rerun()

        else:

            st.info(
                "No skills available."
            )


# ============================================================
# TECHNOLOGY STACK
# ============================================================

elif page == "🛠️ Technology Stack":

    st.title("🛠️ Technology Stack")

    st.caption(
        "Manage your technology categories."
    )

    st.divider()

    category_name = st.text_input(
        "Category",
        placeholder="🐍 Programming"
    )

    technologies_text = st.text_area(
        "Technologies",
        placeholder="Python, SQL, C++, C"
    )

    if st.button(
        "💾 Save Category",
        use_container_width=True
    ):

        if not category_name.strip():

            st.error(
                "Category name is required."
            )

        else:

            DATA["tech_stack"][
                category_name.strip()
            ] = [
                item.strip()
                for item in technologies_text.split(",")
                if item.strip()
            ]

            save_data(DATA)

            st.success(
                "Technology category saved!"
            )

            st.rerun()


    st.divider()

    st.subheader(
        "Existing Categories"
    )

    for category, technologies in DATA["tech_stack"].items():

        with st.expander(category):

            st.write(
                ", ".join(technologies)
            )

            if st.button(
                f"🗑️ Delete {category}",
                key=f"delete_{category}"
            ):

                del DATA["tech_stack"][
                    category
                ]

                save_data(DATA)

                st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🔐 Vinayak Kesti Portfolio Admin Panel"
)
