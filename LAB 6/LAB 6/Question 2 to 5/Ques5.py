from fastapi import FastAPI, File, UploadFile, Request
import uvicorn
import shutil
import pandas as pd
import numpy as np
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")
@app.get("/", response_class=HTMLResponse)
async def upload(request: Request):
   return templates.TemplateResponse("index.html", {"request": request})

@app.post("/uploader/")
async def create_upload_file(file1: UploadFile = File(...), file2: UploadFile = File(...)):
   with open("destination1.txt", "wb") as buffer:
      shutil.copyfileobj(file1.file, buffer)
   with open("destination2.csv", "wb") as buffer2:
      shutil.copyfileobj(file2.file, buffer2)

   df = pd.read_csv('destination2.csv')

   f = open("destination1.txt", "r")
   arr = []
   encountered_rollnos = set()

   for x in f:
      x = x.rstrip()
      rollno = int(x)
      
      if rollno not in encountered_rollnos:
         arr.append(rollno)
      else:
         arr = [x for x in arr if x != rollno]

      encountered_rollnos.add(rollno)

   df["Status"] = df["RollNo"].isin(arr).astype(int)

   df.to_csv('output.csv', index=False)
   
   return {"filename1": file1.filename, "filename2": file2.filename}
