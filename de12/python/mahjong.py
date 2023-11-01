#計算
from mahjong.hand_calculating.hand import HandCalculator
#麻雀牌
from mahjong.tile import TilesConverter
#役, オプションルール
from mahjong.hand_calculating.hand_config import HandConfig, OptionalRules
#鳴き
from mahjong.meld import Meld
#風(場&自)
from mahjong.constants import EAST, SOUTH, WEST, NORTH

#HandCalculator(計算用クラス)のインスタンスを生成
calculator = HandCalculator()

#結果出力用
def print_hand_result(hand_result):
     #翻数, 符数
     print(hand_result.han, hand_result.fu)
     #点数(ツモアガリの場合[左：親失点, 右:子失点], ロンアガリの場合[左:放銃者失点, 右:0])
     print(hand_result.cost['main'], result.cost['additional'])
     #役
     print(hand_result.yaku)
     #符数の詳細
     for fu_item in hand_result.fu_details:
          print(fu_item)
     print('')

#アガリ形(上と同じ)
tiles = TilesConverter.string_to_136_array(honors='55666777' , sou='789' , pin='123')

#アガリ牌(上と同じ)
win_tile = TilesConverter.string_to_136_array(honors='7')[0]

#鳴き(なし)
melds = None

#ドラ(なし)
dora_indicators = None

#オプション(ツモを追加,Falseだとロン)
config = None

#計算
result = calculator.estimate_hand_value(tiles, win_tile, melds, dora_indicators, config)
print_hand_result(result)

