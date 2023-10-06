import pyautogui

count = int(input())
for i in range(1, count + 1):
    pyautogui.write("#" * i)
    pyautogui.press("enter")


# import pyautogui
# n=int(input())
# for i in range(1, n + 1):
#     pyautogui.write('#' * i)
#     # pyautogui.write('\n')
#     pyautogui.write(['enter'])
