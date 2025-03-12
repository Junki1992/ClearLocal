import shutil
import argparse
from pathlib import Path

def organize_files(directory):
    directory = Path(directory).expanduser() # '~' を展開して完全なパスに変換
    if not directory.exists():
        print(f"指定されたフォルダは見つかりませんでした: {directory}")
        return

    # 分類マップ（拡張子ごとにフォルダを指定）
    file_categories = {
        "PDFs": [".pdf"],
        "Images": [".jpg", ".jpeg", ".png", "webp"],
        "Scripts": [".py", ".sh"],
        "Texts": [".txt", ".md"],
        "Videos": [".mp4", ".mov"],
        "Others": [] # どこにも分類されないファイル用
    }

    log_path = directory / "moved_files.log"

    with open(log_path, "w") as log_file:
        for file in directory.iterdir():
            # ファイルのみを処理し、フォルダは無視
            if file.is_file():  # この条件チェックを正しい位置に移動
                dest_folder = "Others"
                for category, extensions in file_categories.items():
                    if file.suffix.lower() in extensions:
                        dest_folder = category
                        break
                dest_folder_path = directory / dest_folder
                dest_folder_path.mkdir(exist_ok=True)

                new_file_path = dest_folder_path / file.name

                ## **重複ファイルの処理**
                counter = 1
                while new_file_path.exists():
                    new_file_path = dest_folder_path / f"{file.stem}_{counter}-{file.suffix}"
                    counter += 1

                # ファイル移動
                shutil.move(file, new_file_path)

                # ログに記録
                log_file.write(f"{file} → {new_file_path}\n")
    print(f"整理完了!ログ: {log_path}")

# argparseの設定
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="フォルダ内のファイルを拡張仕事に整理するスクリプト")
    parser.add_argument("directory", help="整理するフォルダのパス")
    args = parser.parse_args()

    organize_files(args.directory)