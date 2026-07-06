# ╔══════════════════════════════════════════════════════════════════════════╗
# ║         DATA VISUALIZATION - MATPLOTLIB + SEABORN + PLOTLY               ║
# ╚══════════════════════════════════════════════════════════════════════════╝

import pandas as pd
import numpy as np

# ══════════════════════════════════════════════════════════════════════════
# PART A: MATPLOTLIB
# ══════════════════════════════════════════════════════════════════════════

import matplotlib.pyplot as plt

# إنشاء بيانات تجريبية
np.random.seed(42)
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.normal(0, 0.1, 100)
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 32]

# ──────────────────────────────────────────────────────────────────────────
# A.1: Line Plot - رسم الخطوط
# ──────────────────────────────────────────────────────────────────────────
plt.figure(figsize=(10, 5))          # إنشاء figure بحجم 10×5 إنش
plt.plot(x, y, color='blue', linestyle='-', linewidth=2, label='sin(x) + noise')
# └─→ x: المحور الأفقي, y: المحور الرأسي
#     color: لون الخط, linestyle: نوع الخط (- = متصل)
#     linewidth: سمك الخط, label: اسم الخط للـ legend

plt.title('Line Plot Example', fontsize=14, fontweight='bold')
plt.xlabel('X Axis', fontsize=12)
plt.ylabel('Y Axis', fontsize=12)
plt.legend()                          # عرض الـ legend
plt.grid(True, alpha=0.3)             # شبكة خفيفة
plt.show()                            # عرض الرسمة

# ──────────────────────────────────────────────────────────────────────────
# A.2: Scatter Plot - رسم النقاط
# ──────────────────────────────────────────────────────────────────────────
plt.figure(figsize=(8, 6))
plt.scatter(x, y, c=y, cmap='viridis', s=50, alpha=0.7, edgecolors='black')
# └─→ c=y: لون كل نقطة يعتمد على قيمة y
#     cmap: خريطة الألوان, s: حجم النقاط
#     alpha: الشفافية, edgecolors: لون الحدود

plt.title('Scatter Plot', fontsize=14)
plt.xlabel('X')
plt.ylabel('Y')
plt.colorbar(label='Y Value')
plt.show()

# ──────────────────────────────────────────────────────────────────────────
# A.3: Bar Chart - الرسم البياني الأعمدة
# ──────────────────────────────────────────────────────────────────────────
plt.figure(figsize=(8, 5))
plt.bar(categories, values, color=['red', 'green', 'blue', 'orange', 'purple'])
plt.title('Bar Chart', fontsize=14)
plt.xlabel('Category')
plt.ylabel('Value')
for i, v in enumerate(values):
    plt.text(i, v + 1, str(v), ha='center', fontweight='bold')
    # └─→ كتابة القيمة فوق كل عمود
plt.show()

# Bar Chart أفقي
plt.figure(figsize=(6, 5))
plt.barh(categories, values, color='skyblue')
plt.title('Horizontal Bar Chart')
plt.show()

# ──────────────────────────────────────────────────────────────────────────
# A.4: Histogram - الرسم البياني التكراري
# ──────────────────────────────────────────────────────────────────────────
data = np.random.normal(100, 15, 1000)  # 1000 نقطة، mean=100, std=15

plt.figure(figsize=(8, 5))
plt.hist(data, bins=30, color='steelblue', edgecolor='black', alpha=0.7)
# └─→ bins=30: عدد الأعمدة, edgecolor: لون حدود الأعمدة

plt.title('Histogram', fontsize=14)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.axvline(data.mean(), color='red', linestyle='dashed', linewidth=2, label=f'Mean: {data.mean():.1f}')
plt.legend()
plt.show()

# ──────────────────────────────────────────────────────────────────────────
# A.5: Subplots - رسومات فرعية متعددة
# ──────────────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
# └─→ 2×2 = 4 رسومات في figure واحد
#     axes[0,0], axes[0,1], axes[1,0], axes[1,1]

axes[0, 0].plot(x, np.sin(x))
axes[0, 0].set_title('Sine Wave')

axes[0, 1].scatter(x, y, s=10)
axes[0, 1].set_title('Scatter')

axes[1, 0].bar(categories, values)
axes[1, 0].set_title('Bar Chart')

axes[1, 1].hist(data, bins=20)
axes[1, 1].set_title('Histogram')

plt.tight_layout()  # ضبط المسافات بين الرسومات
plt.show()

