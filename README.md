# GetExcused 🐾  
**Because even machines need a day off!**  

*A humorous API that generates creative excuses using AI - perfect for those "I need an excuse" emergencies!*  

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/)
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-%23FFD21E.svg?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/)

![image](https://github.com/user-attachments/assets/d1619bc7-7105-4cbc-be55-3898c01a12a4)

## 🚀 Features  
- 🤖 AI-powered excuse generation using HuggingFace models  
- 🎲 Random excuse mode for surprise results  
- 🎇 Excuses rank list
- 🐳 Dockerized microservices architecture  
- ☁️ AWS deployment ready  
- 📦 Clean MVP architecture pattern  

## ⚙️ Installation & Usage  

### Prerequisites  
- Python 3.9+  
- Docker  
- [HuggingFace API token](https://huggingface.co/settings/tokens)  

```bash
# Clone repository
git clone https://github.com/HighFaev/GetExcused.git
cd GetExcused

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Add your HuggingFace API token to .env as HUGGINGFACE_API_KEY
