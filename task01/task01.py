import pandas as pd


df = pd.read_csv("employees_dirty.csv")


while True:
    print("\n=== task01: 500行の社員CSVをきれいにする ===")
    print("1. 最初の10行を表示する")
    print("2. 列名を整理する")
    print("3. 社員IDと文字列を整理する")
    print("4. 社員IDの重複を削除する")
    print("5. カテゴリの表記を統一する")
    print("6. 数値データを整理する")
    print("7. 入社日を整理する")
    print("8. 不自然な値を欠損値にする")
    print("9. 欠損値を補完する")
    print("10. 必要な列だけ残して保存する")
    print("11. 現在の表を表示する")
    print("12. 欠損値の数を表示する")
    print("0. 終了")

    choice = input("番号を選んでください: ")

    if choice == "1":
        print(df.head(10))
    elif choice == "2":
        # TODO: 列名を整理し、社員データとして分かりやすい名前にそろえる
        pass
    elif choice == "3":
        # TODO: 社員ID、氏名、部署、勤務地、雇用形態、ステータス、役職、メモを整理する
        pass
    elif choice == "4":
        # TODO: 同じ社員IDのデータを1件だけ残す
        pass
    elif choice == "5":
        # TODO: 部署、勤務地、雇用形態、ステータスの表記を統一する
        pass
    elif choice == "6":
        # TODO: 年齢、基本給、残業時間、評価点を計算や集計に使える形にする
        pass
    elif choice == "7":
        # TODO: 入社日を日付として扱える形にする
        pass
    elif choice == "8":
        # TODO: 年齢、基本給、残業時間、評価点、部署、勤務地の不自然な値を欠損値にする
        pass
    elif choice == "9":
        # TODO: 欠損値を列ごとに適切な値で補完する
        pass
    elif choice == "10":
        # TODO: 必要な列だけを見やすい順番で残し、employees_clean.csv に保存する
        pass
    elif choice == "11":
        print(df)
    elif choice == "12":
        print(df.isna().sum())
    elif choice == "0":
        break
    else:
        print("その番号はありません")
