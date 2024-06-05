# import threading
# from pathlib import Path

# def vowels_file(filepath):
#     unlilar = 'AEIOUaeiou'
#     sanoq = 0
#     with open(filepath, 'r') as file:
#         for line in file:
#             count += sum(1 for char in line if char in unlilar)
#     print(f"{filepath}: {sanoq} ta unli harf")

# def txt_files():
#     txt_files = Path('.').glob('*.txt') 
#     threads = []

#     for filepath in txt_files:
#         thread = threading.Thread(target=vowels_file, args=(filepath,))
#         threads.append(thread)
#         thread.start()

#     for thread in threads:
#         thread.join()

# if __name__ == "__main__":
#     txt_files()
# ozgina tushunish qiyin bo'ldi


