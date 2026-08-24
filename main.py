from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os

app = FastAPI(title="Ai Trade API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DepositRequest(BaseModel):
    network: str
    amount: float
    txid: str

class WithdrawRequest(BaseModel):
    network: str
    amount: float
    destination: str

@app.get("/")
def read_root():
    return {"status": "online", "message": "Ai Trade Backend API Active"}

@app.post("/api/deposit")
def handle_deposit(data: DepositRequest):
    # Here your backend logs or verifies the TXID on chain
    return {"status": "success", "message": f"Received deposit submission for {data.amount} USDT ({data.network}). TXID: {data.txid}"}

@app.post("/api/withdraw")
def handle_withdraw(data: WithdrawRequest):
    if data.amount < 5:
        return {"status": "error", "message": "Minimum withdrawal is $5 USDT"}
    return {"status": "success", "message": f"Withdrawal request of {data.amount} USDT to {data.destination} submitted."}
