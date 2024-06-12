from deeppavlov import configs, build_model
import request
import re

def find(question, model):
    if question != "":
        
        result = ''
        number = ""
        
        with open("number.txt", encoding="utf-8") as file:
            for item in file:
                number += item

        with open(f"data//{number}//main.txt", encoding="utf-8") as file:
            for item in file:
                result += item

        answer = model([result], [question])
        text = f"Отвечает ли: {answer[0]}, на вопрос: {question}"

        text_answer = request.request_gpt(text)
        
        answer = ' '.join(answer[0])

        print(text_answer)

        if "Да" in text_answer:
            return answer[0].upper() + answer[1:]
        
        elif "Нет" in text_answer:
            result = ""
            with open(f"data//{number}//reduced.txt", encoding="utf-8") as file:
                for item in file:
                    result += item

            answer = request.request_gpt(f"{result} /n Найди в этом тексте ответ на этот вопрос: {question}")
            answer = re.sub(r'\.[^./]+?$', '', answer)
            if not "нет ответа на вопрос" or "не указано" in answer:
                return answer  
            else:
                return f"К сожалению, я не смогу ответить на этот вопрос."
        else:
            return f"К сожалению, я не смогу ответить на этот вопрос."
    else:
        return 0

