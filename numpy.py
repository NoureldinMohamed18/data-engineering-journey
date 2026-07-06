# ╔══════════════════════════════════════════════════════════════════════════╗
# ║                    NUMPY COMPLETE PRACTICAL GUIDE                        ║
# ╚══════════════════════════════════════════════════════════════════════════╝

# ───────────────────────────────────────────────────────────────────────────
# SECTION 1: استيراد المكتبة
# ───────────────────────────────────────────────────────────────────────────
import numpy as np  
# np هو alias (اختصار) شائع الاستخدام في كل كود Data Science

# ───────────────────────────────────────────────────────────────────────────
# SECTION 2: إنشاء Arrays
# ───────────────────────────────────────────────────────────────────────────

# 2.1: إنشاء array من list عادي
arr1 = np.array([1, 2, 3, 4, 5])
# └─→ تحويل قائمة Python لـ NumPy array من نوع int64

# 2.2: إنشاء array ثنائي الأبعاد (مصفوفة)
arr2 = np.array([[1, 2, 3], 
                  [4, 5, 6]], dtype=np.float32)
# └─→ 2 صفوف × 3 أعمدة، نوع البيانات float32

print("Shape:", arr2.shape)    # (2, 3) → 2 صفوف، 3 أعمدة
print("Dimensions:", arr2.ndim) # 2 → بعدان
print("Data Type:", arr2.dtype) # float32
print("Size:", arr2.size)       # 6 → عدد العناصر الكلي

# 2.3: إنشاء arrays خاصة
zeros = np.zeros((3, 4))       # مصفوفة 3×4 مليئة بأصفار
ones = np.ones((2, 2))          # مصفوفة 2×2 مليئة بواحدات
identity = np.eye(3)            # مصفوفة وحدة 3×3 (قطر 1، الباقي 0)
full = np.full((2, 3), 7)       # مصفوفة 2×3 مليئة بالرقم 7

# 2.4: إنشاء sequences
arange_arr = np.arange(0, 10, 2)   # [0, 2, 4, 6, 8] (بداية, نهاية, خطوة)
linspace_arr = np.linspace(0, 1, 5) # [0, 0.25, 0.5, 0.75, 1] (5 أعداد متساوية)

# 2.5: إنشاء random arrays
random_arr = np.random.random((3, 3))      # أرقام عشوائية بين 0 و1
randint_arr = np.random.randint(0, 100, (2, 2)) # أعداد صحيحة عشوائية
normal_arr = np.random.normal(0, 1, (3, 3))     # توزيع طبيعي (mean=0, std=1)

# 2.6: إنشاء array مشابه لآخر
zeros_like_arr = np.zeros_like(arr2)  # نفس شكل arr2 لكن بأصفار
ones_like_arr = np.ones_like(arr2)    # نفس الشكل لكن بواحدات

# ───────────────────────────────────────────────────────────────────────────
# SECTION 3: Shaping & Reshaping (تغيير الأبعاد)
# ───────────────────────────────────────────────────────────────────────────

a = np.arange(6)           # [0, 1, 2, 3, 4, 5] ← 1D
print("Original shape:", a.shape)  # (6,)

a = a.reshape(3, 2)        # [[0,1],[2,3],[4,5]] ← 3×2
print("Reshaped to 3x2:", a.shape)  # (3, 2)

a = a.reshape(2, -1)       # -1 يعني "احسب البُعد التاني تلقائياً"
# └─→ يصبح 2×3 لأن 6÷2 = 3

a = a.ravel()              # يرجع لـ 1D: [0, 1, 2, 3, 4, 5]

# ───────────────────────────────────────────────────────────────────────────
# SECTION 4: Transposition (النقل)
# ───────────────────────────────────────────────────────────────────────────

b = np.arange(10).reshape(5, 2)  # 5×2
print("Original shape:", b.shape)  # (5, 2)

b_T = b.T                        # النقل ← يصبح 2×5
print("Transposed shape:", b_T.shape)  # (2, 5)

# النقل العام للأبعاد الأعلى
c = np.arange(24).reshape(2, 3, 4)  # 2×3×4
c_t = c.transpose((1, 0, 2))        # يبدل البعد الأول والثاني ← 3×2×4

# ───────────────────────────────────────────────────────────────────────────
# SECTION 5: Views vs Copies (الفرق المهم!)
# ───────────────────────────────────────────────────────────────────────────

original = np.array([1, 2, 3, 4, 5])

view = original[1:4]       # slicing يُرجع VIEW تلقائياً
view[0] = 999              # تعديل الـ view
print("Original after view edit:", original)  # [1, 999, 3, 4, 5] ← تغير!

