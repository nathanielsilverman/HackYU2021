dict = {}

def map_update(dict, st, emoji):
    sa = st.split()
    emoarray = emoji.split()
    for i in range(len(sa)):
        if sa[i] == emoarray[i]:
            continue
        else:
            dict[sa[i]] = emoarray[i]


def main():
    global dict
    map_update(dict,
               "She counted. One. She could hear the steps coming closer. Two. Puffs of breath could be seen coming from his mouth. Three. He stopped beside her. Four. She pulled the trigger of the gun.",
               "๐ค๐ฉ counted. 1๏ธโฃ. ๐ค๐ฉ could ๐๏ธ the ๐ช โคต๏ธ closer. 2๏ธโฃ. Puffs of ๐ซ could be ๐ โคต๏ธ from ๐ค๐จโฌ๏ธ ๐. 3๏ธโฃ. ๐ค๐จ ๐ beside ๐ค๐ฉโฌ๏ธ. 4๏ธโฃ. ๐ค๐ฉ pulled the trigger of the ๐ซ.")
    map_update(dict, "The red glint of paint sparkled under the sun. He had dreamed of owning this car since he was ten, and that dream had become a reality less than a year ago. It was his baby and he spent hours caring for it, pampering it, and fondling over it. She knew this all too well, and that's exactly why she had taken a sludge hammer to it.", "The ๐ด glint of paint sparkled under the โ๏ธ. ๐ค๐จ had dreamed of owning this ๐๏ธ since ๐ค๐จ was ten, โ that dream had become a reality less than a year ago. It was ๐ค๐จโฌ๏ธ ๐ถ โ ๐ค๐จ spent ยฐ ๐๏ธ for it, pampering it, โ fondling over it. ๐ค๐ฉ ๐ก this all too well, โ that's โก โ๏ธ ๐ค๐ฉ had taken a sludge ๐จ to it.")
    map_update(dict, "You can decide what you want to do in life, but I suggest doing something that creates. Something that leaves a tangible thing once you're done. That way even after you're gone, you will still live on in the things you created.", "โก๏ธ๐ค ๐ฅซ decide what โก๏ธ๐ค ๐ to do in ๐งฌ, but I suggest doing something that creates. Something that ๐ a tangible thing ๐ you're โ๏ธ. That way even after you're โก๏ธ, โก๏ธ๐ค will still live on in the things โก๏ธ๐ค created.")
    map_update(dict, "area book business case child company country day eye fact family government group hand home job life lot man money month mother Mr night number part people place point problem program question right room school state story student study system thing time waterway week woman word work world year", "area ๐๏ธ ๐งโ๐ผ case ๐ง company country day ๐๏ธ fact ๐ช๏ธ government group โ ๐?๏ธ job ๐งฌ lot ๐ค๐จ ๐ธ month ๐คถ Mr ๐ number ยง ๐ฅ place ๐๏ธ problem program โ๏ธ โก๏ธ room ๐ซ state story ๐จโ๐๏ธ study system thing โฑ๏ธ waterway week ๐ค๐ฉ word โ๏ธ ๐บ๏ธ year")
    map_update(dict, "cat dog mouse elephant tiger water bottle cup beer wine cookies cookie folder folders candy party parties balloons balloon", "๐ฑ ๐ถ ๐ญ ๐ ๐ฏ ๐ ๐พ ๐ฅค ๐บ ๐ท ๐ช ๐ช ๐ ๐ ๐ฌ ๐ ๐ฏโโ๏ธ ๐ ๐")
    map_update(dict, "beach sea boat house pizza fish dolphin war sword duck chicken home building school girl boy face ear nose eye eyes", "๐๏ธ โต๏ธ ๐ฅ๏ธ ๐๏ธ ๐ ๐ฃ ๐ฌ war ๐คบ ๐ฆ ๐ ๐?๏ธ ๐ข ๐ซ ๐ง ๐ฆ ๐ ๐๏ธ ๐ ๐๏ธ ๐")

