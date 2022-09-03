import random 
print('Có 3 loại bi: bi xanh, bi vàng, bi đỏ nếu bạn chọn cùng đáp án với máy tính bạn sẽ thắng và nếu không chọn đúng thì thua.')
a = input('Bạn sẵn sàng chưa? yes or no : ')
if a == 'yes':
  list =['bi xanh','bi vàng','bi đỏ']
  your_choose = input('Bạn chọn bi nào: ')
  bot_choose = random.choice(list)
  print()
  print('Máy tính chọn:',bot_choose)
  print('Bạn chọn:',your_choose)
  if your_choose == bot_choose:
    print('Yeahhh, bạn thắng rồi !')
  elif your_choose not in list:
    print('Bạn ghi sai rồi !')
  else :
    print('Bạn thua !!')
else:
  print('!!!')