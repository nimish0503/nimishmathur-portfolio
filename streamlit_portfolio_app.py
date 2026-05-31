# Nimish Mathur — Streamlit Portfolio (Updated with Full Info)

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
      <p>🚀 I'm a Data Science & AI enthusiast pursuing my <b>M.Sc. in Applied Data Science & Analytics</b> at SRH University Heidelberg (Germany). 
      I love building scalable data systems, automating analytics, and developing intelligent models that turn data into impact.
      Currently writing my thesis at <b>Omnisent Sports</b>, building a data-driven sports investment intelligence framework integrating 
      athlete performance, social capital, and commercial valuation using agentic AI and RAG workflows.</p>
    """, unsafe_allow_html=True)
    pill_row(["💻 Data Engineering", "🤖 Machine Learning", "📊 Data Visualization", "☁️ Cloud Computing", "🧭 AI Engineering"])
    st.markdown("<hr class='hr-soft'/>", unsafe_allow_html=True)
    st.markdown("""
    ### 💬 Quick Intro
    - 📍 Based in Mannheim, Germany  
    - 💡 Passionate about AI Agent Frameworks, Environmental Analytics & Process Mining  
    - ⚙️ Skilled in Python, SQL, Airflow, GCP, LangChain, Neo4j  
    - 🧠 Exploring the balance between AI Ethics and Technical Design
    - 🏅 NVIDIA Certified in Deep Learning & Prompt Engineering
    - 🌍 German A2 | English C1
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

    # Omnisent — Thesis
    st.markdown("""
    <div class='nm-card'>
      <h3>🏟️ Omnisent Sports — Thesis Student</h3>
      <p>📍 Heidelberg, Germany | Mar 2026 – Sep 2026</p>
      <ul>
        <li>Developing a data-driven <b>sports investment intelligence framework</b> integrating athlete performance data, social capital indicators, and commercial valuation to reduce fragmentation across scouting, sponsorship, and investment decision-making.</li>
        <li>Designing an exploratory <b>Social Performance Index (SPI)</b> to quantify athlete social and commercial value alongside on-field metrics, enabling holistic athlete valuation across sports, leagues, and competition tiers.</li>
        <li>Proposing an AI-assisted analytics pipeline covering data ingestion, athlete scoring, normalization, and matching support using concepts from <b>agentic AI, retrieval-augmented workflows</b>, and automated sports analytics.</li>
        <li>Exploring algorithmic matching frameworks using <b>multi-criteria decision analysis</b> and stable matching theory for club-player, brand-athlete, and investor-club recommendations with explainable decision outputs.</li>
      </ul>
    </div>
    """, unsafe_allow_html=True)
    pill_row(["Python", "Agentic AI", "RAG", "LangChain", "Multi-Criteria Decision Analysis", "Stable Matching", "NLP", "PostgreSQL"])

    st.markdown("<br/>", unsafe_allow_html=True)

    # Omnisent — Data Science Intern
    st.markdown("""
    <div class='nm-card'>
      <h3>🏟️ Omnisent Sports — Data Science Intern</h3>
      <p>📍 Germany (Remote) | Nov 2025 – Mar 2026</p>
      <ul>
        <li>Built AI-powered <b>sentiment analysis pipelines</b> using pretrained NLP models (HuggingFace, RoBERTa) for sports media and social data.</li>
        <li>Developed end-to-end <b>data pipelines</b> using Python, SQL, and PostgreSQL for analytics-ready datasets.</li>
        <li>Designed and contributed to <b>Streamlit dashboards</b> for internal analytics and reporting.</li>
        <li>Collaborated with product and engineering teams to improve data quality, schema design, and business alignment.</li>
      </ul>
    </div>
    """, unsafe_allow_html=True)
    pill_row(["Python", "HuggingFace", "RoBERTa", "SQL", "PostgreSQL", "Streamlit", "NLP"])

    st.markdown("<br/>", unsafe_allow_html=True)

    # CRISIL
    st.markdown("""
    <div class='nm-card'>
      <h3>🏢 CRISIL Limited — Database Administrator Intern</h3>
      <p>📍 Mumbai, India | Dec 2023 – Jun 2024</p>
      <ul>
        <li>Automated KPI and compliance reports using Python (Pandas, SQLAlchemy), improving efficiency by <b>40%</b>.</li>
        <li>Designed and optimized ETL pipelines for audit and performance data using <b>Airflow</b> and <b>PostgreSQL</b>, improving performance by <b>30%</b>.</li>
        <li>Created <b>Power BI dashboards</b> and data validation scripts for high-stakes business reporting.</li>
        <li>Supported database migration projects with <b>zero downtime</b> and strong QA alignment.</li>
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
        <h3>🧠 AI-Driven Multi-Agent System for Algae Management (HAB)</h3>
        <p><b>Goal:</b> Predict and manage Harmful Algal Blooms (HABs) in German surface waters using AI and satellite data.</p>
        <p><b>What I Did:</b> Designed and deployed a multi-agent framework with four intelligent agents — 
        <b>HOMOGEN</b> (data harmonization), <b>CALIBRO</b> (satellite calibration), <b>PREDIKT</b> (bloom forecasting), 
        and <b>VISIOS</b> (deep learning-based image validation). Integrated <b>Sentinel-2, Landsat-9, MODIS</b>, and 
        in-situ sensor data within a harmonized <b>SWIM (Surface Water Information Management)</b> framework. 
        Built a modular, scalable agentic architecture enabling independent deployment, inter-agent communication, 
        and fault-tolerant data pipelines.</p>
        <p><b>Result:</b> Improved data processing efficiency by 80%, achieved <b>87–94% model accuracy</b>, and 
        delivered research insights for climate resilience and AI-driven environmental policy support.</p>
        </div>
        """, unsafe_allow_html=True)
        pill_row(["Python", "TensorFlow", "Transformers", "CNN", "LangChain", "REST API", "Sentinel-2", "Landsat-9", "MODIS", "Satellite Data", "Multi-Agent AI"])

        st.markdown("""
        <div class='nm-card'>
        <h3>🧩 Data Integration Pipeline for Knowledge Graphs</h3>
        <p><b>Goal:</b> Automate semantic data ingestion and validation.</p>
        <p><b>What I Did:</b> Built ETL pipeline with Python, Airflow, and Neo4j; schema alignment via RDF/SPARQL with monitoring and validation. Built GNN prototypes (PyTorch Geometric) and integrated RDF/Neo4j into RAG pipelines.</p>
        <p><b>Result:</b> Delivered robust ETL ensuring high data integrity for semantic AI systems. Improved retrieval by 20% and enhanced interpretability in graph reasoning tasks.</p>
        </div>
        """, unsafe_allow_html=True)
        pill_row(["Airflow", "Neo4j", "RDF", "SPARQL", "ETL", "PyTorch Geometric", "GNN", "RAG"])

        st.markdown("""
        <div class='nm-card'>
        <h3>💬 TruHealth — Mental Health Analytics</h3>
        <p><b>Goal:</b> Analyze online discussions to understand mental-health sentiment.</p>
        <p><b>What I Did:</b> Built NLP pipeline (TF-IDF, Logistic Regression, Naive Bayes) and integrated Flask + Power BI dashboard with MongoDB backend.</p>
        <p><b>Result:</b> Achieved 85% accuracy and clear sentiment patterns supporting awareness campaigns.</p>
        </div>
        """, unsafe_allow_html=True)
        pill_row(["NLP", "Flask", "Power BI", "TF-IDF", "MongoDB", "Sentiment Analysis"])

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
    pill_row(["Python", "SQL", "R", "Bash", "JavaScript", "TypeScript"])

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
    pill_row(["GCP", "Azure", "AWS (S3, EC2, Lambda)", "BigQuery", "Pub/Sub", "Docker", "Kubernetes", "GitHub Actions", "CI/CD", "Linux Server Management"])

    # Machine & Deep Learning
    st.markdown("""
    <div class='nm-card'>
      <h3>🤖 Machine & Deep Learning</h3>
    </div>
    """, unsafe_allow_html=True)
    pill_row(["Scikit-learn", "TensorFlow", "PyTorch", "PyTorch Geometric", "XGBoost", "LightGBM", "LSTM / RNNs", "Transformers", "CNN", "GNN", "Grad-CAM", "SHAP", "LIME"])

    # NLP & LLM Ecosystem
    st.markdown("""
    <div class='nm-card'>
      <h3>🧠 NLP & LLM Ecosystem</h3>
    </div>
    """, unsafe_allow_html=True)
    pill_row(["Hugging Face", "RoBERTa", "Sentence Transformers", "Embeddings", "Text Summarization", "LLM Fine-Tuning", "LangSmith", "Prompt Templates", "Prompt Engineering"])

    # Agentic & Generative AI
    st.markdown("""
    <div class='nm-card'>
      <h3>🧩 Agentic & Generative AI</h3>
    </div>
    """, unsafe_allow_html=True)
    pill_row(["LangChain", "LangGraph", "OpenAI API", "LlamaIndex", "CrewAI", "Multi-Agent Systems", "Event Bus", "RAG", "FAISS", "Chroma", "Prompt Engineering"])

    # Databases & Storage
    st.markdown("""
    <div class='nm-card'>
      <h3>🗄️ Databases & Storage</h3>
    </div>
    """, unsafe_allow_html=True)
    pill_row(["PostgreSQL", "MySQL", "MongoDB", "Neo4j", "BigQuery", "SQLite", "ElasticSearch", "Snowflake", "Cloud Buckets"])

    # Visualization & BI
    st.markdown("""
    <div class='nm-card'>
      <h3>📊 Visualization & BI</h3>
    </div>
    """, unsafe_allow_html=True)
    pill_row(["Power BI", "Tableau", "SAP Analytics Cloud", "Streamlit", "Looker Studio", "Matplotlib", "Seaborn", "Plotly", "Altair"])

    # Tools, Collaboration & Analytics
    st.markdown("""
    <div class='nm-card'>
      <h3>🧰 Tools, Collaboration & Analytics</h3>
    </div>
    """, unsafe_allow_html=True)
    pill_row(["Excel (Power Query, PivotTables)", "Excel VBA", "Git", "GitHub", "Jira", "Confluence", "Notion", "Miro", "Slack Automation", "Postman", "Playwright", "Cypress", "Jest"])

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
      <p><b>Blended Intensive Programme — Trends in Research and Innovation in the Context of Computer Science (May–Jun 2025)</b></p>
      <p>Explored the theme <b>"The Future of Coding"</b> through hands-on reinforcement learning for autonomous driving 
      using <b>AWS DeepRacer</b> and cloud-based simulation environments.</p>
      <p>Worked collaboratively with international teams on AI innovation and ethical frameworks for intelligent systems.</p>
    </div>
    """, unsafe_allow_html=True)
    pill_row(["Reinforcement Learning", "AWS DeepRacer", "AWS Cloud", "AI Ethics", "Autonomous Systems", "Collaborative Research"])

# --------------------------------------------------
# Certifications & Awards (Updated with Verified Certificates)
# --------------------------------------------------
def render_certs_awards():
    st.header("🏅 Certifications & Awards")

    # Certifications
    st.markdown("""
    <div class='nm-card'>
      <h4>🎓 Certifications</h4>
      <ul style='line-height:1.9;'>

        <li><b>Building LLM Applications With Prompt Engineering</b> — NVIDIA <span style='color:#9aa4ad;font-size:12px;'>| Nov 2025</span><br/>
        <span style='font-size:13px;'>Credential ID: g-2IlRd1RO6ZWcYuaAXLtA</span></li>

        <li><b>Fundamentals of Deep Learning</b> — NVIDIA <span style='color:#9aa4ad;font-size:12px;'>| Oct 2025</span><br/>
        <span style='font-size:13px;'>Credential ID: 1tO0Ys3ITkGJkXM3sgBKrQ | Skills: Deep Learning</span></li>

        <li><b>Python for Data Science, AI & Development</b> — IBM / Coursera <span style='color:#9aa4ad;font-size:12px;'>| Jan 2025</span></li>

        <li><b>Introduction to Data Engineering</b> — IBM / Coursera <span style='color:#9aa4ad;font-size:12px;'>| Jan 2025</span></li>

        <li><b>SAS Certified Specialist: Visual Business Analytics Using SAS Viya</b> — SAS <span style='color:#9aa4ad;font-size:12px;'>| Nov 2024 · Expires Nov 2029</span></li>

        <li><b>SAS Visual Analytics 2 for SAS Viya: Advanced</b> — SAS <span style='color:#9aa4ad;font-size:12px;'>| Nov 2024</span></li>

        <li><b>SAS Visual Analytics 1 for SAS Viya: Basics</b> — SAS <span style='color:#9aa4ad;font-size:12px;'>| Nov 2024</span></li>

        <li><b>Intermediate Python for Developers</b> — DataCamp <span style='color:#9aa4ad;font-size:12px;'>| Oct 2024</span><br/>
        <span style='font-size:13px;'>Skills: Programming, Python</span></li>

        <li><b>Data Science Methodology</b> — IBM / Coursera <span style='color:#9aa4ad;font-size:12px;'>| Aug 2024</span></li>

        <li><b>Tools for Data Science</b> — IBM / Coursera <span style='color:#9aa4ad;font-size:12px;'>| Aug 2024</span></li>

        <li><b>What is Data Science?</b> — IBM / Coursera <span style='color:#9aa4ad;font-size:12px;'>| Jul 2024</span></li>

        <li><b>Foundations: Data, Data, Everywhere</b> — Google / Coursera <span style='color:#9aa4ad;font-size:12px;'>| May 2024</span></li>

        <li><b>Google Data Analytics Capstone: Complete a Case Study</b> — Google / Coursera <span style='color:#9aa4ad;font-size:12px;'>| May 2024</span></li>

        <li><b>Programming for Everybody (Getting Started with Python)</b> — University of Michigan / Coursera <span style='color:#9aa4ad;font-size:12px;'>| Mar 2024</span></li>

      </ul>
    </div>
    """, unsafe_allow_html=True)

    pill_row(["NVIDIA", "IBM", "Google", "SAS", "DataCamp", "University of Michigan", "Coursera"])

    st.markdown("<br/>", unsafe_allow_html=True)

    # Udemy Courses
    st.markdown("""
    <div class='nm-card'>
      <h4>📚 Courses & Self-Learning (Udemy)</h4>
      <ul style='line-height:1.9;'>
        <li><b>Agentic AI Full-Stack Masterclass: RAG, MCP & AI Agents</b> — Nikhil Agarwal</li>
        <li><b>Complete Agentic AI Bootcamp With LangGraph and Langchain</b> — KRISHAI Technologies / Krish Naik</li>
        <li><b>Data Analytics Masters 2026: From Basics to Advanced</b> — Dr. Satyajit Pattnaik</li>
        <li><b>AWS Certified Data Engineer Associate 2026 – Hands On!</b> — Sundog Education / Frank Kane</li>
        <li><b>Statistics for Data Science and Business Analysis</b> — 365 Careers</li>
        <li><b>Python Mega Course: Build 20 Real-World Apps and AI Agents</b> — Ardit Sulce (600,000+ Students)</li>
        <li><b>Microsoft Power BI Desktop – Data Analytics with Dashboards</b> — Charlie Walker</li>
        <li><b>Mathematical Foundations of Machine Learning</b> — Dr Jon Krohn / SuperDataScience Team</li>
        <li><b>The Data Science Course: Complete Data Science Bootcamp 2026</b> — 365 Careers</li>
        <li><b>Become a Probability & Statistics Master</b> — Krista King</li>
        <li><b>The Complete Digital Marketing Course – 12 Courses in 1</b> — Rob Percival / Daragh Walsh</li>
        <li><b>German for You A1/A2: A German Language Course for Beginners</b> — Esther Hartwig</li>
        <li><b>Practical GenAI: Basics, Tools, Use Cases, Ethics, Future</b> — Yash Thakker</li>
        <li><b>The Complete Personal Finance Course: Save, Protect, Make More</b> — Chris Haroun</li>
        <li><b>The Complete Full-Stack Web Development Bootcamp</b> — Dr. Angela Yu</li>
        <li><b>Complete Investing Course (Stocks, ETFs, Index/Mutual Funds)</b> — Mohsen Hassan / bloom team</li>
        <li><b>Speak Like a Pro: Public Speaking for Professionals</b> — Jennifer Hennings</li>
        <li><b>MongoDB – The Complete Developer's Guide</b> — Academind / Maximilian Schwarzmüller</li>
        <li><b>FULL STACK JAVA DEV: Java + JSP + Spring + Boot + JS + React</b> — StudyEasy Organization / Chaand Sheikh</li>
      </ul>
    </div>
    """, unsafe_allow_html=True)
    pill_row(["Python", "TensorFlow", "scikit-learn", "Airflow", "LangChain", "LangGraph", "RAG", "AWS", "Power BI", "Tableau", "SAP SAC", "MongoDB", "Full-Stack", "GenAI"])

    st.markdown("<br/>", unsafe_allow_html=True)

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
        <li>📧 Email: nimish.mathur0503@gmail.com</li>
        <li>📱 Phone: +49 15257173184</li>
        <li>📍 Location: Mannheim, Germany</li>
        <li>🌐 Portfolio: <a href="https://nimishportfolio0503.streamlit.app" target="_blank">nimishportfolio0503.streamlit.app</a></li>
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
