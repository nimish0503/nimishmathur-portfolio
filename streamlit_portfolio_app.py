# Nimish Mathur — Streamlit Portfolio (Final Version with Work Experience Added)

import os
import streamlit as st

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(page_title="Nimish Mathur — Portfolio", page_icon="📊", layout="wide")

# --------------------------------------------------
# CSS — Dark Modern Aesthetic
# --------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

:root {
  --bg: #0b0f14;
  --card: #111923;
  --accent: #00d1b2;
  --muted: #9aa4ad;
  --text: #e6edf3;
}

html, body, [class*="css"] {
  font-family: 'Inter', sans-serif;
  background: var(--bg);
}

.main .block-container { max-width: 1150px; padding-top: 1.0rem; }
[data-testid="stSidebar"] { background: #0a121a; }
[data-testid="stSidebar"] a:hover { color: #00d1b2; }

h1,h2,h3,h4 { color: var(--text); letter-spacing: .2px; }
p, li, span, div { color: var(--muted); }
a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }

.nm-card {
  background: var(--card);
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: 18px;
  padding: 18px;
  box-shadow: 0 10px 25px rgba(0,0,0,0.25);
  transition: transform 120ms ease, box-shadow 120ms ease, border-color 120ms ease;
}
.nm-card:hover {
  transform: translateY(-2px);
  border-color: rgba(0,209,178,.35);
  box-shadow: 0 14px 34px rgba(0,0,0,0.35);
}

.nm-pill {
  display: inline-block;
  padding: 6px 12px;
  border-radius: 999px;
  background: rgba(0,209,178,0.12);
  color: #b9fff0;
  border: 1px solid rgba(0,209,178,0.28);
  margin-right: 8px;
  margin-bottom: 8px;
  font-size: 12px;
}
.hr-soft {
  border: 0;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.18), transparent);
  margin: 16px 0;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Helper Functions
# --------------------------------------------------
def pill_row(pills):
    st.markdown("<div>" + "".join([f"<span class='nm-pill'>{p}</span>" for p in pills]) + "</div>", unsafe_allow_html=True)

