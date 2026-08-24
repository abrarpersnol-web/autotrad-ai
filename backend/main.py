from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DepositData(BaseModel):
    user_id: str
    amount: float
    card_number: str

class WithdrawData(BaseModel):
    user_id: str
    amount: float
    ton_address: str

@app.post("/api/v1/deposit")
async def process_deposit(data: DepositData):
    if data.amount < 1.0:
        raise HTTPException(status_code=400, detail="Minimum deposit is $1.00 USD")
    return {
        "status": "success",
        "message": f"Successfully processed ${data.amount} deposit request!"
    }

@app.post("/api/v1/withdraw-ton")
async def withdraw_ton(data: WithdrawData):
    if not data.ton_address.startswith(("EQ", "UQ")):
        raise HTTPException(status_code=400, detail="Invalid TON Wallet Address format")
    return {
        "status": "processing",
        "message": f"Withdrawal request of ${data.amount} to {data.ton_address} submitted!"
    }
