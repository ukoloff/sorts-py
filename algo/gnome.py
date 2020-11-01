#
# Gnome sort
#
# https://gist.github.com/avolkov/47321a2ef0756b0aaef9
#

def sort(array):
    i = 0
    while i < len(array):
        if i == 0 or array[i-1] <= array[i]:
            i += 1
        else:
            array[i], array[i-1] = array[i-1], array[i]
            i -= 1
