#Ning
#19 Sep
#linguistics tp1

words = ["how", "why", "however", "whenver", "never"]

response = ["* "+ word[0:2] + " " + word + "\n" for word in words]
#Interpreter response is in list format: ['* ho how\n', '* wh why\n', '* ho however\n', '* wh whenver\n', '* ne never\n']
#interactive_interpreter.PNG is also attached for reference

modify = ["* " + word[0:2] + " " + word + "\n" if word[0:2]=="wh" else "- " + word[0:2] + " " + word + "\n" for word in words]
#Interpreter response is in list format: ['- ho how\n', '* wh why\n', '- ho however\n', '* wh whenever\n', '- ne never\n']
#interacitve_interpreter_part2.PNG is also attached for reference
