from pathlib import Path

import pandas as pd


REPORT_DIR = Path("daily_reports")

df = pd.DataFrame()


while True:
    print("\n=== task03: 3個のCSVを1つにまとめてきれいにする ===")
    print("1. CSVファイルの数を表示する")
    print("2. すべてのCSVを読み込んで1つにまとめる")
    print("3. 列名と文字列を整理する")
    print("4. 作業時間とコストを整理する")
    print("5. 作業日を整理する")
    print("6. 不自然な値を欠損値にする")
    print("7. 欠損値を補完する")
    print("8. 必要な列だけ残して保存する")
    print("9. 現在の表を表示する")
    print("10. 欠損値の数を表示する")
    print("0. 終了")

    choice = input("番号を選んでください: ")

    if choice == "1":
        print(len(list(REPORT_DIR.glob("*.csv"))))
    elif choice == "2":
        csv_files = list(REPORT_DIR.glob("*.csv"))

        df = pd.concat(
        [pd.read_csv(csv_file) for csv_file in csv_files],
        ignore_index=True
        )

        print(df)
        pass
    elif choice == "3":
        # TODO: 列名、社員ID、部署、プロジェクト、ステータス、メモを整理する
        pass
    elif choice == "4":
        # TODO: 作業時間とコストを計算や集計に使える形にする
        pass
    elif choice == "5":
        # TODO: 作業日を日付として扱える形にする
        pass
    elif choice == "6":
        # TODO: 作業時間、コスト、作業日、部署、ステータスの不自然な値を欠損値にする
        pass
    elif choice == "7":
        # TODO: 欠損値を列ごとに適切な値で補完する
        pass
    elif choice == "8":
        # TODO: 必要な列だけを見やすい順番で残し、daily_reports_clean.csv に保存する
        pass
    elif choice == "9":
        print(df)
    elif choice == "10":
        print(df.isna().sum())
    elif choice == "0":
        break
    else:
        print("その番号はありません")
