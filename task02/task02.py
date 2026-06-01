import sqlite3
from idlelib import query
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
        conn = sqlite3.connect(DATABASE_FILE)
        query = """
        SELECT * FROM employees
        """
        employees_df = pd.read_sql_query(query, conn)
        query = """
        SELECT * FROM payroll
        """
        payroll_df = pd.read_sql_query(query, conn)
        query = """
        SELECT * FROM attendance
        """
        attendance_df = pd.read_sql_query(query, conn)
        pass
    elif choice == "3":
        # TODO: 社員データのID、文字列、日付、重複を整理する
        print(employees_df.columns)
        employees_df["employee_id"] = employees_df["employee_id"].astype(str).str.strip().str.upper()
        employees_df["employee_id"] = employees_df["employee_id"].str.replace("EMP-","E",regex=False)
        employees_df["name"] = employees_df["name"].astype(str).str.strip()
        employees_df["department"] = employees_df["department"].astype(str).str.strip().str.upper()
        employees_df["department"] = employees_df["department"].str.replace({
            "SALES":"営業","ＤＥＶ":"DEV","DEV":"開発","HR":"人事","SUPPORT":"サポート","ACCOUNTING":"経理"
        },regex=False)
        employees_df["office"] = employees_df["office"].astype(str).str.strip().str.upper()
        employees_df["office"] = employees_df["office"].str.replace({
            "TOKYO":"東京","OSAKA":"大阪","NAGOYA":"名古屋","REMOTE":"リモート"
        },regex=False)
        employees_df["status"] = employees_df["status"].astype(str).str.strip().str.upper()
        employees_df["status"] = employees_df["status"].str.replace({
            "ACTIVE":"在籍","RETIRED":"退職","LEAVE":"休職"
        },regex=False)
        employees_df["joined_at"] = employees_df["joined_at"].str.replace({
            "/":"-","年":"-","月":"-","日":""
        },regex=False)
        employees_df["joined_at"] = pd.to_datetime(employees_df["joined_at"],errors="coerce")
        employees_df = employees_df.drop_duplicates(subset="employee_id", keep="last")
        print(employees_df)
        employees_df.to_csv("employees_crean.csv", index=False, encoding="utf-8")
        pass
    elif choice == "4":
        # TODO: 給与データのID、月、基本給、残業時間、賞与を整理する
        payroll_df["employee_id"] = payroll_df["employee_id"].astype(str).str.strip().str.upper()
        payroll_df["employee_id"] = payroll_df["employee_id"].str.replace("EMP-", "E", regex=False)
        payroll_df["base_salary"] = payroll_df["base_salary"].astype(str).str.replace({"¥":"",",":"","円":""},regex=False)
        payroll_df["base_salary"] = pd.to_numeric(payroll_df["base_salary"],errors="coerce").astype("Int64")
        payroll_df["overtime_hours"] = payroll_df["overtime_hours"].astype(str).str.replace("時間","",regex=False)
        payroll_df["overtime_hours"] = pd.to_numeric(payroll_df["overtime_hours"],errors="coerce").astype("Int64")
        payroll_df.loc[
            (payroll_df["overtime_hours"] < 0),"overtime_hours"
        ] = pd.NA
        payroll_df["bonus"] = payroll_df["bonus"].astype(str).str.replace({"¥": "", ",": ""},regex=False)
        payroll_df["bonus"] = pd.to_numeric(payroll_df["bonus"], errors="coerce").astype("Int64")
        print(payroll_df)
        payroll_df.to_csv("payroll_crean.csv", index=False, encoding="utf-8")
        pass
    elif choice == "5":
        # TODO: 勤怠データのID、月、勤務日数、遅刻回数を整理する
        attendance_df["employee_id"] = attendance_df["employee_id"].astype(str).str.strip().str.upper()
        attendance_df["employee_id"] = attendance_df["employee_id"].str.replace("EMP-", "E", regex=False)
        attendance_df["work_days"] = pd.to_numeric(attendance_df["work_days"],errors="coerce").astype("Int64")
        attendance_df["late_count"] = pd.to_numeric(attendance_df["late_count"],errors="coerce").astype("Int64")
        attendance_df.loc[
            (attendance_df["late_count"] < 0),"late_count"
        ] = pd.NA
        print(attendance_df)
        attendance_df.to_csv("attendance_crean.csv", index=False, encoding="utf-8")
        pass
    elif choice == "6":
        employees_df = employees_df.rename(
            columns={"employees_id":"社員ID","name":"氏名","department":"部署",
                     "office":"勤務地","status":"ステータス","joined_at":"入社日"})
        payroll_df = payroll_df.rename(
            columns={"employee_id":"社員ID","month":"対象月","base_salary":"基本給",
                     "overtime_hours":"残業時間","bonus":"賞与"})
        attendance_df = attendance_df.rename(
            columns={"employee_id":"社員ID","month":"対象月","work_days":"勤務日数","late_count":"遅刻回数"})
        summary_df = create_summary_table(employees_df, payroll_df, attendance_df)
        # TODO: company_payroll_clean.csv に保存する
        print(summary_df)
        summary_df.to_csv("company_payroll_crean.csv",index=False,encoding="utf-8")
        pass
    elif choice == "7":
        if summary_df.empty:
            summary_df = create_summary_table(employees_df, payroll_df, attendance_df)
        print(summary_df)
    elif choice == "0":
        break
    else:
        print("その番号はありません")
