from cgitb import handler
from fastapi import FastAPI, HTTPException
from copykitt import genarate_branding_anippet, genarate_keyword
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)
MAX_INPUT_LENGTH =32


@app.get("/genarate_snipper")
async def genarate_snippet_api(promt:str):
    validate_input_length(promt)
    snippet = genarate_branding_anippet(promt)
    return {"snippet": snippet, "keywords":[]}


@app.get("/genarate_keywords")
async def genarate_keywords_api(promt:str):
    validate_input_length(promt)
    keyword = genarate_keyword(promt)
    return {"snippet":None, "keywords": keyword}


@app.get("/genarate_snippet_and_ keywords")
async def genarate_keywords_api(promt:str):
    validate_input_length(promt)
    snippet = genarate_branding_anippet(promt)
    keyword = genarate_keyword(promt)
    return {"snippet": snippet, "keywords": keyword }

def validate_input_length(promt:str):
     if len(promt)>MAX_INPUT_LENGTH:
        raise HTTPException(status_code=400, detail=f"Input length to long. must be under {MAX_INPUT_LENGTH}")

# uvicorn copykitt_api:app --reload