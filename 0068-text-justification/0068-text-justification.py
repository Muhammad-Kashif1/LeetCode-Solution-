class Solution(object):
    def fullJustify(self, words, maxWidth):
        result = []
        line = []
        char_count = 0
        
        for word in words:
            if char_count + len(line) + len(word) <= maxWidth:
                line.append(word)
                char_count += len(word)
            else:
                num_spaces = maxWidth - char_count
                if len(line) == 1:
                    result.append(line[0] + ' ' * num_spaces)
                else:
                    num_gaps = len(line) - 1
                    spaces_per_gap = num_spaces // num_gaps
                    extra_spaces = num_spaces % num_gaps
                    justified_line = ''
                    for i in range(len(line) - 1):
                        justified_line += line[i] + ' ' * spaces_per_gap
                        if i < extra_spaces:
                            justified_line += ' '
                    justified_line += line[-1]
                    result.append(justified_line)
                line = [word]
                char_count = len(word)
        
        # Handle the last line (left-justify)
        last_line = ' '.join(line)
        last_line += ' ' * (maxWidth - len(last_line))
        result.append(last_line)
        
        return result
