# main.py — 主程式入口（CLI 選單）
# 對應課程：條件判斷、迴圈、例外處理

from account import Account
from storage import load_records, save_records
from utils import monthly_report, format_record


def show_menu():
    print("\n========== 個人財務記帳 ==========")
    print("1. 新增收支紀錄")
    print("2. 刪除紀錄")
    print("3. 查詢所有紀錄")
    print("4. 月收支報表")
    print("5. 離開")
    print("==================================")


def main():
    # 載入資料（檔案不存在時回傳空 list）
    records = load_records()
    account = Account(owner="預設使用者", records=records)

    while True:
        show_menu()
        try:
            choice = input("請選擇功能 (1-5)：").strip()
        except KeyboardInterrupt:
            print("\n程式結束。")
            break

        if choice == "1":
            try:
                date = input("日期 (YYYY-MM-DD)：").strip()
                category = input("類別（收入/支出）：").strip()
                amount = float(input("金額："))
                note = input("備註：").strip()
                account.add_record(date, category, amount, note)
                save_records(account.records)
                print("✅ 新增成功！")
            except ValueError:
                print("❌ 金額格式錯誤，請輸入數字。")

        elif choice == "2":
            try:
                idx = int(input("請輸入要刪除的紀錄編號：")) - 1
                account.delete_record(idx)
                save_records(account.records)
                print("✅ 刪除成功！")
            except (ValueError, IndexError):
                print("❌ 無效的編號。")

        elif choice == "3":
            if not account.records:
                print("目前無任何紀錄。")
            else:
                for i, r in enumerate(account.records, 1):
                    print(f"{i}. {format_record(r)}")

        elif choice == "4":
            month = input("輸入月份 (YYYY-MM)：").strip()
            monthly_report(account.records, month)

        elif choice == "5":
            print("感謝使用，再見！")
            break

        else:
            print("❌ 無效選項，請輸入 1-5。")


if __name__ == "__main__":
    main()
