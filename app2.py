import streamlit as st
import time

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="TribalScholar AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# SESSION STATE
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "🏠 Dashboard"

if "application_submitted" not in st.session_state:
    st.session_state.application_submitted = False

if "profile_saved" not in st.session_state:
    st.session_state.profile_saved = False

if "documents_verified" not in st.session_state:
    st.session_state.documents_verified = False


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

/* Main page */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Main heading */
.main-title {
    font-size: 38px;
    font-weight: 750;
    color: #4DA3FF;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 17px;
    color: #AAB2BD;
    margin-bottom: 25px;
}

/* General card */
.card {
    padding: 22px;
    border-radius: 14px;
    background: #18212F;
    border: 1px solid #2D3A4D;
    margin-bottom: 15px;
    color: #E8EDF3;
    min-height: 100px;
}

.card-title {
    font-size: 19px;
    font-weight: 650;
    color: #FFFFFF;
    margin-bottom: 8px;
}

.number {
    font-size: 31px;
    font-weight: 750;
    color: #4DA3FF;
    margin-bottom: 5px;
}

/* Scholarship card */
.scholarship-card {
    padding: 25px;
    border-radius: 15px;
    background: #18212F;
    border: 1px solid #2D3A4D;
    margin-top: 15px;
    margin-bottom: 15px;
    color: #E8EDF3;
}

.match-score {
    font-size: 36px;
    font-weight: 800;
    color: #46D39A;
}

/* Status */
.success-text {
    color: #46D39A;
    font-weight: 600;
}

.warning-text {
    color: #FFCC66;
    font-weight: 600;
}

/* Buttons */
.stButton > button {
    border-radius: 9px;
    padding: 0.55rem 1.2rem;
    font-weight: 600;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    border-right: 1px solid #30394A;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HELPER FUNCTION
# =========================================================

def change_page(page_name):
    st.session_state.page = page_name


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🎓 TribalScholar AI")
st.sidebar.caption("Scholarship & Fellowship Management")

pages = [
    "🏠 Dashboard",
    "🤖 AI Scholarship Matcher",
    "🔍 Explore Scholarships",
    "📝 Apply for Scholarship",
    "📂 My Applications",
    "📄 Document Verification",
    "📊 Application Tracker",
    "👤 Profile",
    "🛡️ Admin Dashboard"
]

selected_page = st.sidebar.radio(
    "Navigation",
    pages,
    index=pages.index(st.session_state.page)
)

st.session_state.page = selected_page

st.sidebar.divider()

st.sidebar.info(
    "🤖 AI-enabled scholarship assistance for Scheduled Tribe students."
)

st.sidebar.caption("Prototype • PS 26239")


# =========================================================
# DASHBOARD
# =========================================================

if st.session_state.page == "🏠 Dashboard":

    st.markdown(
        '<div class="main-title">Welcome, Student 👋</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Find, apply and track scholarships from one platform.'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="card">
            <div class="number">6</div>
            <b>Eligible Scholarships</b>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <div class="number">2</div>
            <b>Applications</b>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <div class="number">1</div>
            <b>Under Review</b>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="card">
            <div class="number">85%</div>
            <b>Profile Completed</b>
        </div>
        """, unsafe_allow_html=True)

    st.subheader("🎯 Recommended for You")

    st.markdown("""
    <div class="scholarship-card">

        <div class="card-title">
        National Fellowship for Scheduled Tribe Students
        </div>

        Financial assistance for eligible Scheduled Tribe students
        pursuing higher education and research programmes.

        <br><br>

        <span class="success-text">
        ● High Eligibility Match
        </span>

    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 4])

    with col1:
        if st.button("Check Eligibility", use_container_width=True):
            st.session_state.page = "🤖 AI Scholarship Matcher"
            st.rerun()

    with col2:
        if st.button("Explore Scholarships"):
            st.session_state.page = "🔍 Explore Scholarships"
            st.rerun()

    st.divider()

    st.subheader("🚀 How TribalScholar AI Works")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.info("👤\n\n**Create Profile**\n\nEnter academic and personal details.")

    with c2:
        st.info("🤖\n\n**AI Matching**\n\nFind suitable scholarship schemes.")

    with c3:
        st.info("📄\n\n**Verify Documents**\n\nPreliminary AI-assisted verification.")

    with c4:
        st.info("📊\n\n**Track Status**\n\nMonitor application progress.")


