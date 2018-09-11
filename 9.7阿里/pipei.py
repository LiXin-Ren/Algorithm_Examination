"""
输入:
输入数据包含两行，
第一行，实体列表，多种实体之间用分号隔开，实体名和实体值之间用下划线隔开，多个实体值之间用竖线隔开，所有标点都是英文状态下的，格式如下：
实体名称1_实体值1|实体值2|…;实体名称2_实体值1|实体值2|…;…
第二行，用户的自然语言指令
输出:
被标记了关键词的指令。指令中的关键词前后加一个空格被单独分出来，并在后面跟上"/"+实体名称来标记。如果一个实体值属于多个实体，将这些实体都标记出来，并按照实体名称的字符串顺序正序排列，并以逗号分隔。
输入范例:
singer_周杰|周杰伦|刘德华|王力宏;song_冰雨|北京欢迎你|七里香;actor_周杰伦|孙俪
请播放周杰伦的七里香给我听
输出范例:
请播放 周杰伦/actor,singer 的 七里香/song 给我听
"""
entities = input().split(';')
entityNum = len(entities)
content_name = {}
#name_content = {}
for i in range(entityNum):
    name, contents = entities[i].split('_')
    contents = contents.split('|')
    for content in contents:
        if content not in content_name:
            content_name[content] = [name]
        else:
            content_name[content].append(name)
            content_name[content].sort()

   # name_content[name] = content

question = input()

result = []
i = 0
while i < len(question):
    flag_key = False
    maxLength = 0

    for key in content_name:            #某个词出现在question中
        position_q = i+1
        if question[i] == key[0]:
                      #question index
            j = 1                       #词（key）的index
            while position_q < len(question) and j < len(key):       #对比词有没有完整出现在question中
                if key[j] == question[position_q]:
                    j += 1
                    position_q += 1
                else:
                    break
            if j == len(key):
                if maxLength < j:
                    maxLength = j
                    flag_key = key
    if flag_key != False:
        result.append((i,i+maxLength,flag_key))
    i += (maxLength+1)


outputStr = ''
now = 0
for i in range(len(result)):
    start, end = result[i][0]-now, result[i][1]-now

    outputStr += question[0:start]+' '+question[start:end]+'/'+','.join(content_name[result[i][2]])+' '
    question = question[end:]
    now = end
outputStr += question

print(outputStr)

