# storage.py — 資料讀寫模組
# 對應課程：檔案操作、模組、例外處理

import csv
import os

DATA_PATH = os.path.join("data", "records.csv")
FIELDNAMES = ["date", "category", "amount", "note"]


def load_records() -> list:
    """從 CSV 讀取所有紀錄，檔案不存在時回傳空 list。"""
    if not os.path.exists(DATA_PATH):
        return []
    records = []
    try:
        with open(DATA_PATH, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["amount"] = float(row["amount"])
                records.append(row)
    except Exception as e:
        print(f"⚠️ 讀取資料失敗：{e}")
    return records


def save_records(records: list):
    """將所有紀錄寫入 CSV。"""
    os.makedirs("data", exist_ok=True)
    try:
        with open(DATA_PATH, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(records)
    except Exception as e:
        print(f"⚠️ 儲存資料失敗：{e}")
