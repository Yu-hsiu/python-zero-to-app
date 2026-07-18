# account.py — Account 類別
# 對應課程：OOP、class、屬性與方法


class Account:
    """代表一個使用者的財務帳戶。"""

    def __init__(self, owner: str, records: list = None):
        self.owner = owner
        self.records = records if records is not None else []

    def add_record(self, date: str, category: str, amount: float, note: str):
        """新增一筆收支紀錄。"""
        record = {
            "date": date,
            "category": category,
            "amount": amount,
            "note": note,
        }
        self.records.append(record)

    def delete_record(self, index: int):
        """依索引刪除紀錄，索引越界時拋出 IndexError。"""
        if 0 <= index < len(self.records):
            removed = self.records.pop(index)
            return removed
        else:
            raise IndexError(f"索引 {index} 超出範圍（共 {len(self.records)} 筆）")

    def filter_by_category(self, category: str) -> list:
        """依類別篩選紀錄。"""
        return [r for r in self.records if r["category"] == category]

    def filter_by_month(self, month: str) -> list:
        """依月份 (YYYY-MM) 篩選紀錄。"""
        return [r for r in self.records if r["date"].startswith(month)]

    def __repr__(self):
        return f"Account(owner={self.owner!r}, records={len(self.records)} 筆)"
