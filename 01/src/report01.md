# 第01回レポート

## 作成者
- 学籍番号: K24044
- 氏名: 加藤雅士

## 問1
utils.pyのlist_generator_function関数の引数に文字列型の値を指定した．
list_generator_function関数では引数はcountという変数に代入されており，countが使われている20行目で問題が発生する．
発生する問題は，「range関数の引数は整数のint型である必要がある」のに対して，引数に与えた変数countに代入されているのは文字列型です．
その結果，list_generator_function関数がTypeError例外を発生させ，エラー１が表示されます．

## 問2
main.pyのprint_process関数の引数に間違った数値と文字列のペアを指定した．
print_process関数では引数numberと引数fizzbuzz_resultが渡され，それらの整合性をチェックする処理が42行目で実行される．
発生する問題は，「fizzbuzz_resultがnumberに対する正しいFizzBuzzの結果である必要がある」のに対して，引数に与えた数値に対して+2が渡されている．
その結果，print_process関数がValueError例外を発生させ，エラー２が表示されます．