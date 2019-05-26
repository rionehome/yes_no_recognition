# yes_no_recognition
## Overview
「Yes」と「No」のみの音声認識のパッケージです。

## Setup
【PocketSphinx】  
`git clone https://github.com/cmusphinx/pocketsphinx-python.git`

`sudo apt-get install -y python python-dev python-pip build-essential swig git libpulse-dev`

`sudo pip install pocketsphinx`

`sudo apt-get install -y libttspico-utils`

【Julius(英語版)】  
https://sourceforge.net/projects/juliusmodels/files/  
このサイトのENVR-v5.4.Dnn.Bin.zipをダウンロードして展開する  

## Description
recognition.pyは**PocketSphinx**での音声認識のコードです。  
recognition_english_julius.pyは**Julius**(英語版)での音声認識のコードです。  
subscriber.pyは認識結果の表示と音声認識再開のテスト用のコードです。  

## Usage
* PockeSphinxを音声認識に使う場合

```
roslaunch yes_no_recognition yes_no_recognition.launch
```

* Julius(英語版)を音声認識に使う場合  
`/yes_no_recognition/src/dictionary/yes_no_julius.dict`を単語辞書にしてモジュールモードでJuliusを起動する。

```
roslaunch yes_no_recognition yes_no_recognition_julius_english.launch
````

* 上のどちらかのコマンドを実行し、`recognition_start`にBool型のメッセージ(True)を投げると音声認識が開始する。

## Node
**`name` recognition**

**`name` recognition_julius_english**

### Subscribe Topic

* **`recognition_start`** 音声認識開始と停止の受け取り（ std_msgs/Bool ）

True：音声認識　開始  
False:音声認識　停止

### Publish Topic

* **`recognition_result`** 音声認識結果 ( std_msgs/String )

## Node
**`name` subscriber**

### Subscribe Topic
* **`recognition_result`** 音声認識結果の受け取り（ std_msgs/String ）

### Publish Topic
* **`recognition_start`** 音声認識再開 ( std_msgs/Bool )

True：音声認識　開始  
False:音声認識　停止

