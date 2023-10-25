# ＝＝＝＝＝for文＝＝＝＝＝
for i in range(1,4):
    print(i,"人目")

    # 文字にはダブルクォーテーションをつけるよ！！！
    name=input("名前を教えてね")
    waist=float(input("腹囲は？"))
    age=int(input("年齢は？"))

    print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")

    # ＝＝＝＝＝if文＝＝＝＝＝

    if waist>=85:
        print(name,"さん、内臓脂肪蓄積要注意です")
    else:
        if waist<=45:
                print(name,"さん、瘦せすぎです")
        else:print(name,"さん、腹囲は問題ありません")
        
        if age>=40 and waist>=85:
            print(name,"さん、内臓脂肪蓄積要注意です")