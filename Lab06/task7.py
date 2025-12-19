import os
import csv
from collections import Counter, defaultdict


def task7():
    curr_dir = os.path.dirname(__file__)
    dir_task7 = os.path.join(curr_dir, 'files_task7')
    
    if not os.path.exists(dir_task7):
        os.makedirs(dir_task7)
    
    file_path = os.path.join(dir_task7, 'marks.csv')

    result_path = os.path.join(dir_task7, 'statistics.txt')
    
    students_data = []
    all_marks = []
    question_stats = defaultdict(lambda: {'correct': 0, 'total': 0})
    time_marks = []
    
    try:
        with open(file_path, "r", encoding='utf-8') as f:
            reader = csv.reader(f)
            
            for row_num, row in enumerate(reader, 1):
                if len(row) < 5:
                    continue
                
                try:
                    student_id = row[0]
                    time_str = row[3]
                    mark_str = row[4].replace(',', '.')
                    
                    if mark_str.strip() in ['-', '']:
                        continue
                    
                    mark = float(mark_str)
                    
                    answers = []
                    for x in row[5:]:
                        x_cleaned = x.strip().replace(',', '.')
                        if x_cleaned in ['-', '']:
                            answers.append(0.0)
                        else:
                            answers.append(float(x_cleaned))
                    
                    minutes = int(time_str.split()[0])
                    
                    students_data.append({
                        'id': student_id,
                        'time': minutes,
                        'mark': mark,
                        'answers': answers
                    })
                    
                    all_marks.append(mark)
                    time_marks.append((mark, minutes))
                    
                    for i, answer in enumerate(answers):
                        question_stats[i]['total'] += 1
                        if answer > 0:
                            question_stats[i]['correct'] += 1
                
                except ValueError as e:
                    print(f"Помилка в рядку {row_num}: {e}")
                    continue
        
        if not students_data:
            print("Не знайдено валідних даних студентів у файлі")
            return
        


        student_count = len(students_data)
        mark_distribution = Counter(all_marks)
        
        print("="*70)
        print(f"{'СТАТИСТИКА ТЕСТУВАННЯ':^70}")
        print("="*70)
        print(f"\nКількість студентів: {student_count}")
        
        print("\n" + "-"*70)
        print("РОЗПОДІЛ ОЦІНОК:")
        print("-"*70)
        for mark in sorted(mark_distribution.keys()):
            count = mark_distribution[mark]
            print(f"  {mark:5.2f}: {count:3d} студентів")
        
        print("\n" + "-"*70)
        print("СЕРЕДНЯ ОЦІНКА ЗА ЧАС ВИКОНАННЯ (крок 1 хв):")
        print("-"*70)
        if time_marks:
            min_time = min(t[1] for t in time_marks)
            max_time = max(t[1] for t in time_marks)
            
            for minute in range(min_time, max_time + 1):
                minute_marks = [m[0] for m in time_marks if m[1] == minute]
                if minute_marks:
                    avg_mark = sum(minute_marks) / len(minute_marks)
                    print(f"  {minute:2d} хв: {avg_mark:.2f} (студентів: {len(minute_marks)})")
        
        time_marks.sort(key=lambda xx: xx[0] / xx[1], reverse=True)
        top_5 = time_marks[:5]
        
        print("\n" + "-"*70)
        print("ТОП-5 НАЙКРАЩИХ ОЦІНОК (співвідношення оцінка/час):")
        print("-"*70)
        for i, (mark, time_spent) in enumerate(top_5, 1):
            ratio = mark / time_spent
            print(f"  {i}. Оцінка {mark:.2f} за {time_spent:2d} хв → коефіцієнт: {ratio:.3f}")
        


        with open(result_path, "w", encoding='utf-8') as f:
            f.write("="*70 + "\n")
            f.write(f"{'СТАТИСТИКА ТЕСТУВАННЯ':^70}\n")
            f.write("="*70 + "\n\n")
            
            f.write(f"Кількість студентів: {student_count}\n\n")
            
            f.write("-"*70 + "\n")
            f.write("РОЗПОДІЛ ОЦІНОК:\n")
            f.write("-"*70 + "\n")
            for mark in sorted(mark_distribution.keys()):
                count = mark_distribution[mark]
                f.write(f"  Оцінка {mark:.2f}: {count} студентів\n")
            
            f.write("\n" + "-"*70 + "\n")
            f.write("СТАТИСТИКА ПО ПИТАННЯХ:\n")
            f.write("-"*70 + "\n\n")
            
            for q_num in sorted(question_stats.keys()):
                stats = question_stats[q_num]
                correct = stats['correct']
                total = stats['total']
                correct_percent = (correct / total * 100) if total > 0 else 0
                incorrect_percent = ((total - correct) / total * 100) if total > 0 else 0
                
                f.write(f"Питання {q_num + 1}:\n")
                f.write(f"  Правильних відповідей: {correct} ({correct_percent:.1f}%)\n")
                f.write(f"  Неправильних відповідей: {total - correct} ({incorrect_percent:.1f}%)\n\n")
            

            f.write("-"*70 + "\n")
            f.write("ТОП-5 НАЙКРАЩИХ ОЦІНОК (співвідношення оцінка/час):\n")
            f.write("-"*70 + "\n\n")
            
            for i, (mark, time_spent) in enumerate(top_5, 1):
                ratio = mark / time_spent
                f.write(f"{i}. Оцінка {mark:.2f} за {time_spent} хв (коефіцієнт: {ratio:.3f})\n")
            
            f.write("\n" + "="*70 + "\n")
        
        print("\n" + "="*70)
        print(f"Статистику збережено у файл: {result_path}")
        print("="*70)
    
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")


task7()

