# create_gif_image
時系列データのプロットをデータ渡せば勝手にやってくれる奴

## Plotlyのレイアウト設定に関して
基本的には公式リファレンスを読めばいい(https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html)

XAxisのscaleanchor='y'で軸の比が1対1になる。
titleとかannotationの設定のx,yはx軸y軸を1の長さと見なしたときの値を入れる。端に文字を置きたい場合はannotationでx=0.03,y=0.03とか設定すればいい。
plotlyはデータ量が多くなりすぎるとめちゃくちゃ表示が重くなるから画像で出力してしまう方がいいかもしれない。