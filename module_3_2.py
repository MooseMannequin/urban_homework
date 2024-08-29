def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    check_a = True
    check_b = True
    given_domains = ['.ru', '.com', '.net']
    if recipient == sender:
        print('Нельзя отправить письмо самому себе!')
        return
    
    
    if '@' in recipient and '@' in sender:
        check_a = True
        #print('success_@')
    else:
        check_a = False
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return
    for domain_check in range(1):
        for domain in given_domains:
            if recipient.endswith(domain):
                check_b = True
                #print('success_recipient')
                break
            else:
                check_b = False
        if check_b == False:    
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
            break
        else:
            for domain in given_domains:
                if sender.endswith(domain):
                    check_b = True
                    #print('success_sender')
                    break
                else:
                    check_b = False
            if check_b == False:    
                print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    
    
    if check_a == True and check_b == True and sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    elif check_a == True and check_b == True and sender != 'university.help@gmail.com':
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email('блабла', 'pepo@mail.net', sender = 'booba@yandex.ru')
print()
send_email('123', 'university.help@gmail.com')
print()
send_email('abc', 'pepo@mail.net')
print()
send_email('123', 'pepo@mail.WOW')