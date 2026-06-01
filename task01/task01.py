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
        df.columns = df.columns.str.strip()
        df = df.rename(columns={
            "employee_id":"社員ID","department":"部署","base_salary":"基本給","office":"勤務地","status":"ステータス"
        })
        pass
    elif choice == "3":
        # TODO: 社員ID、氏名、部署、勤務地、雇用形態、ステータス、役職、メモを整理する
        df["社員ID"] = df["社員ID"].astype(str).str.strip().str.upper()
        df["氏名"] = df["氏名"].astype(str).str.strip().str.upper()
        df["部署"] = df["部署"].astype(str).str.strip().str.upper()
        df["勤務地"] = df["勤務地"].astype(str).str.strip().str.upper()
        df["雇用形態"] = df["雇用形態"].astype(str).str.strip().str.upper()
        df["ステータス"] = df["ステータス"].astype(str).str.strip().str.upper()
        df["役職"] = df["役職"].astype(str).str.strip().str.upper()
        df["メモ"] = df["メモ"].astype(str).str.strip().str.upper()
        pass
    elif choice == "4":
        # TODO: 同じ社員IDのデータを1件だけ残す
        df["社員ID"] = df["社員ID"].str.replace("EMP-", "E", regex=False)
        df = df.drop_duplicates(subset="社員ID", keep="last")
        pass
    elif choice == "5":
        # TODO: 部署、勤務地、雇用形態、ステータスの表記を統一する
        df["部署"] = df["部署"].str.replace({
            "SALES": "営業", "HR": "人事", "SUPPORT": "サポート", "ACCOUNTING": "経理", "ＤＥＶ": "DEV", "DEV": "開発"
        }, regex=False)
        df["勤務地"] = df["勤務地"].str.replace({
            "TOKYO": "東京", "OSAKA": "大阪", "NAGOYA": "名古屋", "REMOTE": "リモート"
        }, regex=False)
        df["雇用形態"] = df["雇用形態"].str.replace({
            "-": "", "PARTTIME": "アルバイト", "FULLTIME": "正社員", "CONTRACT": "契約"
        }, regex=False)
        df["ステータス"] = df["ステータス"].str.replace({
            "ACTIVE": "在籍", "LEAVE": "休職", "RETIRED": "退職"
        }, regex=False)
        pass
    elif choice == "6":
        # TODO: 年齢、基本給、残業時間、評価点を計算や集計に使える形にする
        df["年齢"] = df["年齢"].astype(str).str.replace("歳","",regex=False)
        df["年齢"] = pd.to_numeric(df["年齢"],errors="coerce").astype("Int64")
        df["基本給"] = df["基本給"].astype(str).str.replace({"¥":"","円":"",",":""},regex=False)
        df["基本給"] = pd.to_numeric(df["基本給"],errors="coerce").astype("Int64")
        df["残業時間"] = df["残業時間"].astype(str).str.replace("時間","",regex=False)
        df["残業時間"] = pd.to_numeric(df["残業時間"],errors="coerce").astype("Int64")
        df["評価"] = df["評価"].astype(str).str.replace("点","",regex=False)
        df["評価"] = pd.to_numeric(df["評価"],errors="coerce").astype("Int64")
        pass
    elif choice == "7":
        # TODO: 入社日を日付として扱える形にする
        df["入社日"] = df["入社日"].astype(str).str.replace({"年":"-","月":"-","日":"","/":"-"},regex=False)
        df["入社日"] = pd.to_datetime(df["入社日"],errors="coerce")
        pass
    elif choice == "8":
        # TODO: 年齢、基本給、残業時間、評価点、部署、勤務地の不自然な値を欠損値にする
        df.loc[
            (df["年齢"] > 60),"年齢"
        ] = pd.NA
        df.loc[
            (df["残業時間"] < 0),"残業時間"
        ] = pd.NA
        df.loc[
            (df["評価"] > 100),"年齢"
        ] = pd.NA
        pass
    elif choice == "9":
        # TODO: 欠損値を列ごとに適切な値で補完する
        df["年齢"] = df["年齢"].fillna(-1)
        df["基本給"] = df["基本給"].fillna(-1)
        df["残業時間"] = df["残業時間"].fillna(-1)
        df["評価"] = df["評価"].fillna(-1)
        df["入社日"] = df["入社日"].fillna("2000-01-01")
        df["入社日"] = pd.to_datetime(df["入社日"], errors="coerce")
        df["ステータス"] = df["ステータス"].fillna("不明")
        pass
    elif choice == "10":
        # TODO: 必要な列だけを見やすい順番で残し、employees_clean.csv に保存する
        df = df[["社員ID","氏名","年齢","ステータス","部署","役職","雇用形態","勤務地","入社日","評価","基本給"]]
        print(df.head(5))
        df.to_csv("employees_clean.csv", index=False, encoding="utf-8")
        pass
    elif choice == "11":
        print(df)
    elif choice == "12":
        print(df.isna().sum())
    elif choice == "0":
        break
    else:
        print("その番号はありません")
