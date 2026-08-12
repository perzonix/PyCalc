from config import OPERATORS, MAX_LENGTH

def format_result(val):
    val = round(val, 3)
    if isinstance(val, float) and val.is_integer():
        return str(int(val))
    return str(val)

def handle_press(symbol, display, history_display):
    current = display.cget('text')

    if len(current) >= MAX_LENGTH and symbol in '0123456789.':
        if current != '0':
            return

    if symbol == 'C':
        display.configure(text='0')
        history_display.configure(text='')
        
    elif symbol == '⌫':   
        new_text = current[:-1]
        if new_text == '-' or not new_text or current == 'Ошибка':
            display.configure(text='0')
        else:
            display.configure(text=new_text)
            
    clean_curr = current
    if current != 'Ошибка':
        while clean_curr and clean_curr[-1] in OPERATORS + ['.']:
            clean_curr = clean_curr[:-1]

    if symbol == 'x²':
        if current != 'Ошибка' and clean_curr:
            try:
                val = eval(clean_curr.replace('x', '*').replace(':', '/').replace('^', '**'))
                history_display.configure(text=f"sqr({clean_curr}) =")
                display.configure(text=format_result(val ** 2))
            except Exception:
                display.configure(text='Ошибка')

    elif symbol == '√':
        if current != 'Ошибка' and clean_curr:
            try:
                val = eval(clean_curr.replace('x', '*').replace(':', '/').replace('^', '**'))
                if val < 0:
                    display.configure(text='Ошибка')
                else:
                    history_display.configure(text=f"√({clean_curr}) =")
                    display.configure(text=format_result(val ** 0.5))
            except Exception:
                display.configure(text='Ошибка')

    elif symbol == '1/x':
        if current != 'Ошибка' and clean_curr:
            try:
                val = eval(clean_curr.replace('x', '*').replace(':', '/').replace('^', '**'))
                if val == 0:
                    display.configure(text='Ошибка')
                else:
                    history_display.configure(text=f"1/({clean_curr}) =")
                    display.configure(text=format_result(1 / val))
            except Exception:
                display.configure(text='Ошибка')

    elif symbol == '+/-':
        if current != 'Ошибка' and current != '0':
            if current.startswith('-'):
                display.configure(text=current[1:])
            else:
                display.configure(text='-' + current)

    elif symbol == '%':
        if current != 'Ошибка' and clean_curr:
            try:
                val = eval(clean_curr.replace('x', '*').replace(':', '/').replace('^', '**'))
                history_display.configure(text=f"{clean_curr}% =")
                display.configure(text=format_result(val / 100))
            except Exception:
                display.configure(text='Ошибка')

    elif symbol == '=':   
        if current == 'Ошибка' or not clean_curr:
            return

        expr = clean_curr.replace('x', '*').replace(':', '/').replace('^', '**')
        try:
            result = eval(expr)
            history_display.configure(text=clean_curr + ' =')
            display.configure(text=format_result(result))
        except Exception:
            display.configure(text='Ошибка')

    elif symbol in OPERATORS:
        if current == 'Ошибка':
            current = '0'
        
        if current[-1] in OPERATORS:
            display.configure(text=current[:-1] + symbol)
        elif current[-1] == '.':
            display.configure(text=current[:-1] + symbol)
        else:
            display.configure(text=current + symbol)

    elif symbol == '.':
        if current == 'Ошибка':
            current = '0'

        if current[-1] in OPERATORS:
            display.configure(text=current + '0.')
            return

        last_number = current.replace('+', ' ').replace('-', ' ').replace('x', ' ').replace(':', ' ').replace('^', ' ').split()[-1] if current else ''
        if '.' not in last_number:
            display.configure(text=current + '.')

    else: # Обработка цифр
        if symbol in ['⌫', 'C', '=', 'x²', '1/x', '√', '+/-']:
            return

        if current == 'Ошибка' or current == '0':
            display.configure(text=symbol)
        else:
            display.configure(text=current + symbol)