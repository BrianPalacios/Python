#El algoritmo de Luhn es un método utilizado para verificar la validez 
#de números de tarjetas de crédito, números de identificación personal y 
#otros tipos de números de identificación.
#Definir funcion para verificar los numeros de la tarjeta
def verify_card_number(car_number):
    sum_of_odd_digitos = 0
    #car_number = "ABC123" --> print(car_number[::-1])  # Salida: "321CBA"
    card_number_reversed = car_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        #la función int() se utiliza para convertir un valor a un entero 
        #(un número entero sin decimales).
        sum_of_odd_digitos += int(digit)
    
    sum_of_ever_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number//10) + (number%10)
        sum_of_ever_digits += number
    total = sum_of_odd_digitos + sum_of_ever_digits

    return total % 10 == 0

def main():
    card_number = '4111-1111-4555-1146'
    #str.maketrans() se utiliza para crear una tabla de 
    #traducción que elimina los guiones y espacios de una cadena de texto
    card_translation = str.maketrans({'-': '', ' ': ''})
    #translate()se utiliza para reemplazar caracteres en una cadena de texto utilizando 
    #una tabla de traducción.
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

main()