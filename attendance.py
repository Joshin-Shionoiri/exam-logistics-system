import streamlit as st
import pandas as pd
from datetime import datetime
import os

def show():
    st.subheader("✅ 受付管理画面")

    # CSVファイルの準備
    csv_file = "data/attendance.csv"
    if not os.path.exists(csv_file):
        pd.DataFrame(columns=["受験番号", "準会場コード", "受付日時"]).to_csv(csv_file, index=False)

    # 入力欄（バーコードリーダー対応）
    exam_id = st.text_input("受験番号（バーコードをスキャン）")
    venue_code = st.text_input("準会場コード（例：JUKU001）")

    # 登録処理
    if st.button("✅ 受付記録を登録する") and exam_id and venue_code:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_record = pd.DataFrame([[exam_id, venue_code, timestamp]],
                                  columns=["受験番号", "準会場コード", "受付日時"])
        new_record.to_csv(csv_file, mode="a", header=False, index=False)
        st.success(f"{exam_id} の受付を記録しました ✅")

    # 受付履歴表示
    st.markdown("---")
    st.subheader("📋 受付履歴一覧")
    df = pd.read_csv(csv_file)
    venue_filter = st.text_input("準会場コードで絞り込み（空欄で全表示）")
    if venue_filter:
        df = df[df["準会場コード"] == venue_filter]
    st.dataframe(df)