copy = original[1:4].copy()  # صريح: أريد نسخة
# أو: copy = np.copy(original[1:4])
copy[0] = 888
print("Original after copy edit:", original)  # لم يتغير

# ───────────────────────────────────────────────────────────────────────────
# SECTION 6: العمليات الرياضية (Element-wise)
# ───────────────────────────────────────────────────────────────────────────

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])

# 6.1: الجمع والطرح والضرب والقسمة
print("Addition:\n", x + y)        # [[6,8],[10,12]]
print("Subtraction:\n", x - y)     # [[-4,-4],[-4,-4]]
print("Multiplication:\n", x * y)  # [[5,12],[21,32]] ← عنصر بعنصر!
print("Division:\n", x / y)        # [[0.2,0.33...]]

# 6.2: ضرب المصفوفات (Matrix Multiplication)
print("Dot product:\n", np.dot(x, y))  # أو: x @ y
# └─→ [[19,22],[43,50]] ← ضرب مصفوفات حقيقي

# 6.3: العمليات على نفس المصفوفة
print("x + 10:\n", x + 10)    # يضيف 10 لكل عنصر (Broadcasting!)
print("x ** 2:\n", x ** 2)    # كل عنصر يُرفع للتربيع

# 6.4: العمليات المكانية (In-place)
x += 1   # يعدل x نفسه بدون إنشاء نسخة جديدة ← أسرع في الذاكرة

# ───────────────────────────────────────────────────────────────────────────
# SECTION 7: UFuncs (Universal Functions)
# ───────────────────────────────────────────────────────────────────────────

arr = np.array([0, np.pi/2, np.pi])

print("sin:", np.sin(arr))       # [0, 1, 0]
print("cos:", np.cos(arr))       # [1, 0, -1]
print("exp:", np.exp(np.array([1, 2, 3])))  # [e^1, e^2, e^3]
print("sqrt:", np.sqrt(np.array([4, 9, 16])))  # [2, 3, 4]
print("log:", np.log(np.array([1, np.e, np.e**2])))  # [0, 1, 2]

# دوال إحصائية
arr = np.array([1, 2, 3, 4, 5])
print("Sum:", np.sum(arr))           # 15
print("Mean:", np.mean(arr))         # 3.0
print("Std:", np.std(arr))           # الانحراف المعياري
print("Min:", np.min(arr))           # 1
print("Max:", np.max(arr))           # 5
print("Argmax:", np.argmax(arr))     # 4 ← موقع الـ max

# ───────────────────────────────────────────────────────────────────────────
# SECTION 8: Indexing & Slicing (التقطيع)
# ───────────────────────────────────────────────────────────────────────────

img = np.arange(16).reshape(4, 4)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]

print("Top-left:", img[0, 0])       # 0 ← أول عنصر
print("First row:", img[0, :])      # [0,1,2,3] ← الصف الأول
print("Last column:", img[:, -1])   # [3,7,11,15] ← آخر عمود
print("Center 2x2:", img[1:3, 1:3]) # [[5,6],[9,10]]

# Slicing متقدم
print("Every other:", img[::2, ::2])  # [[0,2],[8,10]] ← كل ثاني عنصر
print("Reversed rows:", img[::-1, :])  # يقلب الصفوف

# Boolean Indexing (التقطيع الشرطي)
print("Values > 10:", img[img > 10])   # [11,12,13,14,15]
img[img < 5] = 0                     # يصفر كل القيم < 5

# Fancy Indexing (تقطيع بقائمة)
print("Rows 1 & 3:", img[[1, 3], :])   # الصف 1 والصف 3

# ───────────────────────────────────────────────────────────────────────────
# SECTION 9: Axes & Aggregation (الأبعاد والتجميع)
# ───────────────────────────────────────────────────────────────────────────

matrix = np.array([[1, 2, 3],
                    [4, 5, 6]])  # 2×3

print("Sum all:", matrix.sum())           # 21 ← مجموع كل العناصر
print("Sum axis=0:", matrix.sum(axis=0))  # [5,7,9] ← جمع على الصفوف
print("Sum axis=1:", matrix.sum(axis=1))  # [6,15] ← جمع على الأعمدة

# keepdims يحافظ على الأبعاد
print("Keep dims:", matrix.sum(axis=1, keepdims=True))  # [[6],[15]]

# دوال التجميع المختلفة
print("Mean by col:", matrix.mean(axis=0))   # [2.5, 3.5, 4.5]
print("Max by row:", matrix.max(axis=1))     # [3, 6]

# ───────────────────────────────────────────────────────────────────────────
# SECTION 10: Broadcasting (البث)
# ───────────────────────────────────────────────────────────────────────────

