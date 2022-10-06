import json
import os
from urllib.request import urlretrieve


def get_content(line, substr_begin, substr_end):
    list = []
    start = 0
    end = 0

    while end != -1:
        start = line.find(substr_begin, start)
        end = line.find(substr_end, start)
        if end >= 0:
            list.append(line[start + len(substr_begin):end])
            start = end

    return list


def get_json(line):
    nesting = 0
    start = 0
    end = 0

    for i in range(len(line) - 1):
        if line[i] == '{':
            if nesting == 0:
                start = i
            nesting += 1

        elif line[i] == '}':
            nesting -= 1
            if nesting == 0:
                end = i
                return line[start:end + 1]


def get_file(url, path):
    urlretrieve(url, path)


path = "/home/niki/Рабочий стол/Course/input_txt"
substr_begin = '<script> (function(document, player)'
substr_end = '</script>'

for dirpath, dirnames, filenames in os.walk(path):

    for file in filenames:

        if file.endswith('.txt'):

            file_path = os.path.join(dirpath, file)

            with open(file_path, 'r') as f:

                line = f.read()
                content = get_content(line, substr_begin, substr_end)
                json_line = get_json(content[0][content[0].find('{') + 1:])
                json_file = json.loads(json_line)

                url = None
                flag_fps = 0
                flag_quality = ""
                for v in json_file["request"]["files"]["progressive"]:

                    if v["quality"] == "1080p":

                        flag_quality = "1080p"
                        if v["fps"] == 60:
                            flag_fps = 60
                            url = v["url"]
                            break
                        elif v["fps"] == 30:
                            flag_fps = 30
                            url = v["url"]
                            continue
                        elif v["fps"] == 25 and flag_fps != 30:
                            flag_fps = 25
                            url = v["url"]
                            continue
                        elif v["fps"] == 15 and flag_fps != 25:
                            flag_fps = 15
                            url = v["url"]
                            continue
                        elif int(v["fps"]) > flag_fps:
                            flag_fps = int(v["fps"])
                            url = v["url"]
                            continue

                    elif v["quality"] == "720p":

                        if flag_quality != "1080p":
                            flag_quality = "720p"
                            if v["fps"] == 60:
                                flag_fps = 60
                                url = v["url"]
                                continue
                            elif v["fps"] == 30 and flag_fps != 60:
                                flag_fps = 30
                                url = v["url"]
                                continue
                            elif v["fps"] == 25 and flag_fps != 30:
                                flag_fps = 25
                                url = v["url"]
                                continue
                            elif int(v["fps"]) > flag_fps:
                                flag_fps = int(v["fps"])
                                url = v["url"]
                                continue

                file = file.split('.')[0]
                file = file + '.mp4'
                get_file(url, os.path.join("/home/niki/Рабочий стол/Course/", file))
