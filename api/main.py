from fastapi import FastAPI
import os
from fastapi import FastAPI, File, UploadFile
from PIL import Image
from fastapi.responses import FileResponse
import shutil

app = FastAPI()

@app.post("/inference")
async def inference(file: UploadFile = File(...)):

    #empty dir
    dir = ['/app/src/results/cmp', '/app/src/results/restored_faces',
            '/app/src/results/cropped_faces', '/app/src/results/restored_imgs',
            '/app/src/inputs/whole_imgs']

    for i in range(len(dir)):
        for f in os.listdir(dir[i]):
            os.remove(os.path.join(dir[i], f))
    
    #read image
    im = Image.open(file.file)
    im.save(f"/app/src/inputs/whole_imgs/{file.filename}") 

    #enhance image
    os.system('python3 /app/src/inference_gfpgan.py -i /app/src/inputs/whole_imgs -o /app/src/results')

    #zip results
    shutil.make_archive('/app/src/results','zip','/app/src/results')

    response = FileResponse('/app/src/results.zip', media_type="application/x-zip-compressed")
    response.headers["Content-Disposition"] = "attachment; filename=results.zip"
    
    return response
