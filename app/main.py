from fastapi import FastAPI, UploadFile, File, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles  # Импортируем для работы с файлами
from app.services.text_processing import process_text
import uvicorn
from fastapi.responses import RedirectResponse

app = FastAPI()

# Настройка для отдачи статических файлов
app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def root():
    return RedirectResponse(url="/upload")

@app.get("/upload", response_class=HTMLResponse)
async def upload_form(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})

@app.post("/upload", response_class=HTMLResponse)
async def upload_file(request: Request, file: UploadFile = File(...)):
    content = await file.read()
    words_stats = process_text(content.decode('utf-8'))
    words_stats = sorted(words_stats, key=lambda x: -x.idf)[:50]
    return templates.TemplateResponse("result.html", {"request": request, "words": words_stats})

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