# ──────────────────────────────────────────────────────────────────────────
# A.6: Box Plot - للكشف عن Outliers
# ──────────────────────────────────────────────────────────────────────────
data_with_outliers = np.concatenate([np.random.normal(50, 10, 100), [100, 105, 110]])

plt.figure(figsize=(6, 5))
plt.boxplot(data_with_outliers, vert=True, patch_artist=True,
            boxprops=dict(facecolor='lightblue'))
# └─→ vert=True: رأسي, patch_artist=True: تلوين الصندوق
#     boxprops: خصائص الصندوق

plt.title('Box Plot (Outliers Detection)')
plt.ylabel('Value')
plt.show()

# ══════════════════════════════════════════════════════════════════════════
# PART B: SEABORN
# ══════════════════════════════════════════════════════════════════════════

import seaborn as sns

# تحميل datasets المدمجة في Seaborn
tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')

print("Tips dataset:")
print(tips.head())

# ──────────────────────────────────────────────────────────────────────────
# B.1: Line Plot - Seaborn
# ──────────────────────────────────────────────────────────────────────────
plt.figure(figsize=(10, 5))
sns.lineplot(data=flights, x='year', y='passengers', marker='o')
# └─→ data=flights: DataFrame المصدر
#     x, y: أسماء الأعمدة
#     marker='o': نقاط على الخط

plt.title('Passengers Over Time')
plt.show()

# ──────────────────────────────────────────────────────────────────────────
# B.2: Scatter Plot with Regression Line
# ──────────────────────────────────────────────────────────────────────────
plt.figure(figsize=(8, 6))
sns.regplot(data=tips, x='total_bill', y='tip', scatter_kws={'alpha': 0.5})
# └─→ regplot = scatter plot + خط انحدار خطي
#     scatter_kws: خصائص النقاط

plt.title('Total Bill vs Tip (with Regression Line)')
plt.show()

# ──────────────────────────────────────────────────────────────────────────
# B.3: Bar Plot - Seaborn
# ──────────────────────────────────────────────────────────────────────────
plt.figure(figsize=(8, 5))
sns.barplot(data=tips, x='day', y='total_bill', hue='sex', palette='Set2')
# └─→ hue='sex': يفصل البيانات حسب الجنس (أعمدة ملونة)
#     palette: خريطة الألوان

plt.title('Average Total Bill by Day')
plt.show()

# ──────────────────────────────────────────────────────────────────────────
# B.4: Box Plot - Seaborn
# ──────────────────────────────────────────────────────────────────────────
plt.figure(figsize=(8, 5))
sns.boxplot(data=tips, x='day', y='total_bill', palette='coolwarm')
plt.title('Distribution of Total Bill by Day')
plt.show()

# Violin Plot (Box Plot + Density)
plt.figure(figsize=(8, 5))
sns.violinplot(data=tips, x='day', y='total_bill', palette='muted')
plt.title('Violin Plot - Total Bill by Day')
plt.show()

# ──────────────────────────────────────────────────────────────────────────
# B.5: Heatmap - خريطة حرارية
# ──────────────────────────────────────────────────────────────────────────
# مصفوفة الارتباط
corr = tips[['total_bill', 'tip', 'size']].corr()

plt.figure(figsize=(6, 5))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f',
            square=True, linewidths=0.5)
# └─→ annot=True: عرض الأرقام, fmt='.2f': تنسيق رقمي
#     square=True: مربعات متساوية, linewidths: فواصل

plt.title('Correlation Heatmap')
plt.show()

# ──────────────────────────────────────────────────────────────────────────
# B.6: Pair Plot - رسومات زوجية
# ──────────────────────────────────────────────────────────────────────────
# نستخدم sample أصغر للسرعة
sample = tips[['total_bill', 'tip', 'size']].sample(50)

sns.pairplot(sample, diag_kind='kde', plot_kws={'alpha': 0.6})
# └─→ diag_kind='kde': الرسومات القطرية = KDE
#     plot_kws: خصائص الرسومات الزوجية

plt.suptitle('Pair Plot', y=1.02)
plt.show()

# ──────────────────────────────────────────────────────────────────────────
# B.7: Count Plot
# ──────────────────────────────────────────────────────────────────────────
plt.figure(figsize=(6, 4))
sns.countplot(data=tips, x='day', palette='viridis')
plt.title('Count of Entries by Day')
plt.show()

# ──────────────────────────────────────────────────────────────────────────
# B.8: Joint Plot (Scatter + Histograms)
# ──────────────────────────────────────────────────────────────────────────
sns.jointplot(data=tips, x='total_bill', y='tip', kind='scatter',
              marginal_kws=dict(bins=20))
