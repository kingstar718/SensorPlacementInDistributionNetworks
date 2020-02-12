import json

# 功能：之前7000+点有模拟错误的，找出来，重新模拟

nodePath = "F:\\水质监测点研究\\2020新开始\\waterQuality7589.json"


def openJson(path):
    with open(path, "r") as f:
        data = json.load(f)
    print(data)


if __name__ == "__main__":
    filePath = "F:\\AWorkSpace\\Python-Learning-Data\\json.json"
    openJson(nodePath)
    pass