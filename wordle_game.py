import re

class Wordle:

    def get_matches(self, word: str, values: list, words: list):
        regex = self.result_to_regex(word, values)
        pattern = re.compile(regex)
        return [word for word in words if pattern.match(word)]

    def result_to_regex(self, guess: str, result: list):
        regex = ''
        template = '\)%c|\]%c|\.%c|\w%c|%c\w'
        for i in [0,1,2,3,4]:
            match result[i]:
                case 1:
                    regex += '[^' + guess[i] + ']'
                    if '(?=.*' + guess[i] + ')' not in regex:
                        regex = '(?=.*' + guess[i] + ')' + regex
                case 2:
                    regex += guess[i]
                    if '(?!.*' + guess[i] + ')' in regex:
                        regex = regex.replace('(?!.*' + guess[i] + ')', '')
                case _:
                    pattern = re.compile(template % (guess[i], guess[i], guess[i], guess[i], guess[i]))
                    if not (re.search(pattern, regex) or regex.endswith(guess[i])):
                        regex = '(?!.*' + guess[i] + ')' + regex
                    regex  += '[^' + guess[i] + ']'
            if '(?!.*' + guess[i] + ')' in regex and '(?=.*' + guess[i] + ')' in regex:
                regex = regex.replace('(?!.*' + guess[i] + ')', '')
        return '^' + regex + '$'