import requests
from fastapi import FastAPI

app = FastAPI()


@app.post("/check_virtual_address")
async def check_virtual_address(merchant_id: str, merchant_ref_no: str, virtual_address: str, transaction_status: str):
    url = "https://upitestv2.hdfcbank.com/upi/checkMeVirtualAddress"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    payload = {
        "PGMerchantId": merchant_id,
        "Merchant Ref No": merchant_ref_no,
        "VPA": virtual_address,
        "Status": transaction_status
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.text


@app.post("/collect-transaction")
def collect_transaction(merchant_id: str, order_no: str, payer_virtual_addr: str, amount: int, remarks: str,
                        expiry: int):
    url = "https://upitestv2.hdfcbank.com/upi/meTransCollectSvc"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    payload = {
        "merchantId": merchant_id,
        "orderNo": order_no,
        "payerVirtualAddress": payer_virtual_addr,
        "amount": amount,
        "remarks": remarks,
        "expiry": expiry
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.text


@app.post("/transaction-status")
def transaction_status(merchant_id: str, order_no: str, upi_txn_id: int):
    url = "https://upitestv2.hdfcbank.com/upi/transactionStatusQuery"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    payload = {
        "merchantId": merchant_id,
        "orderNo": order_no,
        "UPITxnID": upi_txn_id
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.text


@app.post("/refund-request")
def refund_request(merchant_id: str, new_order_no: str, original_order_no: str,
                   original_trn_ref_no: int, original_cust_ref_no: int, remarks: str, refund_amt: int, currency: str,
                   transaction_type: str, payment_type: str):
    url = "https://upitestv2.hdfcbank.com/upi/refundReqSvc"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    payload = {
        "merchantId": merchant_id,
        "newOrderNo": new_order_no,
        "originalOrderNo": original_order_no,
        "originalTrnRefNo": original_trn_ref_no,
        "originalCustRefNo": original_cust_ref_no,
        "remarks": remarks,
        "refund_amt": refund_amt,
        "currency": currency,
        "transactionType": transaction_type,
        "paymentType": payment_type
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.text
