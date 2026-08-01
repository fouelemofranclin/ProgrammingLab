def e_palindromo(stringa):

    s = stringa.lower().replace("anna","radar")
    return s == s[::-1]

print(e_palindromo("anna"))

