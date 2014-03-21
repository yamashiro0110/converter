converter
======================

ログファイルをCSVに変換する<br>
> Python2.7推奨

## Install

```
git clone https://github.com/yamashiro-r/converter.git
```

## Usage

```
cd $INSTALL_DIR
python _run_convert.py $LOG_FILE_PATH $LOG_FORMAT $OUT_PUT_CSV_PATH
```

* LOG_FILE_PATH
    * 読み込むログファイルのパス
* LOG_FORMAT
    * 読み込むログファイルのフォーマット
* OUT_PUT_CSV_PATH
    * CSVに変換したログの出力先

> Ex

* ディレクトリ構成
```
$ ls -1
LICENSE
README.md
_run_convert.py
logs
src
```

<br>

* 読み込むファイル
    * Apacheのcombinedを例にします

```
$ cat logs/access_log
192.168.0.11 - - [18/Mar/2014:00:14:45 +0900] "GET /html/test.html HTTP/1.1" 200 271 "-" "python-requests/2.2.1 CPython/2.7.5 Darwin/13.1.0"
192.168.0.11 - - [18/Mar/2014:01:42:24 +0900] "GET /html/test.html HTTP/1.1" 200 271 "-" "python-requests/2.2.1 CPython/2.7.5 Darwin/13.1.0"
192.168.0.11 - - [18/Mar/2014:01:49:57 +0900] "GET /html/test.html HTTP/1.1" 200 271 "-" "python-requests/2.2.1 CPython/2.7.5 Darwin/13.1.0"
```

<br>

* スクリプト実行

```
$ python _run_convert.py logs/access.log combined logs/access.csv
```

<br>

* 変換したログを出力したファイル

```
$ cat logs/access.csv
"192.168.0.11","-","-","18/Mar/2014:02:06:05","GET","/html/test.html","HTTP/1.1","200","271","-","python-requests/2.2.1 CPython/2.7.5 Darwin/13.1.0"
"192.168.0.11","-","-","18/Mar/2014:02:09:22","GET","/html/test.html","HTTP/1.1","200","271","-","python-requests/2.2.1 CPython/2.7.5 Darwin/13.1.0"
"192.168.0.11","-","-","18/Mar/2014:02:18:53","GET","/html/test.html","HTTP/1.1","200","271","-","python-requests/2.2.1 CPython/2.7.5 Darwin/13.1.0"
```

## LICENSE

The MIT License (MIT)

Copyright (c) 2014 yamashiro-r

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
