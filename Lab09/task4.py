import csv
import os
import matplotlib.pyplot as plt


class KmrCsv:
    ref = None
    num = None

    def set_ref(self, ref):
        if ref is not None and not isinstance(ref, str):
            raise TypeError("ref (шлях до CSV) має бути рядком або None")
        self.ref = ref

    def get_ref(self):
        return self.ref

    def set_num(self, num):
        if not isinstance(num, (int, str)):
            raise TypeError("num (номер КМР) має бути цілим числом або рядком")
        self.num = num

    def get_num(self):
        return self.num

    # Читає дані з CSV файлу і повертає їх у вигляді списку
    def read_csv(self):
        if self.ref is None:
            return None
        if not isinstance(self.ref, str) or not self.ref.strip():
            return None
        if not os.path.exists(self.ref):
            print(f"Помилка: файл '{self.ref}' не існує")
            return None
        data = []
        try:
            with open(self.ref, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    data.append(row)
        except (OSError, csv.Error) as e:
            print(f"Помилка читання CSV файлу '{self.ref}': {e}")
            return None
        return data

    # Виводить інформацію про файл: номер КМР і кількість студентів
    def info(self):
        data = self.read_csv()
        if data is None:
            print("Файл не встановлено")
            return
        student_count = len(data) if data else 0
        print(f"Номер КМР: {self.num}")
        print(f"Кількість студентів, що виконали КМР: {student_count}")


class Statistic:
    # Визначає відсотки правильних відповідей на кожне питання серед усіх студентів
    def avg_stat(self, data):
        if not isinstance(data, list) or len(data) == 0:
            return tuple()
        if not data[0] or len(data[0]) < 5:
            return tuple()
        question_count = len(data[0]) - 5
        if question_count <= 0:
            return tuple()
        correct_counts = [0] * question_count
        total_students = len(data)
        for row in data:
            for i in range(question_count):
                if i + 5 < len(row):
                    try:
                        score = float(row[i + 5].replace(',', '.').strip('"'))
                        if score > 0:
                            correct_counts[i] += 1
                    except (ValueError, IndexError):
                        pass
        percentages = tuple((count / total_students * 100) if total_students > 0 else 0 for count in correct_counts)
        return percentages

    # Визначає яку оцінку набрала відповідна кількість студентів
    def marks_stat(self, data):
        if not isinstance(data, list) or len(data) == 0:
            return {}
        marks = {}
        for row in data:
            if len(row) >= 5:
                try:
                    mark = float(row[4].replace(',', '.').strip('"'))
                    mark = round(mark, 2)
                    marks[mark] = marks.get(mark, 0) + 1
                except (ValueError, IndexError):
                    pass
        return marks

    # Визначає який середній бал за хвилину набирав студент під час виконання КМР
    def marks_per_time(self, data):
        if not isinstance(data, list) or len(data) == 0:
            return {}
        result = {}
        for row in data:
            if len(row) >= 5:
                try:
                    student_id = row[0]
                    mark = float(row[4].replace(',', '.').strip('"'))
                    time_str = row[3]
                    minutes = self._parse_time(time_str)
                    if minutes > 0:
                        result[student_id] = mark / minutes
                    else:
                        result[student_id] = 0
                except (ValueError, IndexError):
                    pass
        return result

    def _parse_time(self, time_str):
        try:
            if time_str is None:
                return 0
            if 'хв' in time_str:
                parts = time_str.split('хв')
                minutes = int(parts[0].strip())
                if len(parts) > 1 and 'сек' in parts[1]:
                    seconds = int(parts[1].split('сек')[0].strip())
                    minutes += seconds / 60
                return minutes
            return 0
        except (ValueError, AttributeError):
            return 0

    # Формує п'ять найкращих результатів середніх балів за хвилину для вибірки в заданих межах
    def best_marks_per_time(self, data, bottom_margin, top_margin):
        if not isinstance(data, list) or len(data) == 0:
            return tuple()
        if not isinstance(bottom_margin, (int, float)) or not isinstance(top_margin, (int, float)):
            raise ValueError("Межі мають бути числами")
        if bottom_margin > top_margin:
            bottom_margin, top_margin = top_margin, bottom_margin

        marks_per_time_dict = self.marks_per_time(data)
        filtered = {}
        for row in data:
            if len(row) >= 5:
                try:
                    student_id = row[0]
                    mark = float(row[4].replace(',', '.').strip('"'))
                    if bottom_margin <= mark <= top_margin and student_id in marks_per_time_dict:
                        filtered[student_id] = (mark, marks_per_time_dict[student_id])
                except (ValueError, IndexError):
                    pass
        sorted_items = sorted(filtered.items(), key=lambda x: x[1][1], reverse=True)
        top_5 = sorted_items[:5]
        return tuple((student_id, mark, avg_per_min) for student_id, (mark, avg_per_min) in top_5)


class Plots:
    def __init__(self):
        self._cat = None

    # Встановлює каталог для збереження графіків
    def set_cat(self, cat):
        if cat is None:
            self._cat = None
            return
        if not isinstance(cat, str) or not cat.strip():
            raise ValueError("Каталог для збереження графіків має бути непорожнім рядком або None")
        self._cat = cat.strip()
        if not os.path.exists(self._cat):
            os.makedirs(self._cat, exist_ok=True)

    # Формує гістограму відсотків правильних відповідей на кожне питання
    def avg_plot(self, percentages):
        if not percentages:
            return
        plt.figure(figsize=(10, 6))
        questions = [f"Питання {i+1}" for i in range(len(percentages))]
        plt.bar(questions, percentages)
        plt.xlabel('Питання')
        plt.ylabel('Відсоток правильних відповідей (%)')
        plt.title('Відсотки правильних відповідей на кожне питання')
        plt.xticks(rotation=45)
        plt.tight_layout()
        filename = os.path.join(self._cat, 'avg_plot.png') if self._cat else 'avg_plot.png'
        plt.savefig(filename)
        plt.close()

    # Формує гістограму розподілу оцінок за кількістю студентів
    def marks_plot(self, marks_dict):
        if not marks_dict:
            return
        plt.figure(figsize=(10, 6))
        marks = sorted(marks_dict.keys())
        counts = [marks_dict[mark] for mark in marks]
        plt.bar([str(m) for m in marks], counts)
        plt.xlabel('Оцінка')
        plt.ylabel('Кількість студентів')
        plt.title('Розподіл оцінок')
        plt.tight_layout()
        filename = os.path.join(self._cat, 'marks_plot.png') if self._cat else 'marks_plot.png'
        plt.savefig(filename)
        plt.close()

    # Формує гістограму для п'яти найкращих результатів середніх балів за хвилину
    def best_marks_plot(self, best_marks):
        if not best_marks:
            return
        if not isinstance(best_marks, (list, tuple)):
            return
        try:
            student_ids = [item[0][:8] + '...' if len(str(item[0])) > 8 else str(item[0]) for item in best_marks if len(item) >= 3]
            avg_per_min = [item[2] for item in best_marks if len(item) >= 3]
            if not student_ids or not avg_per_min:
                return
        except (IndexError, TypeError):
            return
        plt.figure(figsize=(10, 6))
        plt.bar(student_ids, avg_per_min)
        plt.xlabel('ID студента')
        plt.ylabel('Середній бал за хвилину')
        plt.title('Топ-5 найкращих результатів середніх балів за хвилину')
        plt.xticks(rotation=45)
        plt.tight_layout()
        filename = os.path.join(self._cat, 'best_marks_plot.png') if self._cat else 'best_marks_plot.png'
        plt.savefig(filename)
        plt.close()


class KmrWork(KmrCsv, Statistic, Plots):
    kmrs = {}
    cat = "results"

    def __init__(self, ref, num):
        KmrCsv.__init__(self)
        Plots.__init__(self)
        self.set_ref(ref)
        self.set_num(num)
        KmrWork.kmrs[self.num] = self.ref
        self.set_cat(KmrWork.cat)

    # Порівнює статистику двох КМР: кількість виконаних, середній бал, середній час
    def compare_csv(self, other_num):
        if self.num not in KmrWork.kmrs or other_num not in KmrWork.kmrs:
            print("Один з КМР не зареєстрований")
            return
        
        data1 = self.read_csv()
        if data1 is None:
            print("Помилка: не вдалося прочитати дані першого КМР")
            return
        
        other_kmr = KmrCsv()
        other_kmr.set_ref(KmrWork.kmrs[other_num])
        other_kmr.set_num(other_num)
        data2 = other_kmr.read_csv()
        if data2 is None:
            print("Помилка: не вдалося прочитати дані другого КМР")
            return
        
        count1 = len(data1) if data1 else 0
        count2 = len(data2) if data2 else 0
        avg1 = self._calculate_avg_mark(data1)
        avg2 = self._calculate_avg_mark(data2)
        avg_time1 = self._calculate_avg_time(data1)
        avg_time2 = self._calculate_avg_time(data2)
        result = f"Порівняння КМР {self.num} та КМР {other_num}:\n"
        result += f"КМР {self.num}: кількість виконаних - {count1}, середній бал - {avg1:.2f}, середній час - {avg_time1:.2f} хв\n"
        result += f"КМР {other_num}: кількість виконаних - {count2}, середній бал - {avg2:.2f}, середній час - {avg_time2:.2f} хв\n"
        print(result)
        filename = os.path.join(self.cat, f'compare_{self.num}_vs_{other_num}.txt')
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(result)
        except (OSError, IOError) as e:
            print(f"Помилка запису файлу '{filename}': {e}")

    def _calculate_avg_mark(self, data):
        if not data or len(data) == 0:
            return 0
        total = 0
        count = 0
        for row in data:
            if len(row) >= 5:
                try:
                    mark = float(row[4].replace(',', '.').strip('"'))
                    total += mark
                    count += 1
                except (ValueError, IndexError):
                    pass
        return total / count if count > 0 else 0

    def _calculate_avg_time(self, data):
        if not data or len(data) == 0:
            return 0
        total_minutes = 0
        count = 0
        for row in data:
            if len(row) >= 4:
                try:
                    time_str = row[3]
                    minutes = self._parse_time(time_str)
                    total_minutes += minutes
                    count += 1
                except (ValueError, IndexError):
                    pass
        return total_minutes / count if count > 0 else 0

    # Порівнює відсотки правильних відповідей двох КМР і зберігає гістограми
    def compare_avg_plots(self, other_num):
        if self.num not in KmrWork.kmrs or other_num not in KmrWork.kmrs:
            print("Один з КМР не зареєстрований")
            return
        
        data1 = self.read_csv()
        if data1 is None:
            print("Помилка: не вдалося прочитати дані першого КМР")
            return
        
        other_kmr = KmrCsv()
        other_kmr.set_ref(KmrWork.kmrs[other_num])
        other_kmr.set_num(other_num)
        data2 = other_kmr.read_csv()
        if data2 is None:
            print("Помилка: не вдалося прочитати дані другого КМР")
            return
        
        percentages1 = self.avg_stat(data1)
        percentages2 = self.avg_stat(data2)
        
        if not percentages1 or not percentages2:
            print("Помилка: не вдалося обчислити відсотки для порівняння")
            return
        
        plt.figure(figsize=(10, 6))
        questions = [f"Питання {i+1}" for i in range(len(percentages1))]
        plt.bar(questions, percentages1)
        plt.xlabel('Питання')
        plt.ylabel('Відсоток правильних відповідей (%)')
        plt.title(f'Відсотки правильних відповідей - КМР {self.num}')
        plt.xticks(rotation=45)
        plt.tight_layout()
        filename1 = os.path.join(self.cat, f'compare_avg_{self.num}.png')
        plt.savefig(filename1)
        plt.close()
        print(f"Графік збережено: {filename1}")
        
        plt.figure(figsize=(10, 6))
        questions = [f"Питання {i+1}" for i in range(len(percentages2))]
        plt.bar(questions, percentages2)
        plt.xlabel('Питання')
        plt.ylabel('Відсоток правильних відповідей (%)')
        plt.title(f'Відсотки правильних відповідей - КМР {other_num}')
        plt.xticks(rotation=45)
        plt.tight_layout()
        filename2 = os.path.join(self.cat, f'compare_avg_{other_num}.png')
        plt.savefig(filename2)
        plt.close()
        print(f"Графік збережено: {filename2}")


def task04():
    kmr1 = KmrWork("marks2.lab11.csv", 1)
    kmr2 = KmrWork("marks2.lab11.csv", 2)

    data2 = kmr2.read_csv()
    if data2:
        percentages = kmr2.avg_stat(data2)
        kmr2.avg_plot(percentages)
        marks_dict = kmr2.marks_stat(data2)
        kmr2.marks_plot(marks_dict)
        
        best_marks = kmr2.best_marks_per_time(data2, 0, 10)
        kmr2.best_marks_plot(best_marks)

    kmr1.compare_csv(2)
    kmr1.compare_avg_plots(2)


task04()

