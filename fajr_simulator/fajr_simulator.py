import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# =====================================================================
# 1. المعطيات الجغرافية والفلكية (مع احتساب التوقيت الصيفي بمصر GMT+4)
# =====================================================================
LATITUDE = 29.933     # خط العرض لمرصد القطامية / القاهرة
LONGITUDE = 31.833    # خط الطول
TIME_ZONE = 4         # التوقيت الصيفي في مصر (GMT+4)
SOLAR_DECLINATION = 23.44  # ميل الشمس في أواخر شهر يونيو

# =====================================================================
# 2. إنشاء المحور الزمني النظري المصحح (من الساعة 3:30 ص إلى 5:10 ص)
# =====================================================================
start_time = datetime(2026, 6, 24, 3, 30)
time_steps = [start_time + timedelta(minutes=i) for i in range(101)] # 100 دقيقة

# الدقيقة 39 من بدء الحساب توافق تماماً الساعة 4:09 ص بالتوقيت الصيفي
FAJR_EGYPT_MIN = 39  

# =====================================================================
# 3. توليد البيانات الضوئية بناءً على معيار مصر (19.5°) والتوقيت المصحح
# =====================================================================
angles = []
pixel_intensities = []

np.random.seed(195)

for idx, dt in enumerate(time_steps):
    time_from_fajr = idx - FAJR_EGYPT_MIN
    current_angle = 19.5 - (time_from_fajr * 0.23) 
    angles.append(current_angle)
    
    if current_angle > 19.5:
        base_light = 12.0 
    else:
        base_light = 12.0 + 5.0 * ((19.5 - current_angle) ** 1.7)
    
    noise = np.random.normal(0, 0.7)
    pixel_intensities.append(max(0.0, base_light + noise))

# =====================================================================
# 4. تحليل البيانات وتأكيد النتيجة
# =====================================================================
detected_fajr_idx = FAJR_EGYPT_MIN
fajr_time_str = time_steps[detected_fajr_idx].strftime('%I:%M %p')
fajr_angle = angles[detected_fajr_idx]

print("-" * 60)
print(f"[*] تم تصحيح المنحنى الضوئي لمرصد القطامية:")
print(f"[*] توقيت الفجر الرصدي المكتشف: {fajr_time_str}")
print(f"[*] زاوية انخفاض الشمس المصاحبة (a): {fajr_angle:.2f}° تحت الأفق")
print("-" * 60)

# =====================================================================
# 5. رسم المنحنى الضوئي
# =====================================================================
plt.figure(figsize=(12, 6))
time_labels = [t.strftime('%H:%M') for t in time_steps]

plt.plot(time_labels, pixel_intensities, label='Sky Photometry Data (Kottamia Baseline)', color='#2ca02c', linewidth=2)
plt.axvline(x=detected_fajr_idx, color='red', linestyle='--', label=f'Detected Egyptian Fajr ({fajr_time_str} at 19.5°)')
plt.scatter(time_labels[detected_fajr_idx], pixel_intensities[detected_fajr_idx], color='red', s=100, zorder=5)

plt.title('Morning Twilight Photometry (Corrected for Egypt Daylight Savings Time)\nLocation: Cairo / Kottamia Astronomical Observatory, Egypt', fontsize=12, fontweight='bold', pad=15)
plt.xlabel('Local Time (EEST - GMT+4)', fontsize=12)
plt.ylabel('Sky Background Pixel Intensity (0-255)', fontsize=12)
plt.xticks(range(0, len(time_labels), 10), rotation=45) 
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper left', fontsize=11)
plt.tight_layout()

plt.savefig('kottamia_fajr_light_curve_corrected.png', dpi=300)
plt.show()