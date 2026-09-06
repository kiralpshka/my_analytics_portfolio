import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

data_text = """date,source,registrations,visits
01.01.2026,Instagram,45,1200
02.01.2026,Instagram,52,1350
03.01.2026,Instagram,38,980
04.01.2026,Instagram,61,1500
05.01.2026,Facebook,30,900
06.01.2026,Facebook,42,1100
07.01.2026,Facebook,35,950
08.01.2026,Facebook,55,1300
09.01.2026,Yandex,20,600
10.01.2026,Yandex,28,750
11.01.2026,Yandex,15,500
12.01.2026,Yandex,33,820
13.01.2026,Instagram,48,1250
14.01.2026,Instagram,55,1400
15.01.2026,Facebook,40,1050
16.01.2026,Facebook,50,1200
17.01.2026,Yandex,25,680
18.01.2026,Yandex,30,790"""

data = pd.read_csv(StringIO(data_text))

total_by_source = data.groupby('source')['registrations'].sum()

data['conversion'] = (data['registrations'] / data['visits']) * 100
avg_conversion = data.groupby('source')['conversion'].mean()

print("=" * 40)
print("АНАЛИЗ РЕКЛАМНЫХ КАНАЛОВ ОНЛАЙН-ШКОЛЫ")
print("=" * 40)

print("\n1. Всего регистраций по каналам:")
print(total_by_source)

print("\n2. Средняя конверсия по каналам (%):")
print(avg_conversion.round(2))

print("\n3. Лучший канал по регистрациям:")
best_source = total_by_source.idxmax()
best_count = total_by_source.max()
print(f"   {best_source} — {best_count} регистраций")

print("\n4. Рекомендации:")
if best_source == 'Instagram':
    print("Инвестируйте больше бюджета в Instagram")
    print("Это самый эффективный канал для вашей школы")
else:
    print(f"Канал {best_source} показывает лучшие результаты")

# Строим график
plt.figure(figsize=(10, 6))
total_by_source.plot(kind='bar', color=['#ff6b6b', '#4ecdc4', '#45b7d1'])
plt.title('Регистрации по рекламным каналам', fontsize=16)
plt.xlabel('Канал рекламы')
plt.ylabel('Количество регистраций')
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.3)

plt.savefig('chart.png', dpi=100)
print("\nГрафик сохранён как chart.png")
plt.show()
