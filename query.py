import streamlit as st
import pandas as pd
import os

def show():
    st.subheader("🔍 成績照会画面")

    # CSVファイルの準備
    csv_file = "data/scores.csv"
    if not os.path.exists(csv_file):
        pd.DataFrame(columns=["受験番号", "パスワード", "得点", "判定"]).to_csv(csv_file, index=False)

    # 入力欄
    exam_id = st.text_input("受験番号")
    password = st.text_input("照会パスワード", type="password")

    # 照会処理
    if st.button("照会する"):
        df = pd.read_csv(csv_file)
        result = df[(df["受験番号"] == exam_id) & (df["パスワード"] == password)]

        if not result.empty:
            st.success("照会成功 ✅")
            st.write("📊 成績情報")
            st.dataframe(result[["得点", "判定"]])
        else:
            st.error("照会に失敗しました。受験番号またはパスワードが正しくありません。")
