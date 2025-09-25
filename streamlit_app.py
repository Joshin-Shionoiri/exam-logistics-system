import streamlit as st

st.set_page_config(page_title="試験運営システム", layout="wide")
st.title("📘 試験運営システム")

# サイドバーで画面選択
page = st.sidebar.selectbox("表示する画面を選択してください", ["受付管理", "資材発送管理", "成績照会"])

# 受付管理画面
if page == "受付管理":
    st.subheader("✅ 受付管理")
    exam_id = st.text_input("受験番号（バーコードをスキャン）")
    venue_code = st.text_input("準会場コード")
    if st.button("受付記録を登録する"):
        st.success(f"{exam_id} の受付を記録しました ✅")

# 資材発送管理画面
elif page == "資材発送管理":
    st.subheader("📦 資材発送管理")
    material_id = st.text_input("資材ID（バーコードをスキャン）")
    venue_code = st.text_input("準会場コード")
    quantity = st.number_input("部数", min_value=1, step=1)
    if st.button("発送記録を登録する"):
        st.success(f"{material_id} を {venue_code} に {quantity}部 発送記録しました ✅")

# 成績照会画面
elif page == "成績照会":
    st.subheader("🔍 成績照会")
    exam_id = st.text_input("受験番号")
    password = st.text_input("照会パスワード", type="password")
    if st.button("照会する"):
        st.info(f"{exam_id} の成績を表示します（仮）")
