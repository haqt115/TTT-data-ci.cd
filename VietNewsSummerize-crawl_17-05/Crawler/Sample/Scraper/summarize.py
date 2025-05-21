import pandas as pd
import google.generativeai as genai
import os


# ===== 1. Danh sách API keys thay vì 1 key =====
API_KEYS = {
    "key1": "AIzaSyDbyeu_mamcJ_mnCz0x8rn9Bs01hb0ZGCc",
    "key2": "AIzaSyBOb1EJ7shnujjEDFYx7H2p4MszqEsVPL8",
    "key3": "AIzaSyAHPtfknfozqPAyX82Y7yLJCdZJuYDdQVY",
}

# ===== 2. Hàm tạo mô hình theo key =====
def load_model(api_key):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("models/gemini-2.0-flash")


# 3. Hàm tóm tắt nội dung

def summarize_text(text, max_len=3000):
    text = str(text)
    if len(text) > max_len:
        text = text[:max_len]  # Giới hạn độ dài để tránh lỗi

    prompt = f"Tóm tắt văn bản sau trong 3 đến 4 câu:\n\n{text}"
    for name, key in API_KEYS.items():
        try:
            model = load_model(key)
            response = model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            print(f"[!] Key '{name}' bị lỗi: {e}")
            continue

    print("[!] Tất cả các API key đều thất bại.")
    return ""
    

# 4. Hàm xử lý file sau khi đã crawl và preprocess
def summarize_news(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"[!] File {input_path} không tồn tại.")
        return

    df = pd.read_csv(input_path)

    if "content" not in df.columns:
        print(f"[!] Không tìm thấy cột 'content' trong file {input_path}.")
        return

    print(f"[*] Đang tóm tắt file: {input_path} (tổng cộng {len(df)} dòng)")
    df["summary"] = df["content"].apply(summarize_text)

    df.to_csv(output_path, index=False)
    print(f"[+] Đã lưu dữ liệu tóm tắt vào: {output_path}")


# 5. Nếu gọi trực tiếp từ CLI
if __name__ == "__main__":
    summarize_news(
        "Crawler/Data/vnexpress_process.csv",
        "Crawler/Data/vnexpress_summarized.csv"
    )
