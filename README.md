# الاختبار العملي: خدمة المفقودات

اختبار عملي لبرنامج **أساسيات هندسة DevOps** (أكاديمية الخوارزمي). يقيس مهارات المعمل الأول: من المهمة إلى الإصدار.

الخدمة تسجّل الأغراض المفقودة التي يجدها الجمهور ويسلّمونها لمراكز الشرطة.

## قبل أن تبدأ

1. اضغط **Fork** ثم **Create fork**.
2. من نسختك: **Code** ثم **Codespaces** ثم **Create codespace on main**.
3. ثبّت المكتبات ثم تحقق أن البيئة سليمة:

```bash
pip install -r requirements.txt
python -m pytest -q
```

يجب أن ترى `6 passed`.

## المطلوب

طلب الضابط المناوب أن يُسجَّل **رقم هاتف المُبلِّغ** مع كل غرض، حتى يُتواصل معه إن ظهر صاحب الغرض.

### المتطلب

| البند | التفصيل |
| --- | --- |
| اسم الحقل | `contact_phone` |
| إلزامي؟ | نعم |
| الصيغة المقبولة | 10 أرقام تبدأ بـ `05` (مثال: `0501234567`) |
| رقم الإصدار الجديد | `1.1.0` |

### ما يجب أن تسلّمه

| # | المهمة | أين |
| --- | --- | --- |
| 1 | مشروع جديد باسم `lost-items` | Azure DevOps |
| 2 | مهمة (Task) بعنوان `Add contact phone to lost item` | Boards |
| 3 | استيراد نسختك من GitHub | Repos |
| 4 | فرع باسم `feature/contact-phone` | Git |
| 5 | تعديل التحقق والحفظ في `app/main.py`، وتغيير الإصدار | الكود |
| 6 | اختباران جديدان على الأقل: رقم ناقص يُرفض، ورقم بصيغة خاطئة يُرفض | `tests/test_app.py` |
| 7 | كل الاختبارات تنجح، و `flake8` لا يطبع شيئًا | Terminal |
| 8 | Commit رسالته تحتوي رقم المهمة `#ID` | Git |
| 9 | طلب دمج (PR) إلى `main` مرتبط بالمهمة، ومعتمد من مراجع، ومدموج بـ Squash | Repos |
| 10 | إصدار بالوسم `v1.1.0` على `main` | Tags |

## قواعد الاختبار

- لا توجد أوامر جاهزة هنا. ارجع لما تعلمته في المعمل الأول.
- اقرأ ناتج كل أمر. رسالة الخطأ جزء من الحل.
- إن فشل اختبار قديم بعد تعديلك فاسأل نفسك: هل الخطأ في كودي أم أن الاختبار القديم لم يعد يناسب المتطلب الجديد؟
- لا تشارك أي **PAT** أو كلمة مرور في لقطة شاشة.

## التحقق النهائي

```bash
python -m pytest -q
python -m flake8 app tests
```

ثم شغّل الخدمة وافتح `/health`، يجب أن ترى `"version": "1.1.0"`:

```bash
python -m app.main
```

---

## English

Hands-on assessment for *DevOps Engineering Fundamentals*. Add a required `contact_phone` field (10 digits starting with `05`) to the lost items service, following the Lab 1 flow: Work item, branch, tests, commit linked to the work item, reviewed PR with squash merge, and tag `v1.1.0`.
