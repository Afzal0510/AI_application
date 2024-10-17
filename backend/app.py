from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from pdf_handler import process_pdf
from rag_model import RAGModel

app = FastAPI()
rag_model = RAGModel()


@app.post("/upload_pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    content = await process_pdf(file)
    rag_model.add_document(content)
    return {"status": "PDF uploaded successfully"}


@app.post("/ask_question/")
async def ask_question(question: str):
    response = rag_model.get_answer(question)
    return JSONResponse(content={"answer": response})





