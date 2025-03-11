import os
import shutil
from pathlib import Path

# Downloadsフォルダ内のパスを取得
downloads_path = str(Path.home() / "Downloads")

# ファイル一覧を取得して表示
print("Downloadsフォルダ内のファイル一覧")

# 分類マップ（拡張子ごとにフォルダを指定）
category_map = {
    "PDFs": [".pdf"],
    "Images": [".jpg", ".jpeg", ".png", "webp"],
    "Scripts": [".py", ".sh"],
    "Texts": [".txt", ".md"],
    "Videos": [".mp4", ".mov"]
}

# その他をファイルを入れるフォルダ
other_folder = "Others"

# ファイルの一覧を取得
files = [f for f in os.listdir(downloads_path) if os.path.isfile(os.path.join(downloads_path, f))]

# ファイルごとに処理
for file in files:
    file_path = os.path.join(downloads_path, file)
    ext = os.path.splitext(file)[1].lower() # 拡張子を取得(小文字に変換)

    # 拡張子にあったフォルダを探す
    destination_folder = other_folder # デフォルトはOthers
    for folder, extensions in category_map.items():
        if ext in extensions:
            destination_folder = folder
            break

    # フォルダパスを作成
    destination_path = os.path.join(downloads_path, destination_folder) 

    # フォルダがなければ作成
    os.makedirs(destination_path, exist_ok=True)

    # ファイルを移動
    shutil.move(file_path, os.path.join(destination_path, file))
    print(f"Moved] {file} → {destination_path}/")

print("整理完了！")