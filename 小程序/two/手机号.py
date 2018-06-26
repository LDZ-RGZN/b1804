phone = input ('请输入您的手机号:')
for i in phone:
    if phone.startswith('1') and len(phone) == 11:
        print ('您输入的是正确的手机号码')
        break
    else:
        print ('您输入的是错误的手机号码')
        break
