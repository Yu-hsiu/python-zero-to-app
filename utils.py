# utils.py — 工具函式
# 對應課程：函式、math 模組、格式化輸出

import math


def format_record(record: dict) -> str:
    """將一筆紀錄格式化為易讀字串。"""
    sign = "+" if record["category"] == "收入" else "-"
    return (
        f"[{record['date']}] {record['category']} "
        f"{sign}{record['amount']:.2f} 元  備註：{record['note']}"
    )


def monthly_report(records: list, month: str):
    """印出指定月份的收支統計報表。"""
    monthly = [r for r in records if r["date"].startswith(month)]

    if not monthly:
        print(f"📭 {month} 無任何紀錄。")
        return

    income = sum(r["amount"] for r in monthly if r["category"] == "收入")
    expense = sum(r["amount"] for r in monthly if r["category"] == "支出")
    balance = income - expense

    print(f"\n📊 {month} 月收支報表")
    print(f"  收入：{income:.2f} 元")
    print(f"  支出：{expense:.2f} 元")
    print(f"  結餘：{balance:.2f} 元")
    print(f"  筆數：{len(monthly)} 筆")

    # 用 math.floor 示範 math 模組
    print(f"  (支出取整：{math.floor(expense)} 元)")
