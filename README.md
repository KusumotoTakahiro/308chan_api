# 308chan_api
DRF（DjangoRestfulFramework）で作成したAPIです．
中身は，超簡易的な掲示板を扱うためのAPIとなっており，RoomとCommentから構成されています．
一応，DRFのデフォルトのままCRUD処理には，対応しています．

## clone後の立ち上げ方
docker-compose.ymlがある階層で以下のコマンドを実行します．
```sh
docker compose up
```
終了です．
以下にアクセスして，エラーが出なければ問題ありません．
http://localhost:8081/room/

## 動作確認
さきほどまでで動作確認はできていましたが，ここでは，GETとPOSTに関して，動作確認を行いたいと思います．
後学のためにも，Postmanを使ったリクエストを推奨しますが，今回は動作確認が目的なので，cURLでの確認方法を記載します．
※PostmanとはAPIの挙動を確認するためのツールです．基本無料で使えます.（2024年11月03日時点）

### GETリクエスト
```sh
curl --location 'http://localhost:8081/room/'
```
初回であれば，空の配列が返ってくるはずです．

### POSTリクエスト
```sh
curl --location 'http://localhost:8081/room/' \
--form 'name="テストルーム"' \
--form 'description="このルームは，初めて作成したルームです．DRFのテストのため，実行しています．"'
```

実際に変更を確認する際は，GETを実行してみてください．
もしくは，以下のURLに飛んでみてください．
http://localhost:8081/room/


以上で，動作確認を終わります．
