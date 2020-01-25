# 문자 -> 숫자 -> 벡터
# 문자를 Vector로 바꾸는 방법 : One-hot Encoding
# 하나의 단어를 Vector로 인식, 단어 존재시 1 없으면 0
# Bag of words
# 단어별로 인덱스를 부여해서, 한 문장(또는 문서)의 단어의 개수를 Vector로 표현

import os

# 폴더명을 입력하면 해당 폴더 안의 파일들을 가져온
def get_file_list(dir_name):
    return os.listdir(dir_name)

def get_contents(file_list):
    y_class = []
    X_text = []
    class_dict = {
        1: "0", 2: "0", 3: "0", 4: "0", 5: "1", 6: "1", 7: "1", 8: "1" }

    for file_name in file_list:
        try:
            f = open(file_name, "r", encoding = "cp949")
            category = int(file_name.split(os.sup)[1].split("_")[0])
            y_class.append(class_dict[category])
            X_text.append(f.read())
            f.close()
        except UnicodeDecodeError as e:
            print(e)
            print(file_name)
    return X_text, y_class

if __name__ == "__main__":
    dir_name = "news_data"
    file_list = get_file_list(dir_name)
    file_list = [os.path.join(dir_name, file_name) for file_name in file_list]
