# tests/test_account.py — 單元測試
# 對應課程：函式回傳值、OOP

import unittest
from account import Account


class TestAccount(unittest.TestCase):

    def setUp(self):
        self.acc = Account(owner="測試使用者")

    def test_add_record(self):
        self.acc.add_record("2026-07-01", "收入", 50000.0, "薪資")
        self.assertEqual(len(self.acc.records), 1)
        self.assertEqual(self.acc.records[0]["amount"], 50000.0)

    def test_delete_record(self):
        self.acc.add_record("2026-07-01", "支出", 300.0, "午餐")
        self.acc.delete_record(0)
        self.assertEqual(len(self.acc.records), 0)

    def test_delete_invalid_index(self):
        with self.assertRaises(IndexError):
            self.acc.delete_record(99)

    def test_filter_by_category(self):
        self.acc.add_record("2026-07-01", "收入", 50000.0, "薪資")
        self.acc.add_record("2026-07-02", "支出", 300.0, "午餐")
        income_records = self.acc.filter_by_category("收入")
        self.assertEqual(len(income_records), 1)

    def test_filter_by_month(self):
        self.acc.add_record("2026-07-01", "支出", 100.0, "飲料")
        self.acc.add_record("2026-08-01", "支出", 200.0, "書籍")
        july_records = self.acc.filter_by_month("2026-07")
        self.assertEqual(len(july_records), 1)


if __name__ == "__main__":
    unittest.main()
