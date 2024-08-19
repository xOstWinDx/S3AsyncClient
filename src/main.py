from fastapi import FastAPI, UploadFile

from src.s3_client import DEFAULT_S3_CLIENT

app = FastAPI(title="S3 Test")


@app.put("/{file_name}")
async def upload_file(file: UploadFile):
    await DEFAULT_S3_CLIENT.upload_file(file=await file.read(), object_name=file.filename)
