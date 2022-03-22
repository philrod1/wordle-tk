words_file = open('5k.txt', 'r')
words_list = words_file.read().split(',')
words_file.close()
words_list.sort()