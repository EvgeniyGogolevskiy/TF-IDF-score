# TF-IDF Web Application

🚀 Simple web app to upload a text file and see the top 50 words by TF-IDF score.

## Features
- Upload `.txt` files
- Calculate TF and IDF
- Sort by highest IDF
- Beautiful UI with TailwindCSS
- Dockerized for easy run

## How to Run
```bash
git clone https://github.com/EvgeniyGogolevskiy/TF-IDF-score.git
cd test_task_for_Lesta_Games
docker build -t tfidf-app .
docker run -p 8000:8000 tfidf-app