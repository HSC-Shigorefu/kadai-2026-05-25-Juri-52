import subprocess
import sys
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]


def run_task(task_name, user_input, timeout=20):
    task_dir = ROOT / task_name
    script = task_dir / f"{task_name}.py"

    result = subprocess.run(
        [sys.executable, script.name],
        input=user_input,
        text=True,
        capture_output=True,
        cwd=task_dir,
        timeout=timeout,
    )

    assert result.returncode == 0, (
        f"{script} が正常に終了しませんでした。\n"
        f"stdout:\n{result.stdout}\n"
        f"stderr:\n{result.stderr}"
    )
    return result.stdout


def remove_if_exists(path):
    if path.exists():
        path.unlink()


def test_task01_clean_large_employee_csv():
    task_dir = ROOT / "task01"
    output_csv = task_dir / "employees_clean.csv"
    remove_if_exists(output_csv)

    run_task("task01", "2\n3\n4\n5\n6\n7\n8\n9\n10\n0\n")

    assert output_csv.exists(), "employees_clean.csv が作成されていません。"
    df = pd.read_csv(output_csv)

    expected_columns = [
        "社員ID",
        "氏名",
        "部署",
        "年齢",
        "基本給",
        "残業時間",
        "評価点",
        "入社日",
        "勤務地",
        "雇用形態",
        "ステータス",
        "役職",
    ]
    assert list(df.columns) == expected_columns
    assert len(df) == 480
    assert not df["社員ID"].duplicated().any()
    assert df["社員ID"].str.startswith("E").all()
    assert set(df["部署"]) <= {"営業", "開発", "人事", "経理", "サポート", "不明"}
    assert set(df["勤務地"]) <= {"東京", "大阪", "名古屋", "リモート", "不明"}
    assert df[["年齢", "基本給", "残業時間", "評価点"]].isna().sum().sum() == 0
    assert df["年齢"].between(18, 70).all()
    assert df["残業時間"].ge(0).all()
    assert df["評価点"].between(0, 100).all()


def test_task02_clean_sqlite_database_and_export():
    task_dir = ROOT / "task02"
    output_csv = task_dir / "company_payroll_clean.csv"
    remove_if_exists(output_csv)

    run_task("task02", "2\n3\n4\n5\n6\n0\n")

    assert output_csv.exists(), "company_payroll_clean.csv が作成されていません。"
    df = pd.read_csv(output_csv)

    expected_columns = [
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
    assert list(df.columns) == expected_columns
    assert len(df) >= 300
    assert not df[["社員ID", "対象月"]].duplicated().any()
    assert df["社員ID"].str.startswith("E").all()
    assert set(df["部署"]) <= {"営業", "開発", "人事", "経理", "サポート", "不明"}
    assert df[["基本給", "残業時間", "賞与", "勤務日数", "遅刻回数"]].isna().sum().sum() == 0
    assert df["残業時間"].ge(0).all()
    assert df["遅刻回数"].ge(0).all()


def test_task03_clean_3_csv_files_and_combine():
    task_dir = ROOT / "task03"
    output_csv = task_dir / "daily_reports_clean.csv"
    remove_if_exists(output_csv)

    run_task("task03", "2\n3\n4\n5\n6\n7\n8\n0\n", timeout=30)

    assert output_csv.exists(), "daily_reports_clean.csv が作成されていません。"
    df = pd.read_csv(output_csv)

    expected_columns = [
        "社員ID",
        "作業日",
        "部署",
        "プロジェクト",
        "作業時間",
        "コスト",
        "ステータス",
    ]
    assert list(df.columns) == expected_columns
    assert len(df) == 300
    assert df["社員ID"].str.startswith("E").all()
    assert set(df["部署"]) <= {"営業", "開発", "人事", "経理", "サポート", "不明"}
    assert set(df["ステータス"]) <= {"完了", "確認中", "差戻し", "不明"}
    assert df[["作業日", "作業時間", "コスト"]].isna().sum().sum() == 0
    assert df["作業時間"].between(0, 24).all()
    assert df["コスト"].ge(0).all()
