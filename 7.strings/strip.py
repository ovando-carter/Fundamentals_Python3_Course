love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

print("original text:")
print(love_maybe_lines)

empty_list = []
for i in range(len(love_maybe_lines)):
  a = love_maybe_lines[i].strip()
  empty_list.append(a)
  #print(a)
#print()
#print(empty_list)

love_maybe_lines_stripped = empty_list
print()
print("stripped spaces:")
print(love_maybe_lines_stripped)


love_maybe_full = '\n'.join(love_maybe_lines_stripped)
print()
print("each element on its own line:")
print(love_maybe_full)