# =========================================================
# AI SCHOLARSHIP MATCHER
# =========================================================

elif st.session_state.page == "🤖 AI Scholarship Matcher":

    st.markdown(
        '<div class="main-title">🤖 AI Scholarship Matcher</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Enter your details to discover scholarship schemes "
        "that may match your profile."
    )

    st.info(
        "The prototype uses rule-based matching to demonstrate "
        "how an AI-powered recommendation engine could work."
    )

    st.subheader("👤 Student Information")

    col1, col2 = st.columns(2)

    with col1:

        age = st.number_input(
            "Age",
            min_value=15,
            max_value=60,
            value=20
        )

        gender = st.selectbox(
            "Gender",
            ["Female", "Male", "Other"]
        )

        state = st.selectbox(
            "State / UT",
            [
                "Delhi",
                "Haryana",
                "Rajasthan",
                "Madhya Pradesh",
                "Maharashtra",
                "Odisha",
                "Jharkhand",
                "Chhattisgarh",
                "Assam",
                "Other"
            ]
        )

        education = st.selectbox(
            "Current Education Level",
            [
                "Undergraduate",
                "Postgraduate",
                "PhD / Research"
            ]
        )

    with col2:

        income = st.number_input(
            "Annual Family Income (₹)",
            min_value=0,
            value=250000,
            step=10000
        )

        category = st.selectbox(
            "Category",
            [
                "Scheduled Tribe (ST)"
            ]
        )

        marks = st.slider(
            "Previous Academic Score (%)",
            min_value=0,
            max_value=100,
            value=75
        )

        certificate = st.selectbox(
            "Valid ST Certificate",
            ["Yes", "No"]
        )

    st.divider()

    if st.button(
        "✨ Find Scholarships for Me",
        type="primary",
        use_container_width=True
    ):

        with st.spinner("AI is analysing your profile..."):
            time.sleep(1.5)

        if certificate == "Yes":

            score = 70

            if marks >= 60:
                score += 8

            if income <= 600000:
                score += 7

            if education in ["Postgraduate", "PhD / Research"]:
                score += 7

            score = min(score, 95)

            st.success("✨ AI analysis completed!")

            st.subheader("🎓 Best Scholarship Match")

            st.markdown(f"""
            <div class="scholarship-card">

                <div class="card-title">
                National Fellowship for Scheduled Tribe Students
                </div>

                <br>

                <div class="match-score">
                {score}% Match
                </div>

                <br>

                <b>Why this scholarship was recommended</b>

                <br><br>

                ✅ Scheduled Tribe category matched<br>
                ✅ Academic profile matched<br>
                ✅ Family income considered<br>
                ✅ Education level analysed<br>
                ✅ Scholarship category matched

                <br><br>

                <span class="success-text">
                HIGH COMPATIBILITY
                </span>

            </div>
            """, unsafe_allow_html=True)

            st.progress(score / 100)

            st.caption(
                "The match score is a prototype recommendation and "
                "does not represent final government eligibility."
            )

            if st.button(
                "📝 Apply Now",
                type="primary"
            ):
                st.session_state.page = "📝 Apply for Scholarship"
                st.rerun()

            st.subheader("Other Possible Matches")

            c1, c2 = st.columns(2)

            with c1:
                st.markdown("""
                <div class="card">
                    <div class="card-title">
                    National Overseas Scholarship
                    </div>

                    🌍 Study Abroad<br><br>
                    Match: 76%
                </div>
                """, unsafe_allow_html=True)

            with c2:
                st.markdown("""
                <div class="card">
                    <div class="card-title">
                    Higher Education Scholarship Support
                    </div>

                    🎓 Higher Education<br><br>
                    Match: 71%
                </div>
                """, unsafe_allow_html=True)

        else:

            st.warning(
                "The selected schemes require a valid Scheduled "
                "Tribe certificate."
            )


