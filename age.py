driving = input('請問你有開過車嗎?')
if driving == '有':
    age = input('請問你的年齡?')
    age = int(age)
    if age >= 18:
        print('開車兜風讚讚讚!')           # 通過檢核
    else:
        print('逼逼逼，警察先生就是他!')    # 未通過檢核	
elif driving == '沒有':
    age = input('請問你的年齡?')
    age = int(age)
    if age >= 18:
        print('怎麼還沒有去考駕照~?我以為你有駕照了欸')           
    else:
        print('再過幾年就可以考駕照了耶')
else:
    print('請輸入 有/沒有 ')                                    	