import traceback

from fastapi import FastAPI, File, UploadFile
from paddle_script import extract_paddle_result

app = FastAPI()


@app.post("/processimage/")
async def create_upload_file(file: UploadFile):
    print("Trying to process file: {}".format(file.filename))
    try:
        contents = await file.read()
        with open(f"tmp.{file.filename.split('.')[1]}", "wb") as f:
            f.write(contents)
        return {"results": extract_paddle_result(f"tmp.{file.filename.split('.')[1]}")}
    except Exception as e:
        return {
            "error": "Unhandled Internal Server Error. Please send request data to atarasov@binariks.com",
            "details": {"exceptionType": str(type(e)), "args": str(e)},
            "traceback": traceback.format_exc()
            }

