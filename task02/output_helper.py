import pandas as pd


def create_summary_table(employees_df, payroll_df, attendance_df):
    required_employee_columns = ["社員ID", "氏名", "部署", "勤務地", "ステータス", "入社日"]
    required_payroll_columns = ["社員ID", "対象月", "基本給", "残業時間", "賞与"]
    required_attendance_columns = ["社員ID", "対象月", "勤務日数", "遅刻回数"]
    final_columns = [
        "社員ID",
        "氏名",
        "部署",
        "勤務地",
        "ステータス",
        "入社日",
        "対象月",
        "基本給",
        "残業時間",
        "賞与",
        "勤務日数",
        "遅刻回数",
    ]

    if employees_df.empty or payroll_df.empty or attendance_df.empty:
        print("先に2〜5を実行してください")
        return pd.DataFrame()
    if not set(required_employee_columns) <= set(employees_df.columns):
        print("社員データの列名を確認してください")
        return pd.DataFrame()
    if not set(required_payroll_columns) <= set(payroll_df.columns):
        print("給与データの列名を確認してください")
        return pd.DataFrame()
    if not set(required_attendance_columns) <= set(attendance_df.columns):
        print("勤怠データの列名を確認してください")
        return pd.DataFrame()

    result_df = pd.merge(payroll_df, attendance_df, on=["社員ID", "対象月"], how="left")
    result_df = pd.merge(result_df, employees_df, on="社員ID", how="left")
    return result_df[final_columns]