# =========================================================
# EXPLORE SCHOLARSHIPS
# =========================================================

elif st.session_state.page == "🔍 Explore Scholarships":

    st.markdown(
        '<div class="main-title">🔍 Explore Scholarships</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Discover scholarships and fellowships based on your "
        "education and eligibility."
    )

    search = st.text_input(
        "🔎 Search Scholarships",
        placeholder="Search by scholarship name..."
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="scholarship-card">

            <div class="card-title">
            🎓 National Fellowship for Scheduled Tribe Students
            </div>

            <br>

            <b>Level:</b> Higher Education / Research<br><br>

            <b>Category:</b> Scheduled Tribe<br><br>

            <b>Purpose:</b> Fellowship assistance for eligible
            students pursuing advanced education.

            <br><br>

            <span class="success-text">
            ● Applications Open
            </span>

        </div>
        """, unsafe_allow_html=True)

        if st.button("Apply for Fellowship"):
            st.session_state.page = "📝 Apply for Scholarship"
            st.rerun()

    with col2:

        st.markdown("""
        <div class="scholarship-card">

            <div class="card-title">
            🌍 National Overseas Scholarship
            </div>

            <br>

            <b>Level:</b> Master's / PhD Abroad<br><br>

            <b>Category:</b> Eligible ST Students<br><br>

            <b>Purpose:</b> Financial assistance for eligible
            students pursuing higher education abroad.

            <br><br>

            <span class="success-text">
            ● Applications Open
            </span>

        </div>
        """, unsafe_allow_html=True)

        if st.button("Check Overseas Eligibility"):
            st.info(
                "Your academic, income and programme details "
                "will be checked against the scheme criteria."
            )


# =========================================================
# APPLY
# =========================================================

elif st.session_state.page == "📝 Apply for Scholarship":

    st.markdown(
        '<div class="main-title">📝 Scholarship Application</div>',
        unsafe_allow_html=True
    )

    st.write(
        "National Fellowship for Scheduled Tribe Students"
    )

    st.progress(0.25)

    st.subheader("1️⃣ Personal Information")

    col1, col2 = st.columns(2)

    with col1:

        name = st.text_input(
            "Full Name",
            placeholder="Enter full name"
        )

        dob = st.date_input("Date of Birth")

        phone = st.text_input(
            "Mobile Number",
            placeholder="+91 XXXXX XXXXX"
        )

    with col2:

        email = st.text_input(
            "Email Address",
            placeholder="student@example.com"
        )

        application_state = st.selectbox(
            "State / UT",
            [
                "Delhi",
                "Haryana",
                "Rajasthan",
                "Madhya Pradesh",
                "Maharashtra",
                "Odisha",
                "Jharkhand",
                "Chhattisgarh",
                "Other"
            ]
        )

        category_apply = st.selectbox(
            "Category",
            ["Scheduled Tribe (ST)"]
        )

    st.divider()

    st.subheader("2️⃣ Academic Information")

    col1, col2 = st.columns(2)

    with col1:

        institution = st.text_input(
            "Institution / University"
        )

        course = st.text_input(
            "Course / Programme",
            placeholder="Example: B.Tech / M.Tech / PhD"
        )

    with col2:

        year = st.selectbox(
            "Current Year",
            [
                "1st Year",
                "2nd Year",
                "3rd Year",
                "4th Year",
                "Research Scholar"
            ]
        )

        academic_score = st.number_input(
            "Previous Academic Percentage",
            min_value=0.0,
            max_value=100.0,
            value=75.0
        )

    st.divider()

    st.subheader("3️⃣ Financial Information")

    family_income = st.number_input(
        "Annual Family Income (₹)",
        min_value=0,
        value=250000,
        step=10000
    )

    st.divider()

    st.subheader("4️⃣ Documents")

    st.file_uploader(
        "Upload ST Certificate",
        type=["pdf", "jpg", "jpeg", "png"],
        key="apply_st"
    )

    st.file_uploader(
        "Upload Income Certificate",
        type=["pdf", "jpg", "jpeg", "png"],
        key="apply_income"
    )

    st.file_uploader(
        "Upload Academic Marksheet",
        type=["pdf", "jpg", "jpeg", "png"],
        key="apply_marks"
    )

    declaration = st.checkbox(
        "I declare that the information provided above is correct."
    )

    if st.button(
        "🚀 Submit Application",
        type="primary",
        use_container_width=True
    ):

        if not name:
            st.error("Please enter your name.")

        elif not declaration:
            st.error("Please accept the declaration.")

        else:

            with st.spinner("Submitting application..."):
                time.sleep(1)

            st.session_state.application_submitted = True

            st.success(
                "🎉 Application submitted successfully!"
            )

            st.info(
                "Application ID: NFST-2026-00124"
            )

            st.balloons()


# =========================================================
# MY APPLICATIONS
# =========================================================

elif st.session_state.page == "📂 My Applications":

    st.markdown(
        '<div class="main-title">📂 My Applications</div>',
        unsafe_allow_html=True
    )

    st.write("View all your scholarship applications.")

    st.markdown("""
    <div class="scholarship-card">

        <div class="card-title">
        National Fellowship for Scheduled Tribe Students
        </div>

        <br>

        <b>Application ID:</b> NFST-2026-00124

        <br><br>

        <b>Submitted:</b> 19 September 2026

        <br><br>

        <span class="warning-text">
        ● Under Verification
        </span>

    </div>
    """, unsafe_allow_html=True)

    st.progress(0.60)

    c1, c2, c3 = st.columns(3)

    c1.metric("Application", "Submitted")
    c2.metric("Documents", "Checking")
    c3.metric("Current Status", "Under Review")

    if st.button("Track Application"):
        st.session_state.page = "📊 Application Tracker"
        st.rerun()


# =========================================================
# DOCUMENT VERIFICATION
# =========================================================

elif st.session_state.page == "📄 Document Verification":

    st.markdown(
        '<div class="main-title">📄 AI Document Verification</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Upload your documents for preliminary AI-assisted verification."
    )

    st.warning(
        "Prototype feature: verification results shown here are "
        "simulated for demonstration purposes."
    )

    document_type = st.selectbox(
        "Document Type",
        [
            "Scheduled Tribe Certificate",
            "Income Certificate",
            "Academic Marksheet",
            "Identity Document"
        ]
    )

    document = st.file_uploader(
        "Upload Document",
        type=["pdf", "png", "jpg", "jpeg"]
    )

    if document is not None:

        st.success("Document uploaded successfully.")

        if st.button(
            "🤖 Verify Document",
            type="primary"
        ):

            with st.spinner(
                "AI is extracting and analysing document information..."
            ):
                time.sleep(2)

            st.session_state.documents_verified = True

    if st.session_state.documents_verified:

        st.success("✅ Preliminary verification completed")

        st.subheader("Verification Results")

        c1, c2 = st.columns(2)

        with c1:

            st.markdown("""
            <div class="card">

            <div class="card-title">
            Document Checks
            </div>

            ✅ File format valid<br><br>

            ✅ Document type recognised<br><br>

            ✅ Required fields detected<br><br>

            ✅ Name information detected<br><br>

            ⚠ Final authority verification pending

            </div>
            """, unsafe_allow_html=True)

        with c2:

            st.metric(
                "AI Verification Confidence",
                "91%"
            )

            st.progress(0.91)

            st.success(
                "No major preliminary issue detected."
            )

        st.caption(
            "Final document validation would be performed by "
            "the authorised institution/government authority."
        )


# =========================================================
# APPLICATION TRACKER
# =========================================================

elif st.session_state.page == "📊 Application Tracker":

    st.markdown(
        '<div class="main-title">📊 Application Tracker</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Application ID: **NFST-2026-00124**"
    )

    st.progress(0.60)

    st.subheader("Application Journey")

    st.success(
        "✓ 1. Application Submitted"
    )

    st.success(
        "✓ 2. Documents Uploaded"
    )

    st.success(
        "✓ 3. Preliminary AI Verification"
    )

    st.warning(
        "⏳ 4. Institute Verification — In Progress"
    )

    st.info(
        "○ 5. Ministry Review"
    )

    st.info(
        "○ 6. Final Decision"
    )

    st.divider()

    st.subheader("Latest Update")

    st.write(
        "Your application is currently being reviewed by "
        "the educational institution."
    )

    st.caption(
        "Last updated: 19 September 2026"
    )


# =========================================================
# PROFILE
# =========================================================

elif st.session_state.page == "👤 Profile":

    st.markdown(
        '<div class="main-title">👤 Student Profile</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Complete your profile to improve scholarship recommendations."
    )

    st.progress(0.85)

    st.caption("Profile Completion: 85%")

    col1, col2 = st.columns(2)

    with col1:

        profile_name = st.text_input(
            "Full Name",
            "Demo Student"
        )

        profile_email = st.text_input(
            "Email",
            "student@example.com"
        )

        profile_phone = st.text_input(
            "Mobile Number",
            "+91 98765 43210"
        )

    with col2:

        profile_category = st.selectbox(
            "Category",
            ["Scheduled Tribe (ST)"]
        )

        profile_education = st.selectbox(
            "Education",
            [
                "Undergraduate",
                "Postgraduate",
                "PhD / Research"
            ]
        )

        profile_income = st.number_input(
            "Annual Family Income",
            min_value=0,
            value=250000
        )

    if st.button(
        "💾 Save Profile",
        type="primary"
    ):

        st.session_state.profile_saved = True
        st.success("Profile updated successfully!")


# =========================================================
# ADMIN DASHBOARD
# =========================================================

elif st.session_state.page == "🛡️ Admin Dashboard":

    st.markdown(
        '<div class="main-title">🛡️ Admin Dashboard</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Monitor scholarship applications and verification status."
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Total Applications",
            "1,248",
            "+86"
        )

    with c2:
        st.metric(
            "Approved",
            "742"
        )

    with c3:
        st.metric(
            "Pending",
            "391"
        )

    with c4:
        st.metric(
            "Flagged",
            "115"
        )

    st.divider()

    st.subheader("📋 Recent Applications")

    applications = {
        "Application ID": [
            "NFST-2026-00124",
            "NFST-2026-00125",
            "NOS-2026-00321",
            "NFST-2026-00126"
        ],

        "Student": [
            "Student A",
            "Student B",
            "Student C",
            "Student D"
        ],

        "Scheme": [
            "National Fellowship",
            "National Fellowship",
            "Overseas Scholarship",
            "National Fellowship"
        ],

        "AI Check": [
            "Verified",
            "Verified",
            "Review Required",
            "Verified"
        ],

        "Status": [
            "Institute Review",
            "Ministry Review",
            "Document Review",
            "Approved"
        ]
    }

    st.dataframe(
        applications,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.subheader("🤖 AI-Assisted Review")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="card">

        <div class="card-title">
        Duplicate Detection
        </div>

        AI can flag potentially duplicate applications
        for manual review.

        <br><br>

        <span class="warning-text">
        23 applications require review
        </span>

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="card">

        <div class="card-title">
        Document Screening
        </div>

        Uploaded documents can undergo preliminary
        automated screening before official verification.

        <br><br>

        <span class="success-text">
        91% processed
        </span>

        </div>
        """, unsafe_allow_html=True)

    st.subheader("📈 Application Overview")

    chart_data = {
        "Applications": [
            120,
            190,
            260,
            340,
            420,
            510
        ]
    }

    st.bar_chart(chart_data)