import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# タイトル
st.title("📊 CSVデータ分析アプリ")

# ファイルアップロード
uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type=["csv"])

if uploaded_file is not None:
    # データ読み込み
    df = pd.read_csv(uploaded_file)
    st.subheader("データプレビュー")
    st.write(df.head())

    # 基本情報
    st.subheader("データの概要")
    st.write(df.describe())

    # 数値列の選択
    numeric_cols = df.select_dtypes(include=['float', 'int']).columns.tolist()
    if numeric_cols:
        col = st.selectbox("ヒストグラムを表示する列を選択", numeric_cols)
        fig, ax = plt.subplots()
        ax.hist(df[col].dropna(), bins=20)
        ax.set_title(f"{col} の分布")
        st.pyplot(fig)
    else:
        st.info("数値列が見つかりませんでした。")

else:
    st.info("まずCSVファイルをアップロードしてください。")