# Verification of Fajr Prayer Time Using Morning Twilight Photometry
## تحقيق توقيت صلاة الفجر رصدياً باستخدام القياس الضوئي لشفق الصباح

### Overview / نبذة عن المشروع
This project is a computational simulation and data analysis framework that replicates an astrophysical research methodology originally conducted at **Kottamia Astronomical Observatory (Egypt)**. The project aims to cross-verify the astronomical and legal (religious) timing of Fajr prayer by analyzing the sky background brightness to detect the exact moment of the "True Dawn" (Fajr Sadik).

هذا المشروع يقدم إطاراً برمجياً ومحاكاة لتحليل البيانات الفلكية يحاكي المنهجية البحثية الرصدية التي تمت في **مرصد القطامية الفلكي (مصر)**. يهدف المشروع إلى التحقق من التوقيت الفلكي والشرعي لصلاة الفجر عبر تحليل شدة إضاءة خلفية السماء لتحديد اللحظة الدقيقة لانكسار الضوء وبداية "الفجر الصادق".

### Methodology / المنهجية العلمية
* **Location / الموقع:** Cairo / Kottamia Observatory, Egypt (Lat: 29.933° N, Lon: 31.833° E).
* **Target Angle / الزاوية المستهدفة:** $19.5^\circ$ below the horizon (Egyptian General Authority of Survey standard).
* **Hardware Simulated / الأجهزة المستهدفة:** Celestron Travel Scope 70 DX + iPhone 16 Pro Max (RAW Photometry Mode via NightCap).

### How to Run / طريقة التشغيل
1. Install dependencies: `pip install numpy matplotlib`
2. Run the analyzer: `python fajr_simulator.py`

### Result / النتيجة
The simulation correctly incorporates Egypt's Daylight Saving Time (GMT+4) for June, detecting the precise onset of twilight at **04:09 AM** corresponding to the solar depression angle of **$19.5^\circ$**.
