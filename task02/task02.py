import sqlite3
from pathlib import Path

import pandas as pd

from output_helper import create_summary_table


DATABASE_FILE = Path("company.db")

employees_df = pd.DataFrame()
payroll_df = pd.DataFrame()
attendance_df = pd.DataFrame()
summary_df = pd.DataFrame()


while True:
    print("\n=== task02: 1つのSQLiteデータベースをきれいにしてCSV保存する ===")
    print("1. データベースとテーブル名を表示する")
    print("2. SQLクエリーで3つの表を読み込む")
    print("3. 社員データを整理する")
    print("4. 給与データを整理する")
    print("5. 勤怠データを整理する")
    print("6. company_payroll_clean.csv に保存する")
    print("7. 現在の保存用データを表示する")
    print("0. 終了")

    choice = input("番号を選んでください: ")

    if choice == "1":
        print(DATABASE_FILE)
        print("employees")
        print("payroll")
        print("attendance")
    elif choice == "2":
        # TODO: company.db に接続し、SQLクエリーを書いて employees, payroll, attendance を読み込む
        pass
    elif choice == "3":
        # TODO: 社員データのID、文字列、日付、重複を整理する
        pass
    elif choice == "4":
        # TODO: 給与データのID、月、基本給、残業時間、賞与を整理する
        pass
    elif choice == "5":
        # TODO: 勤怠データのID、月、勤務日数、遅刻回数を整理する
        pass
    elif choice == "6":
        summary_df = create_summary_table(employees_df, payroll_df, attendance_df)
        # TODO: company_payroll_clean.csv に保存する
        pass
    elif choice == "7":
        if summary_df.empty:
            summary_df = create_summary_table(employees_df, payroll_df, attendance_df)
        print(summary_df)
    elif choice == "0":
        break
    else:
        print("その番号はありません")
