print('你走进了一个山洞，听到了一个声音')

boyOrGirl = input("我的眼瞎了，ARE YOU A BOY or GIRL (B|G):")

if boyOrGirl == 'B' or boyOrGirl == 'b':
    print("你好啊 小男孩")
else:
    print("你好啊 小姑娘")
    
    
name = input('WHAT IS YOUR NAME:')
print(name, "很好很好")

print("我就是传说中的蟒蛇神，大家也叫我python，或者拍神，我被困在瓶子里面，已经1000年了")

yesOrNo = input("如果你帮我打开瓶盖，我可以满足你三个愿望，打开吗(Y|N):")
if yesOrNo == 'Y' or yesOrNo == 'y':
    print("终于自由了，肚子好饿呀")
    i = 1
    while i <= 3:
        print("说吧，告诉我你的第",i,"个愿望是什么")
        wish = input(":")
        print("简单!")
        print("你的愿望["+wish+"]实现了")
        i = i + 1
else:
    print ("你会后悔的")
    
