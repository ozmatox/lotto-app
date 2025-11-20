from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import requests
from collections import Counter
import random

class LottoLogic:
    @staticmethod
    def analyze_lotto():
        try:
            url = 'http://www.mbnet.com.pl/dl.txt'
            response = requests.get(url)
            if response.status_code != 200:
                return "❌ Nie udało się pobrać danych."

            data = response.text.strip().split('\n')

            all_draws = []
            for line in data:
                parts = line.strip().split()
                if len(parts) >= 3:
                    try:
                        numbers = list(map(int, parts[2].split(',')))
                        if len(numbers) == 6:
                            all_draws.append(numbers)
                    except:
                        continue

            if not all_draws:
                return "⚠️ Brak danych do analizy."

            all_numbers = [num for draw in all_draws for num in draw]
            number_counts = Counter(all_numbers)

            top_6 = number_counts.most_common(6)
            bottom_6 = number_counts.most_common()[-6:]
            top_12 = [num for num, _ in number_counts.most_common(12)]

            top_6_str = ', '.join([str(num) for num, _ in top_6])
            bottom_6_str = ', '.join([str(num) for num, _ in bottom_6])
            sample_draw = ', '.join(map(str, sorted(random.sample(top_12, 6))))

            return (f"🔝 Najczęstsze liczby:\n{top_6_str}\n\n"
                    f"🧊 Najrzadsze liczby:\n{bottom_6_str}\n\n"
                    f"🎲 Przykładowy zakład z top 12:\n{sample_draw}")

        except Exception as e:
            return f"❌ Błąd: {e}"

class LottoLayout(BoxLayout):
    def pokaz_analize(self):
        wynik = LottoLogic.analyze_lotto()
        self.ids.wyniki_label.text = wynik

class LottoApp(App):
    def build(self):
        return LottoLayout()

if __name__ == '__main__':
    LottoApp().run()
