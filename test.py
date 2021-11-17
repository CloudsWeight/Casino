

def run():
    word = ''
    sentence = ''
    print('Please enter some words.')
    print('Include a period (.) when you are finished.')
    while '.' not in word:
        word = input('next word: ')
        sentence = word + ' ' + sentence
    print()
    print('Aha! You said:')
    print(sentence)

if __name__ =="__main__":
    run()
