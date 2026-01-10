# 🏗️ Project Ouroboros: Cognitive Architecture Blueprint
**Status:** 🟡 Phase 0: Foundations & DNA | **Version:** 1.0 (Genesis)

## 📖 System Concept (הקונספט)
המערכת אינה "בוט כתיבה" רגיל. זוהי **מכונת מצבים הסתברותית (Probabilistic State Machine)** המנוהלת על ידי שערים (Gates).
המטרה: לייצר "לולאת אורובורוס" (Ouroboros Loop) – המערכת לומדת מתיקוני המשתמש ומעדכנת את ה-DNA של עצמה בזמן אמת, כך שכל פוסט מדויק יותר מקודמו.

---

## 🛠️ Tech Stack (הטכנולוגיה)
* **Brain:** Claude 4.5 Sonnet (Logic & Reasoning)
* **Orchestration:** LangGraph (State Management)
* **Memory:** Vector Store (Pinecone/Chroma) + `client_dna.md`
* **UI:** Streamlit (For Pilot/Engineering View)
* **Language:** Python 3.11+

---

## 🗺️ Master Roadmap (תוכנית עבודה)

### 🌑 Phase 0: DNA & Feasibility (היתכנות וכיול)
*המטרה: לוודא שיש לנו את "הקול" של הלקוח לפני שכותבים קוד מורכב.*

- [x] **Repository Setup:** הקמת תיקיות, גיט, וקובץ `.gitignore`.
- [x] **Data Collection:** איסוף 20 פוסטים "פוסטים מוזהבים" של הלקוח.
- [x] **DNA Extraction:** הרצת אנליזה על הפוסטים ויצירת קובץ `client_dna.md`.
- [ ] **The Prime Prompt:** יצירת `master_sop.md` (הוראות מערכת) המשלב את ה-DNA.
- [ ] **Manual Simulation:** הרצה ידנית (בצ'אט) של הפרומפט כדי לוודא שהתוצאה נשמעת כמו הלקוח.
- [ ] **GATE 1 APPROVAL:** הלקוח מאשר שהטקסט נשמע כמוהו (Vibe Check).

### 🌒 Phase 1: The Engine (המנוע הבסיסי)
*המטרה: סקריפט פייתון אחד שרץ מקצה לקצה ומייצר טיוטה.*

- [ ] **Environment Setup:** התקנת `poetry`/`venv` וספריות (`anthropic`, `python-dotenv`).
- [ ] **API Connection:** חיבור ראשוני ל-Claude API (בדיקת Hello World).
- [ ] **Knowledge Loader:** סקריפט שטוען את `client_dna.md` לתוך הזיכרון.
- [ ] **Linear Script:** בניית שרשרת פשוטה: `Input` -> `Prompt` -> `Output`.
- [ ] **Output Logging:** שמירת התוצרים לקבצי Markdown מקומיים לבדיקה.

### 🌓 Phase 2: The Agents (הסוכנים והגרף)
*המטרה: פיצול המערכת למומחים שונים (תחקירן, כותב, מבקר).*

- [ ] **Agent 1 - The Hunter:** סוכן שמבצע חיפוש (Tavily) ומביא עובדות.
- [ ] **Agent 2 - The Architect:** סוכן שבונה ראשי פרקים (Outline) לפני הכתיבה.
- [ ] **Agent 3 - The Writer:** סוכן שכותב את הטקסט המלא על בסיס ה-Outline וה-DNA.
- [ ] **LangGraph Setup:** חיבור הסוכנים לגרף ניהול מצבים.
- [ ] **GATE 2 APPROVAL:** המערכת מייצרת פוסט מלא עשיר בעובדות באופן אוטונומי.

### 🌕 Phase 3: The Ouroboros Loop (הלולאה הלומדת)
*המטרה: המערכת לומדת מתיקונים.*

- [ ] **Review Interface:** ממשק פשוט (Streamlit) שמאפשר לאדם לערוך את הטיוטה.
- [ ] **The Diff Engine:** מנגנון שמשווה בין *הטיוטה* לבין *הגרסה הסופית* שאושרה.
- [ ] **Insight Extractor:** סוכן שמנתח את ההבדלים ומנסח חוק חדש ("הלקוח מחק את המילה X, לא להשתמש בה יותר").
- [ ] **DNA Mutation:** עדכון אוטומטי של `client_dna.md` עם החוק החדש.
- [ ] **Final Deployment:** העלאת המערכת לשרת ענן לשימוש שוטף.

---

## 📂 Project Structure
```text
/project-ouroboros
│
├── .env                 # API Keys (NEVER COMMIT THIS)
├── README.md            # This file
├── requirements.txt     # Python dependencies
│
├── 00_knowledge_base    # The Brain
│   ├── raw_data/        # Original client posts
│   ├── client_dna.md    # Extracted style guide [CREATED]
│   └── master_sop.md    # System Instructions
│
├── src                  # The Code
│   ├── main.py          # Entry point
│   └── agents/          # Agent definitions
│
└── logs                 # Output generation