# └─→ kind='scatter': نوع الرسم المركزي
#     marginal_kws: خصائص الرسومات الهامشية

plt.suptitle('Joint Plot', y=1.02)
plt.show()

# ──────────────────────────────────────────────────────────────────────────
# B.9: Themes - سمات Seaborn
# ──────────────────────────────────────────────────────────────────────────
sns.set_style('whitegrid')    # whitegrid, darkgrid, white, dark, ticks
sns.set_palette('husl')       # تغيير لوحة الألوان الافتراضية

plt.figure(figsize=(8, 5))
sns.boxplot(data=tips, x='day', y='total_bill')
plt.title('With Whitegrid Style')
plt.show()

# إعادة الضبط
sns.set_style('white')

# ══════════════════════════════════════════════════════════════════════════
# PART C: PLOTLY (Interactive)
# ══════════════════════════════════════════════════════════════════════════

import plotly.express as px
import plotly.graph_objects as go

# ──────────────────────────────────────────────────────────────────────────
# C.1: Interactive Line Plot
# ──────────────────────────────────────────────────────────────────────────
fig = px.line(flights, x='year', y='passengers',
              title='Passengers Over Time (Interactive)',
              labels={'passengers': 'Number of Passengers'},
              markers=True)
# └─→ interactive: hover لرؤية القيم, zoom, pan
fig.show()

# ──────────────────────────────────────────────────────────────────────────
# C.2: Interactive Scatter Plot
# ──────────────────────────────────────────────────────────────────────────
fig = px.scatter(tips, x='total_bill', y='tip', color='sex',
                 size='size', hover_data=['day', 'time'],
                 title='Tips Dataset - Interactive Scatter')
# └─→ color='sex': لون حسب الجنس
#     size='size': حجم النقاط حسب عدد الأشخاص
#     hover_data: معلومات إضافية عند الـ hover
fig.show()

# ──────────────────────────────────────────────────────────────────────────
# C.3: Interactive Bar Chart
# ──────────────────────────────────────────────────────────────────────────
df_bar = tips.groupby('day')['total_bill'].mean().reset_index()
fig = px.bar(df_bar, x='day', y='total_bill',
             title='Average Bill by Day (Interactive)',
             color='day')
fig.show()

# ──────────────────────────────────────────────────────────────────────────
# C.4: Heatmap with Plotly
# ──────────────────────────────────────────────────────────────────────────
fig = px.imshow(corr, text_auto=True, aspect='auto',
                title='Correlation Heatmap (Interactive)')
fig.show()

# ══════════════════════════════════════════════════════════════════════════
# PART D: DASH - Interactive Dashboard
# ══════════════════════════════════════════════════════════════════════════

# لتشغيل Dash، ثبت: pip install dash

from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px

# إنشاء تطبيق Dash
app = Dash(__name__)

# تخطيط الصفحة
app.layout = html.Div([
    html.H1("Sales Dashboard", style={'textAlign': 'center'}),
    
    # Dropdown للاختيار
    dcc.Dropdown(
        id='category-dropdown',
        options=[{'label': c, 'value': c} for c in tips['day'].unique()],
        value='Sun',
        style={'width': '50%', 'margin': 'auto'}
    ),
    
    # رسم تفاعلي
    dcc.Graph(id='sales-graph'),
    
    # نص يتغير
    html.Div(id='output-text', style={'textAlign': 'center', 'marginTop': 20})
])

# Callback: عندما يتغير Dropdown، يتغير الرسم
@callback(
    Output('sales-graph', 'figure'),
    Output('output-text', 'children'),
    Input('category-dropdown', 'value')
)
def update_graph(selected_day):
    filtered = tips[tips['day'] == selected_day]
    fig = px.scatter(filtered, x='total_bill', y='tip',
                     title=f'Sales for {selected_day}')
    text = f"Showing {len(filtered)} records for {selected_day}"
    return fig, text

# تشغيل الخادم
# if __name__ == '__main__':
#     app.run(debug=True)  # ← افتح localhost:8050 في المتصفح

print("\nDash app defined. Uncomment app.run() to start the server.")

# ══════════════════════════════════════════════════════════════════════════
# PART E: Saving Figures
# ══════════════════════════════════════════════════════════════════════════

# Matplotlib
# plt.savefig('my_plot.png', dpi=300, bbox_inches='tight')
# plt.savefig('my_plot.pdf')  ← PDF عالي الجودة

# Plotly
# fig.write_html('interactive_plot.html')  ← تفاعلي في HTML!
# fig.write_image('plotly_plot.png')