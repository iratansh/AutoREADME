from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import uvicorn

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["chrome-extension://moohkniklmopfcljgkmoleaaefblleci"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model_name = 'gpt2-medium'
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

class CodeRequest(BaseModel):
    code: str

@app.post("/generate_readme")
async def generate_readme(request: CodeRequest):
    code = request.code
    input_prompt = f"Generate a GitHub README for the following code:\n\n{code}"
    input_ids = tokenizer.encode(input_prompt, return_tensors='pt')

    # Ensure input_ids do not exceed model's max length
    if input_ids.shape[1] > 1024:
        input_ids = input_ids[:, :1024]

    # Attention mask
    attention_mask = torch.ones(input_ids.shape, dtype=torch.long)

    with torch.no_grad():
        outputs = model.generate(
            input_ids,
            max_new_tokens=500,  # Adjust this based on your requirements
            num_return_sequences=1,
            attention_mask=attention_mask,
            pad_token_id=tokenizer.eos_token_id
        )

    readme = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
    print(readme)
    return {"readme": readme}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5002)