def dl_button(label, path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            data = f.read()
        st.download_button(
            label=label,
            data=data,
            file_name=os.path.basename(path),
            mime="application/pdf",
            key=f"download_{os.path.basename(path)}_{hash(label)}"
        )

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
with st.sidebar:
    st.markdown("## 🌟 Nimish Mathur")
    st.caption("🤖 Data Science and AI Enthusiast")
    st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/nimish-mathur050302) · [💻 GitHub](https://github.com/nimish0503)")
    st.divider()
    st.markdown("**📄 Download Resume**")
    dl_button("Resume", "assets/NimishMathur_Resume.pdf")
    st.divider()
    section = st.selectbox(
    "📍 Navigate to a section:",
    ["🏠 Introduction", "💼 Work Experience", "🧠 Technical Skills", "💼 Featured Projects", "🎓 Education", "🏅 Certifications & Awards", "📬 Contact"],
    index=0
)

# --------------------------------------------------
# Introduction
# --------------------------------------------------
def render_intro():
    st.markdown("""
    <div class='nm-card' style='padding:32px;'>
      <h1>👋 Hey, I'm <span style='color:#00d1b2;'>Nimish Mathur</span></h1>
      <p>🚀 I’m a Data Science & AI enthusiast pursuing my <b>M.Sc. in Applied Data Science & Analytics</b> at SRH University Heidelberg (Germany). 
      I love building scalable data systems, automating analytics, and developing intelligent models that turn data into impact.</p>
    """, unsafe_allow_html=True)
    pill_row(["💻 Data Engineering", "🤖 Machine Learning", "📊 Data Visualization", "☁️ Cloud Computing", "🧭 AI Engineering"])
    st.markdown("<hr class='hr-soft'/>", unsafe_allow_html=True)
    st.markdown("""
    ### 💬 Quick Intro
    - 📍 Based in Mannheim, Germany  
    - 💡 Passionate about AI Agent Frameworks, Environmental Analytics & Process Mining  
    - ⚙️ Skilled in Python, SQL, Airflow, GCP, LangChain, Neo4j  
    - 🧠 Exploring the balance between AI Ethics and Technical Design
    """, unsafe_allow_html=True)
    st.markdown("""
    <p style='text-align:center; color:#9aa4ad; margin-top:30px;'>✨ "Let's connect, create, and push the boundaries of Data & AI together." ✨</p>
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# Work Experience
# --------------------------------------------------
def render_experience():
    st.header("💼 Work Experience")
    st.markdown("""
    <div class='nm-card'>
      <h3>🏢 CRISIL Limited — Database Administrator Intern</h3>
      <p>📍 Mumbai, India | Dec 2023 – Jun 2024</p>
      <ul>
        <li>Automated KPI and compliance reports using Python (Pandas, SQLAlchemy), improving efficiency by <b>40%</b>.</li>
        <li>Designed and optimized ETL pipelines for audit and performance data using <b>Airflow</b> and <b>PostgreSQL</b>.</li>
        <li>Created <b>Power BI dashboards</b> and data validation scripts for high-stakes business reporting.</li>
        <li>Authored structured technical documentation, improving reproducibility and QA reliability.</li>
      </ul>
    </div>
    """, unsafe_allow_html=True)
    pill_row(["Python", "Pandas", "SQLAlchemy", "Airflow", "PostgreSQL", "Power BI"])

# --------------------------------------------------
# Projects (All 10)
# --------------------------------------------------
def render_projects():
    st.header("💼 Featured Projects")

    # Row 1
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='nm-card'>
        <h3>🌊 Pacific Progress Pulse — Climate & Resilience Dashboard</h3>
        <p><b>Goal:</b> Track climate, disaster resilience, and sustainability indicators across Pacific Island nations.</p>
        <p><b>What I Did:</b> Designed a Tableau dashboard with KPI cards, bubble maps, and trend charts after preparing multi-source data in Tableau Prep.</p>
        <p><b>Result:</b> Enabled visualization of 100+ KPIs and supported policy-level climate insights.</p>
        </div>
        """, unsafe_allow_html=True)
        pill_row(["Tableau", "Excel", "Data Visualization", "Climate Analytics"])

        st.markdown("""
        <div class='nm-card'>
        <h3>🧠 AI-Driven Agents for Algae Management</h3>
        <p><b>Goal:</b> Predict harmful algal blooms using AI and satellite data.</p>
        <p><b>What I Did:</b> Built a multi-agent framework (HOMOGEN, CALIBRO, VISIOS, PREDIKT) integrating Sentinel-2 and ERA5 data with Transformer-based data fusion.</p>
        <p><b>Result:</b> Improved data processing efficiency by 80% and achieved 94% model accuracy.</p>
        </div>
        """, unsafe_allow_html=True)
        pill_row(["Python", "Transformers", "CNN", "REST API", "Satellite Data"])

        st.markdown("""
        <div class='nm-card'>
        <h3>🧩 Data Integration Pipeline for Knowledge Graphs</h3>
        <p><b>Goal:</b> Automate semantic data ingestion and validation.</p>
        <p><b>What I Did:</b> Built ETL pipeline with Python, Airflow, and Neo4j; schema alignment via RDF/SPARQL with monitoring and validation.</p>
        <p><b>Result:</b> Delivered robust ETL ensuring high data integrity for semantic AI systems.</p>
        </div>
        """, unsafe_allow_html=True)
        pill_row(["Airflow", "Neo4j", "RDF", "SPARQL", "ETL"])

        st.markdown("""
        <div class='nm-card'>
        <h3>💬 TruHealth — Mental Health Analytics</h3>
        <p><b>Goal:</b> Analyze online discussions to understand mental-health sentiment.</p>
        <p><b>What I Did:</b> Built NLP pipeline (TF-IDF, Logistic Regression, Naive Bayes) and integrated Flask + Power BI dashboard.</p>
        <p><b>Result:</b> Achieved 85% accuracy and clear sentiment patterns supporting awareness campaigns.</p>
        </div>
        """, unsafe_allow_html=True)
        pill_row(["NLP", "Flask", "Power BI", "TF-IDF", "Sentiment Analysis"])

        st.markdown("""
        <div class='nm-card'>
        <h3>🕵️‍♂️ Hush-Hush Recruiter</h3>
        <p><b>Goal:</b> Automate candidate screening using public GitHub activity and coding data.</p>
        <p><b>What I Did:</b> Built an ML-powered ATS with Streamlit dashboard, SQL database, and automated GitHub scraping and scoring pipeline.</p>
        <p><b>Result:</b> Reduced manual screening effort by 98% and streamlined recruitment workflows.</p>
        </div>
        """, unsafe_allow_html=True)
        pill_row(["Python", "Streamlit", "SQL", "ML Scoring Model", "Automation"])

    with col2:
        st.markdown("""
        <div class='nm-card'>
        <h3>🧬 LungDetect — Pneumonia Detection</h3>
        <p><b>Goal:</b> Detect pneumonia from chest X-rays and provide explainability.</p>
        <p><b>What I Did:</b> DenseNet121 CNN on 6k+ images, Grad-CAM visualization, SQL preprocessing, clinical validation.</p>
        <p><b>Result:</b> Achieved 95% accuracy and interpretable visual outputs for clinicians.</p>
        </div>
        """, unsafe_allow_html=True)
        pill_row(["PyTorch", "DenseNet121", "Grad-CAM", "SQL", "Explainable AI"])

        st.markdown("""
        <div class='nm-card'>
        <h3>🔗 Graph-Based Knowledge Representation</h3>
        <p><b>Goal:</b> Create semantic knowledge graphs for structured retrieval and explainable AI.</p>
        <p><b>What I Did:</b> Built Neo4j schemas and GNN prototypes using PyTorch Geometric; integrated RAG for contextual queries.</p>
        <p><b>Result:</b> Improved retrieval by 20% and enhanced interpretability in graph reasoning tasks.</p>
        </div>
        """, unsafe_allow_html=True)
        pill_row(["Neo4j", "GNN", "PyTorch Geometric", "LangChain"])

        st.markdown("""
        <div class='nm-card'>
        <h3>🧠 Reimagined Goggles — Ethics, Privacy & Law in AI</h3>
        <p><b>Goal:</b> Explore how AI can be designed responsibly under EU AI Act & GDPR.</p>
        <p><b>What I Did:</b> Conducted regulatory research, analyzed AI risk tiers, fairness, and governance frameworks.</p>
        <p><b>Result:</b> Produced an ethics guide bridging technical and policy perspectives.</p>
        </div>
        """, unsafe_allow_html=True)
        pill_row(["AI Ethics", "GDPR", "EU AI Act", "Research"])

        st.markdown("""
        <div class='nm-card'>
        <h3>📉 Customer Churn Analysis — Telecom</h3>
        <p><b>Goal:</b> Predict customer churn and identify key retention drivers.</p>
        <p><b>What I Did:</b> EDA + feature engineering; trained Logistic Regression, Random Forest, and XGBoost; deployed via Flask.</p>
        <p><b>Result:</b> Achieved ~85% accuracy and actionable business insights.</p>
        </div>
        """, unsafe_allow_html=True)
        pill_row(["Python", "Flask", "XGBoost", "EDA", "ML"])

        st.markdown("""
        <div class='nm-card'>
        <h3>🎬 Netflix Recommendation System</h3>
        <p><b>Goal:</b> Build a content-based recommender using Netflix metadata.</p>
        <p><b>What I Did:</b> Cleaned data, created content + hybrid recommenders, visualized genre trends with Seaborn.</p>
        <p><b>Result:</b> Functional recommender providing personalized suggestions and catalog insights.</p>
        </div>
        """, unsafe_allow_html=True)
        pill_row(["pandas", "scikit-learn", "Seaborn", "Recommender Systems"])
        
# --------------------------------------------------
# Technical Skills Section (Final Polished Version)
# --------------------------------------------------
def render_skills():
    st.header("🧠 Technical Skills")

    # Programming & Scripting
    st.markdown("""
    <div class='nm-card'>
      <h3>💻 Programming & Scripting</h3>
    </div>
    """, unsafe_allow_html=True)
    pill_row(["Python", "SQL", "R", "Bash", "JavaScript (basic)"])

    # Data Engineering & Pipelines
    st.markdown("""
    <div class='nm-card'>
      <h3>⚙️ Data Engineering & Pipelines</h3>
    </div>
    """, unsafe_allow_html=True)
    pill_row(["Apache Airflow", "Kafka", "dbt", "ETL Pipelines", "Apache Spark", "Dataflow", "Terraform", "Event-Driven Design"])

    # Cloud & DevOps
    st.markdown("""
    <div class='nm-card'>
      <h3>☁️ Cloud & DevOps</h3>
    </div>
    """, unsafe_allow_html=True)
    pill_row(["GCP", "Azure", "AWS (S3, EC2)", "BigQuery", "Pub/Sub", "Docker", "Kubernetes", "GitHub Actions", "CI/CD", "Linux Server Management"])

    # Machine & Deep Learning
    st.markdown("""
    <div class='nm-card'>
      <h3>🤖 Machine & Deep Learning</h3>
    </div>
    """, unsafe_allow_html=True)
    pill_row(["Scikit-learn", "TensorFlow", "PyTorch", "XGBoost", "LightGBM", "LSTM / RNNs", "Transformers", "CNN", "Grad-CAM", "SHAP", "LIME"])

    # NLP & LLM Ecosystem
    st.markdown("""
    <div class='nm-card'>
      <h3>🧠 NLP & LLM Ecosystem</h3>
    </div>
    """, unsafe_allow_html=True)
    pill_row(["Hugging Face", "Embeddings", "Sentence Transformers", "Text Summarization", "LLM Fine-Tuning", "LangSmith", "Prompt Templates"])

    # Agentic & Generative AI
    st.markdown("""
    <div class='nm-card'>
      <h3>🧩 Agentic & Generative AI</h3>
    </div>
    """, unsafe_allow_html=True)
    pill_row(["LangChain", "OpenAI API", "LlamaIndex", "CrewAI", "Multi-Agent Systems", "Event Bus", "RAG", "FAISS", "Chroma", "Prompt Engineering"])

    # Databases & Storage
    st.markdown("""
    <div class='nm-card'>
      <h3>🧩 Databases & Storage</h3>
    </div>
    """, unsafe_allow_html=True)
    pill_row(["PostgreSQL", "MySQL", "MongoDB", "BigQuery", "SQLite", "ElasticSearch", "Snowflake", "Cloud Buckets"])

    # Visualization & BI
    st.markdown("""
    <div class='nm-card'>
      <h3>📊 Visualization & BI</h3>
    </div>
    """, unsafe_allow_html=True)
    pill_row(["Power BI", "Tableau", "Streamlit", "Looker Studio", "Matplotlib", "Seaborn", "Plotly", "Altair"])

    # Tools, Collaboration & Analytics
    st.markdown("""
    <div class='nm-card'>
      <h3>🧰 Tools, Collaboration & Analytics</h3>
    </div>
    """, unsafe_allow_html=True)
    pill_row(["Excel VBA", "Git", "GitHub", "Jira", "Confluence", "Notion", "Miro", "Slack Automation", "Postman"])

# --------------------------------------------------
# Education (Enhanced with Skills Learned)
# --------------------------------------------------
def render_education():
    st.header("🎓 Education")

    # SRH Hochschule Heidelberg
    st.markdown("""
    <div class='nm-card'>
      <h3>🇩🇪 SRH Hochschule Heidelberg</h3>
      <p><b>M.Sc. Applied Data Science & Analytics (2024–2026)</b></p>
      <p>Focused on Machine Learning, Cloud Data Engineering, and Agentic AI frameworks. 
      Built research projects on multi-agent systems, data harmonization, and AI governance.</p>
    </div>
    """, unsafe_allow_html=True)
    pill_row(["Python (Advanced)", "Airflow", "LangChain", "Neo4j", "GCP", "AI Ethics", "Agentic AI"])

    # Symbiosis Institute of Technology
    st.markdown("""
    <div class='nm-card'>
      <h3>🇮🇳 Symbiosis Institute of Technology</h3>
      <p><b>B.Tech Information Technology (2020–2024)</b></p>
      <p>Developed strong foundations in programming, data structures, and database systems.
      Led the final-year project <b>LungDetect</b>, achieving 95% accuracy in pneumonia detection.</p>
    </div>
    """, unsafe_allow_html=True)
    pill_row(["Python", "SQL", "Flask", "Power BI", "TensorFlow", "Computer Vision", "Team Leadership"])

   # FH St. Pölten — Erasmus+ BIP
    st.markdown("""
    <div class='nm-card'>
      <h3>🇦🇹 FH St. Pölten — Erasmus+ BIP</h3>
      <p><b>Blended Intensive Programme — Trends in Research and Innovation in the Context of Computer Science (2025)</b></p>
      <p>Explored the theme <b>“The Future of Coding”</b> through hands-on reinforcement learning for autonomous driving 
      using <b>AWS DeepRacer</b> and cloud-based simulation environments.</p>
      <p>Worked collaboratively with international teams on AI innovation and ethical frameworks for intelligent systems.</p>
    </div>
    """, unsafe_allow_html=True)
    pill_row(["Reinforcement Learning", "AWS DeepRacer", "AWS Cloud", "AI Ethics", "Autonomous Systems", "Collaborative Research"])

# --------------------------------------------------
# Certifications & Awards (Fixed and Polished)
# --------------------------------------------------
def render_certs_awards():
    st.header("🏅 Certifications & Awards")

    # Certifications
    st.markdown("""
    <div class='nm-card'>
      <h4>🎓 Certifications</h4>
      <ul style='line-height:1.6;'>
        <li><b>IBM Data Science Professional Certificate (Coursera)</b> — Completed a full data science workflow including data analysis, visualization, and predictive modeling using Python (Pandas, Matplotlib, scikit-learn). Built a capstone project predicting housing prices.</li>
        <li><b>Machine Learning with Python (Coursera)</b> — Implemented regression, classification, and clustering models using scikit-learn. Learned model evaluation, tuning, and pipeline automation.</li>
        <li><b>Building ETL Pipelines with Apache Airflow (Udemy)</b> — Created DAGs, custom operators, and scheduled ETL workflows in Airflow for real-time analytics automation.</li>        
        <li><b>Generative AI Masterclass (Udemy)</b> — Explored text and image generation using OpenAI APIs, Hugging Face, and LangChain. Developed prompt-based chatbots and summarization tools.</li>       
        <li><b>Prompt Engineering (Udemy)</b> — Learned advanced prompt techniques for reasoning, structured outputs, and API-integrated LLM workflows.</li>
        <li><b>Power BI Desktop – Dashboards & Data Analytics (Udemy)</b> — Created Power BI dashboards with DAX measures, Power Query transformations, and automated KPI tracking.</li>
        <li><b>SAP Analytics Cloud (SAP Learning)</b> — Designed interactive reports and dashboards integrating SAP datasets with live modeling and visualization features.</li>        
        <li><b>Google Data Analytics Professional Certificate (Udemy)</b> — Applied SQL and visualization techniques to analyze public datasets. Created business dashboards for trend insights.</li>
      </ul>
    </div>
    """, unsafe_allow_html=True)

    pill_row(["Python", "TensorFlow", "scikit-learn", "Airflow", "dbt", "BigQuery", "Vertex AI", "LangChain", "AWS", "Power BI", "Tableau", "SAP SAC"])

    # Awards
    st.markdown("""
    <div class='nm-card'>
      <h4>🏆 Awards</h4>
      <ul style='line-height:1.6;'>
        <li><b>CRISIL Bright Spark Award</b> — Recognized for outstanding contribution during internship by automating compliance reports and ETL workflows.</li>
        <li><b>BioDatathon 2025 (SRH Heidelberg & BioMedX)</b> — Participated in an interdisciplinary biomedical data hackathon integrating ML models with health datasets.</li>
        <li><b>Erasmus+ BIP – Excellence Grade (1)</b> — Achieved top distinction for reinforcement learning project using AWS DeepRacer at FH St. Pölten.</li>
      </ul>
    </div>
    """, unsafe_allow_html=True)


# --------------------------------------------------
# Contact
# --------------------------------------------------
def render_contact():
    st.header("📬 Contact")
    st.markdown("""
    <div class='nm-card'>
      <p>📢 Open to roles and collaborations in Data Engineering, Machine Learning, and Analytics.</p>
      <ul>
        <li>🔗 LinkedIn: <a href="https://www.linkedin.com/in/nimish-mathur050302" target="_blank">linkedin.com/in/nimish-mathur050302</a></li>
        <li>💻 GitHub: <a href="https://github.com/nimish0503" target="_blank">github.com/nimish0503</a></li>
        <li>📧 Email: nimish050302@gmail.com</li>
      </ul>
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# Router
# --------------------------------------------------
if "Introduction" in section:
    render_intro()
elif "Work Experience" in section:
    render_experience()
elif "Featured Projects" in section:
    render_projects()
elif "Education" in section:
    render_education()
elif "Certifications" in section:
    render_certs_awards()
elif "Contact" in section:
    render_contact()
elif "Technical Skills" in section:
    render_skills()

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("<p style='text-align:center;color:#6d7781;margin-top:24px;'>Built with ❤️ using Streamlit</p>", unsafe_allow_html=True)
