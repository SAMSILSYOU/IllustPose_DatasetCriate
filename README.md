# IllustPose_DatasetCriate
IllustPose用のデータセットを作成するためのリポジトリです。

## 概要
IllustPoseで使用するためのJSONファイルを作成します。COCO 2016 Keypoint Dataset(<https://cocodataset.org/#keypoints-2016>)のアノテーション情報を参考に作成しています。

## 操作方法
cv2,matplotlib,PILのライブラリをインポートしてください。
DatasetCriate.pyを実行するとdataフォルダ内の画像が読み取られます。打った点の座標をJSONファイルとしてdataフォルダ内に出力されます。

右クリック:　座標決定

dキー:　次のパーツへ

aキー:　前のパーツへ

rキー:　リセット 
　
escキー:　次の画像へ