# 10.1: Scalar + Array
a = np.array([1, 2, 3])
print("a + 10:", a + 10)  # [11, 12, 13] ← الـ 10 تُبث على كل العناصر

# 10.2: Array 2D + Array 1D
matrix = np.array([[1, 2, 3],
                    [4, 5, 6]])  # shape: (2, 3)
row = np.array([10, 20, 30])       # shape: (3,)
print("Add row:\n", matrix + row)  # يضيف [10,20,30] لكل صف!

# 10.3: Column vector broadcasting
col = np.array([[10], [20]])       # shape: (2, 1)
print("Add col:\n", matrix + col)  # يضيف 10 للصف الأول و20 للثاني

# 10.4: Broadcasting في الصور (3D)
image = np.random.random((100, 200, 3))  # صورة RGB
color_shift = np.array([0.1, 0.2, 0.3])  # تعديل ألوان
bright_image = image + color_shift       # يُبث على البعد الأخير (القنوات)

# ───────────────────────────────────────────────────────────────────────────
# SECTION 11: Upcasting (رفع نوع البيانات)
# ───────────────────────────────────────────────────────────────────────────

a = np.array([1, 2, 3], dtype=np.int32)
b = np.array([1.5, 2.5, 3.5], dtype=np.float32)
result = a + b
print("Result dtype:", result.dtype)  # float32 ← النوع الأعم/أدق

# ⚠️ تحذير: Upcasting لا يمنع Overflow!
uint8_arr = np.array([250, 251, 252], dtype=np.uint8)
print(uint8_arr + 10)  # [4, 5, 6] ← تجاوز! (250+10=260 → 4)

# الحل: تحويل يدوي قبل العملية
float_arr = uint8_arr.astype(np.float32) + 10
print("Correct:", float_arr)  # [260, 261, 262]

# ───────────────────────────────────────────────────────────────────────────
# SECTION 12: Concatenate & Split (الدمج والتقسيم)
# ───────────────────────────────────────────────────────────────────────────

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# الدمج
print("Vertical:\n", np.vstack((a, b)))   # دمج رأسي ← 4×2
print("Horizontal:\n", np.hstack((a, b))) # دمج أفقي ← 2×4
print("Concat axis=0:\n", np.concatenate((a, b), axis=0))  # نفس vstack
print("Concat axis=1:\n", np.concatenate((a, b), axis=1))  # نفس hstack

# التقسيم
split_arr = np.array([1, 2, 3, 4, 5, 6])
parts = np.array_split(split_arr, 3)  # يقسم لـ 3 أجزاء
print("Split:", parts)  # [array([1,2]), array([3,4]), array([5,6])]

# ───────────────────────────────────────────────────────────────────────────
# SECTION 13: Saving & Loading (حفظ وتحميل Arrays)
# ───────────────────────────────────────────────────────────────────────────

arr = np.array([[1, 2, 3], [4, 5, 6]])

# الحفظ
np.save('my_array.npy', arr)           # صيغة NumPy الثنائية
np.savetxt('my_array.csv', arr, delimiter=',')  # CSV

# التحميل
loaded = np.load('my_array.npy')       # يحمل .npy
loaded_csv = np.loadtxt('my_array.csv', delimiter=',')  # يحمل CSV

print("Loaded:", loaded)
print("Loaded CSV:", loaded_csv)

# ───────────────────────────────────────────────────────────────────────────
# SECTION 14: Linear Algebra (الجبر الخطي)
# ───────────────────────────────────────────────────────────────────────────

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Matrix multiply:\n", A @ B)        # أو np.dot(A, B)
print("Determinant:", np.linalg.det(A))   # المحسم
print("Inverse:\n", np.linalg.inv(A))    # المقلوب
print("Eigenvalues:", np.linalg.eigvals(A))  # القيم الذاتية
print("Trace:", np.trace(A))              # أثر المصفوفة

# حل معادلات خطية: Ax = b
b = np.array([1, 2])
x = np.linalg.solve(A, b)
print("Solution:", x)  # x = [-0. , 0.5]

# ───────────────────────────────────────────────────────────────────────────
# SECTION 15: Performance Comparison (مقارنة السرعة)
# ───────────────────────────────────────────────────────────────────────────

import time

size = 1000000
python_list = list(range(size))
numpy_arr = np.arange(size)

# Python sum
start = time.time()
python_sum = sum(python_list)
python_time = time.time() - start

# NumPy sum
start = time.time()
numpy_sum = np.sum(numpy_arr)
numpy_time = time.time() - start

print(f"Python time: {python_time:.4f}s")
print(f"NumPy time: {numpy_time:.4f}s")
print(f"NumPy is {python_time/numpy_time:.0f}x faster!")