def escreva(palavra):
    print('\033[1;33m*'* len(palavra))
    print(palavra)
    print('*'* len(palavra))

print()
escreva('Hoje está chovendo!')
