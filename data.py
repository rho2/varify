raw_data = [
( "vs code", "ubuntu", "python", "spaces", "none", "human"), 
( "none", "Windows", "python", "tabs", "Tesla", "human"), 
( "eclipse", "windows", "java", "tabs", "maceratti", "human"), 
( "eclipse", "macos", "java", "spaces", "bmw", "algo"), 
( "eclipse", "windows", "java", "tabs", "tesla", "human"), 
( "intelliJ", "windows", "java", "tabs", "none", "human"), 
( "eclipse", "windows", "java", "-", "tesla", "mesch"), 
( "vs code", "windows", "c", "tabs", "chevrolet", "human"), 
( "intelliJ", "ubuntu", "java", "spaces", "bmw", "human"), 
( "eclipse", "macos", "c++", "tab", "tesla", "Human"), 
( "pycharm", "ubuntu", "python", "tabs", "diaca", "human"), 
( "vs code", "windows", "python", "tabs", "audi", "human"), 
( "eclipse", "windows", "python", "tabs", "vW", "algorithm"), 
( "vim", "ubuntu", "python", "tabs", "rolls royce", "human"), 
( "vs code", "windows", "java", "both", "aston martin", "algo"), 
( "intelliJ", "macos", "java", "tabs", "BMW", "Human"), 
( "vs code", "windows", "java", "tabs", "mercedes", "human"), 
( "vs code", "arch  Linux", "java", "tabs", "Mercedes", "Human"), 
( "vs code", "windows", "python", "tabs", "Volvo", "combined"), 
( "vim", "debian", "python", "spaces", "tesla", "human"), 
( "vs code", "windows", "python", "tabs", "none", "human"), 
( "jetbrains", "macos", "java", "both", "audi", "perh"), 
( "vs code", "macos", "python", "tabs", "alfa romero", "human"), 
( "vs code", "macos", "python", "spaces", "toyota", "human"), 
( "sublime text", "windows", "java", "tabs", "lexus", "human"), 
( "sublime text", "windows", "python", "tabs", "mini", "algorithm"), 
( "intelliJ", "fedora, windows", "javascript", "spaces", "vw", "human"), 
( "nano", "manjaro", "php", "spaces", "Ford", "Human")]

human_data = [
[" 1.0", "1.0", "0.5",  "0.5"],
[" 1.0", "1.0", "0.5",  "0.5"],
 ["1.0", "1.0", "1.0",  "0.0"], 
 ["1.0", "1.0", "0.0",  "1.0"], 
[" 1.0", "1.0", "0.0",  "0.5"],
 ["1.0", "1.0", "0.0",  "1.0"], 
[" 1.0", "0.5", "0.0",  "0.5"],
 ["1.0", "1.0", "0.0",  "1.0"], 
 ["0.5", "1.0", "0.5",  "1.0"], 
[" 1.0", "0.5", "0.0",  "0.5"],
[" 1.0", "1.0", "0.0",  "0.5"],
[" 1.0", "0.5", "0.5",  "0.5"],
[" 1.0", "1.0", "0.0",  "0.0"],
[" 0.5", "0.5", "0.0",  "0.5"],
[" 1.0", "1.0", "0.0",  "0.5"],
[" 1.0", "1.0", "0.0",  "0.5"],
[" 0.5", "1.0", "0.0",  "0.5"],
[" 1.0", "1.0", "0.0",  "1.0"],
 ["1.0", "1.0", "0.0",  "1.0"], 
[" 1.0", "0.5", "0.0",  "0.5"],
 ["0.5", "1.0", "0.0",  "0.0"], 
[" 0.0", "1.0", "0.0",  "0.5"],
 ["1.0", "0.0", "0.5",  "0.0"], 
[" 1.0", "1.0", "0.5",  "0.5"],
 ["1.0", "1.0", "0.5",  "1.0"], 
 ["1.0", "1.0", "0.5",  "1.0"], 
 ["1.0", "1.0", "0.5",  "1.0"], 
[" 1.0", "1.0", "0.0",  "1.0"],
]


out_raw =[
[4.7, 4.8 ,3.2 , 5 , 4.0], 
[5.5, 5.3 ,5.6 , 4.7 , 2.9], 
[5.1, 4.8 ,4.3 , 5.1 , 3.5], 
[5.1, 5 ,4 , 5.1 , 5], 
[4.1, 4.8 ,3.3 , 4 , 5], 
[4.6, 4.3 ,3.6 , 4.8 , 3.6], 
[4.33, 3.67 ,6.67 , 4.33 , 3.0], 
[5.0, 3.33 ,5.33 , 6.0 , 2.0], 
[6.0, 5.67 ,6.0 , 5.33 , 2.0], 
[3.0, 4.0 ,3.67 , 5.67 , 3.33], 
[5.0, 4.33 ,2.33 , 4.33 , 2.33], 
[6.0, 6.0 ,6.67 , 5.0 , 7.0], 
[5.67, 6.0 ,2.67 , 6.0 , 2.0], 
[5.67, 5.33 ,2.67 , 4.0 , 3.67], 
[4.33, 4.0 ,3.67 , 6.33 , 2.0], 
[5.67, 5.33 ,2.67 , 5.67 , 4.67], 
[5.67, 4.33 ,4.0 , 5.33 , 2.67], 
[6.0, 4.33 ,5.33 , 6.0 , 3.0], 
[5.67, 5.67 ,4.67 , 7.0 , 5.0], 
[6.33, 3.0 ,2.33 , 4.0 , 2.67], 
[5.0, 5.0 ,4.67 , 6.33 , 5.0], 
[6.0, 6.33 ,4.67 , 6.0 , 1.67], 
[4.33, 5.33 ,3.0 , 6.67 , 5.67], 
[3.33, 3.67 ,5.33 , 4.67 , 4.67], 
[6.67, 4.0 ,2.33 , 4.33 , 6.0], 
[4.67, 4.67 ,4.33 , 5.33 , 4.67], 
[6.33, 5.33 ,3.33 , 6.33 , 2.33], 
[3.33, 3.67 ,2.67 , 5.33 , 3.33], 
]

out_norm = []

for a in out_raw:
    l = []
    for b in a:
        l.append((b-1.0) / 6.0)
    out_norm.append(l)

editors = []
oss = []
languages = []
cars = []

for editor, used_os, language, tvs, car, hva in raw_data:
    editors.append(editor.lower())
    oss.append(used_os.lower())
    languages.append(language.lower())
    cars.append(car.lower())

editor_dict = {w: wi for wi, w in enumerate(sorted(editors))}
oss_dict = {w: wi for wi, w in enumerate(sorted(oss))}
languages_dict = {w: wi for wi, w in enumerate(sorted(languages))}
cars_dict = {w: wi for wi, w in enumerate(sorted(cars))}

dataset_easy = []
for editor, used_os, language, tvs, car, hva in raw_data:
    
    elem = []
    editor_hot = [0] * len(editors)
    editor_hot[editor_dict[editor.lower()]] = 1
    elem += editor_hot

    oss_hot = [0] * len(oss)
    oss_hot[oss_dict[used_os.lower()]] = 1
    elem += oss_hot

    lang_hot = [0] * len(languages)
    lang_hot[languages_dict[language.lower()]] = 1
    elem += lang_hot

    car_hot = [0] * len(cars)
    car_hot[cars_dict[car.lower()]] = 1
    elem += car_hot

    choice_indent = tvs.lower() == "tabs"
    choice_employ = hva.lower() == "human"

    elem.append(choice_indent)
    elem.append(choice_employ)

    dataset_easy.append(elem)
