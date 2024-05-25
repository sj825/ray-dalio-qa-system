import json
from fuzzywuzzy import fuzz

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def find_best_match(question, data):
    best_match = None
    highest_score = 0
    for item in data:
        score = fuzz.ratio(question, item['question'])
        if score > highest_score:
            highest_score = score
            best_match = item
    return best_match

def main():
    life_data = load_data('qa_data_life.json')
    work_data = load_data('qa_data_work.json')

    while True:
        user_question = input("질문을 입력하세요 (종료하려면 'exit' 입력): ")
        if user_question.lower() == 'exit':
            break

        best_match_life = find_best_match(user_question, life_data)
        best_match_work = find_best_match(user_question, work_data)

        if best_match_life and (not best_match_work or best_match_life['score'] > best_match_work['score']):
            print("인생 원칙에서의 답변:")
            print(best_match_life['answer'])
        elif best_match_work:
            print("일의 원칙에서의 답변:")
            print(best_match_work['answer'])
        else:
            print("적합한 답변을 찾을 수 없습니다.")

if __name__ == "__main__":
    main()
