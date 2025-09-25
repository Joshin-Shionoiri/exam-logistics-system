import streamlit as st
import pandas as pd
from datetime import datetime
import os

def show():
    st.subheader("📦 資材発送管理画面")

    # CSVファイルの準備
    csv_file = "data/shipping_log.csv"
    if not os.path.exists(csv_file):
        pd.DataFrame(columns=["資材ID", "準会場コード", "部数", "発送日"]).to_csv(csv_file, index=False)

    # 入力欄（バーコードリーダー対応）
    material_id = st.text_input("資材ID（バーコードをスキャン）")
    venue_code = st.text_input("準会場コード（例：JUKU001）")
    quantity = st.number_input("部数", min_value=1, step=1)

    # 登録処理
    if st.button("✅ 発送記録を登録する") and material_id and venue_code and quantity:
        shipping_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_record = pd.DataFrame([[material_id, venue_code, quantity, shipping_date]],
                                  columns=["資材ID", "準会場コード", "部数", "発送日"])
        new_record.to_csv(csv_file, mode="a", header=False, index=False)
        st.success(f"{material_id} を {venue_code} に {quantity}部 発送記録しました ✅")

    # 発送履歴表示
    st.markdown("---")
    st.subheader("📋 発送履歴一覧")
    df = pd.read_csv(csv_file)
    venue_filter = st.text_input("準会場コードで絞り込み（空欄で全表示）")
    if venue_filter:
        df = df[df["準会場コード"] == venue_filter]
    st.dataframe(df)
