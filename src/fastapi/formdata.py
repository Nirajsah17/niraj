from fastapi import FastAPI, UploadFile, File


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
  
@app.post("/uploadfile")
async def file_upload(file: UploadFile = File(...)):
  return {"filename": file.filename}