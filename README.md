# Shopping Genie - E-commerce Customer Service Chatbot 🛍️🧞‍♂️

An intelligent chatbot that combines deep learning (BERT, LSTM) and Retrieval Augmented Generation (RAG) to provide personalized e-commerce assistance. The project focuses on creating a next-generation chatbot for enhanced customer service in e-commerce applications.

![Architecture](https://github.com/user-attachments/assets/6cb7d426-1959-48a3-97d4-09473a8ad902)
_System Architecture_

## 🌟 Key Features

- **Advanced Intent Recognition**:

  - BERT model with 99.70% accuracy
  - Bi-LSTM model with 98.12% accuracy
  - Context-aware intent classification

- **Smart Product Search**:

  - Vector-based similarity search
  - Personalized product recommendations
  - Advanced filtering capabilities

- **Intelligent Response Generation**:

  - RAG integration with OpenAI GPT-3.5
  - Context-aware response generation
  - Dynamic conversation flow

- **Seamless Human Handover**:
  - Automatic detection of complex queries
  - Smooth transition to human agents
  - Context preservation during handover

## 🏗️ Architecture

The system is built on a hybrid architecture combining multiple components:

1. **Frontend Layer**:

   - Streamlit-based user interface
   - Real-time chat interface
   - Product display and interaction

2. **Processing Layer**:

   - Intent recognition (BERT/Bi-LSTM)
   - Named Entity Recognition
   - Question augmentation
   - Context management

3. **Data Layer**:

   - ChromaDB vector database
   - Product information storage
   - Conversation history management

4. **Integration Layer**:
   - OpenAI GPT-3.5 integration
   - RAG implementation
   - Human agent interface

## 💾 Datasets

The chatbot is trained on a diverse set of data sources:

| Dataset Name            | Records  | Purpose             |
| ----------------------- | -------- | ------------------- |
| Bitext Customer Support | 26,872   | Intent Training     |
| Grocery Chatbot         | 2,480    | Domain Knowledge    |
| Custom Product Data     | 1,800    | Product Information |
| Custom Intent Data      | Variable | Intent Enhancement  |

## 🛠️ Tech Stack

- **Frontend**:

  - Streamlit
  - HTML/CSS
  - JavaScript

- **Backend**:

  - Python 3.8+
  - FastAPI
  - WebSocket

- **Machine Learning**:

  - PyTorch
  - Transformers
  - Sentence-Transformers

- **Storage**:

  - ChromaDB
  - SQLite

- **APIs & Services**:
  - OpenAI GPT-3.5
  - Hugging Face Transformers

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/parthtejani27/Shopping-Genie.git
cd Shopping-Genie
```

2. Create and activate virtual environment:

```bash
python -m venv finalproject
# For Windows
.\finalproject\Scripts\activate
# For Unix/MacOS
source finalproject/bin/activate
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

4. Set up environment variables:

```bash
# Create .env file
touch .env

# Add the following to .env
OPENAI_API_KEY=your_openai_key
DB_HOST=your_db_host
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_DATABASE=your_db_name
```

5. Initialize the database:

```bash
python scripts/init_db.py
```

## 🚀 Usage

1. Start the application:

```bash
streamlit run app.py
```

2. Access the application:
   - Open browser and navigate to `http://localhost:8501`
   - Start interacting with Shopping Genie

![Sample Output](https://github.com/user-attachments/assets/bde47e4f-4220-436b-9cc7-581f2b799e12)
_Shopping Genie in Action_

## 📊 Performance Metrics

| Model/Component            | Metric                | Score  |
| -------------------------- | --------------------- | ------ |
| BERT Intent Classification | Accuracy              | 99.70% |
| Bi-LSTM Model              | Accuracy              | 98.12% |
| Response Generation        | Average Response Time | <2s    |
| User Satisfaction          | Rating                | 4.5/5  |

## 🔮 Future Enhancements

1. **Technical Improvements**:

   - Multi-language support
   - Voice interface integration
   - Enhanced personalization
   - Real-time product updates

2. **User Experience**:
   - Advanced UI/UX features
   - Mobile application
   - Integrated payment system
   - Enhanced visualization
