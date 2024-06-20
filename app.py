"""
This is the main file for the FastAPI server. It uses the OpenAI API to generate a README for a given code snippet.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import uvicorn

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["chrome-extension://moohkniklmopfcljgkmoleaaefblleci"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

API_KEY = 'INPUT_YOUR_OPEN_AI_API_KEY'
client = OpenAI(api_key=API_KEY)
model_id = 'text-davincxi-003'

class CodeRequest(BaseModel):
    code: str

@app.post("/generate_readme")
async def generate_readme(request: CodeRequest):
    code = request.code.strip()  
    input_prompt = f"Generate a GitHub README for the following code:\n\n{code}\n\n"

    try:
        response = client.completions.create(
            model=model_id, 
            prompt=input_prompt,
            max_tokens=500, # max length of the completion
        )

        readme = response.choices[0].text.strip()
        print(readme)
        return {"readme": readme}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5002)



