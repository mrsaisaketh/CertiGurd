from core.hasher import generate_hash
from core.blockchain import store_hash, verify_hash
from ai.ml_detector import predict_certificate
from core.ocr_engine import extract_text
import time


def verify_certificate(file_path):

    # 1️⃣ Extract text using real OCR
    try:
        text = extract_text(file_path)
    except Exception as e:
        return f"OCR Error: {str(e)}", "ERROR"

    # 2️⃣ Generate SHA-256 hash
    file_hash = generate_hash(file_path)
    hash_bytes = bytes.fromhex(file_hash)

    # 3️⃣ Check if already stored on blockchain
    try:
        on_chain = verify_hash(hash_bytes)
    except Exception as e:
        return f"Blockchain Error: {str(e)}", "ERROR"

    # 4️⃣ If already verified on blockchain
    if on_chain:
        status = "ORIGINAL (VERIFIED ON BLOCKCHAIN)"
        confidence_display = "Stored On-Chain"

    else:
        # 5️⃣ ML prediction
        try:
            prediction, probability = predict_certificate(text)
        except Exception as e:
            return f"ML Model Error: {str(e)}", "ERROR"

        if prediction == 1:
            store_hash(hash_bytes)
            status = "ORIGINAL (NEWLY STORED ON BLOCKCHAIN)"
        else:
            status = "FAKE"

        confidence_display = f"{round(probability * 100, 2)}%"

    # 6️⃣ Final formatted result
    result = f"""
STATUS: {status}
AI CONFIDENCE: {confidence_display}
VERIFIED AT: {time.ctime()}
"""

    return result, status