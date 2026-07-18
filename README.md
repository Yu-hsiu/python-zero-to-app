# 🐍 python-Train

> **個人財務記帳 CLI App** 

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📌 專案背景

本專案的目的是 能夠以最小限度的開發複習python技能。

---

## 🎯 功能總覽

| 功能 | 說明 | 對應課程知識點 |
|------|------|----------------|
| 新增/刪除收支紀錄 | 記錄日期、類別、金額、備註 | 變數、List、字典 |
| 分類查詢與篩選 | 依類別或日期篩選 | if/elif、迴圈 |
| 統計月收支報表 | 計算月支出/收入總額 | 函式、math 模組 |
| 資料持久化 | CSV 格式存讀檔案 | 檔案讀寫 |
| 輸入錯誤保護 | 非法輸入自動提示重試 | try/except |
| 多帳戶管理 | 每位使用者獨立帳戶 | OOP (Account class) |

---

## 🗂️ 專案結構

```
python-zero-to-app/
├── README.md           # 專案說明（本文件）
├── main.py             # 主程式入口（CLI 選單）
├── account.py          # Account 類別（OOP 設計）
├── storage.py          # 資料讀寫模組（CSV）
├── utils.py            # 工具函式（統計、格式化輸出）
├── data/
│   └── records.csv     # 資料儲存（自動建立）
└── tests/
    └── test_account.py # 單元測試
```

---

## ⚙️ 環境需求

- Python 3.10 以上
- 無需安裝第三方套件（純標準函式庫）

---

## 🚀 快速開始

### 1. Clone 專案
```bash
git clone https://github.com/Yu-hsiu/python-zero-to-app.git
cd python-zero-to-app
```

### 2. 執行程式
```bash
python main.py
```

### 3. 執行單元測試
```bash
python -m unittest tests/test_account.py -v
```

---

## 🖥️ 線上執行（無需安裝）

點擊以下按鈕直接在瀏覽器中執行：

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/Yu-hsiu/python-zero-to-app)

> GitHub Codespaces 提供免費的雲端開發環境，開啟後直接在終端機輸入 `python main.py` 即可。

---

## 📖 課程知識點對應

```
第01集  環境建置         → 本專案執行環境設定
第02集  變數與資料型態    → account.py 的屬性設計
第03集  條件判斷          → main.py 選單邏輯
第04集  迴圈             → main.py 主迴圈
第05集  List/Dict        → 收支紀錄的資料結構
第06集  函式             → utils.py 統計函式
第07集  模組             → storage.py 模組化設計
第08集  檔案操作          → storage.py CSV 讀寫
第09集  例外處理          → try/except 輸入保護
第10集  OOP             → account.py Account 類別
```

---

## 🛣️ 開發里程碑

- [ ] **Milestone 1** — 基礎 CLI 選單 + 新增紀錄 (`main.py`)
- [ ] **Milestone 2** — CSV 存讀資料 (`storage.py`)
- [ ] **Milestone 3** — 查詢與統計報表 (`utils.py`)
- [ ] **Milestone 4** — OOP 多帳戶管理 (`account.py`)
- [ ] **Milestone 5** — 例外處理強化 + 單元測試
- [ ] **Milestone 6** — README 完善 + 展示截圖

---

## 🤝 貢獻指南

1. Fork 本專案
2. 建立 feature branch：`git checkout -b feature/your-feature`
3. 提交 commit：`git commit -m 'Add: 新功能描述'`
4. 推送：`git push origin feature/your-feature`
5. 開啟 Pull Request

---

## 📄 授權

MIT License © 2026 Yu-hsiu
