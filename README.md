# ダウンロードフォルダ整理スクリプト

## 概要
このスクリプトは、指定されたフォルダ内のファイルを拡張子ごとに整理します。

## 使い方
1. Pythonをインストール（必要なら）
2. スクリプトを実行
   ```bash
   # Downloadsフォルダを整理する場合
   python organize_files.py ~/Downloads

   # カレントディレクトリを整理する場合
   python organize_files.py .
   ```

## 整理後のフォルダ構成
```
指定したフォルダ
├── PDFs
│   └── document.pdf
├── Images
│   └── photo.jpg, photo.png など
├── Scripts
│   └── script.py, script.sh など
├── Texts
│   └── notes.txt, README.md など
├── Videos
│   └── video.mp4, movie.mov など
└── Others
    └── その他の拡張子のファイル
```

## ログ
整理の結果は `moved_files.log` に記録されます。

