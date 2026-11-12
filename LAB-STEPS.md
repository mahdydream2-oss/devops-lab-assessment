# الاختبار العملي: خدمة المفقودات

**المطلوب:** إضافة رقم هاتف المُبلِّغ (`contact_phone`) لكل غرض مفقود، ورفع الإصدار إلى `1.1.0`.

**المسار:** مهمة ← فرع ← تعديل ← Commit ← طلب دمج ← إصدار

> الكود جاهز للنسخ. ركّز على أوامر Git وخطوات Azure DevOps.

---

## 1. نسخة المشروع

1. اضغط **Fork** ثم **Create fork**.
2. من نسختك: **Code** ثم **Codespaces** ثم **Create codespace on main**.
3. في الـ Terminal:

```bash
pip install -r requirements.txt
python -m pytest -q
```

✅ النتيجة: `6 passed`

---

## 2. المشروع والمهمة في Azure DevOps

1. افتح **dev.azure.com**، وأنشئ مشروعًا باسم `lost-items` بخصوصية **Private**.
2. **Boards** ثم **Work items** ثم **New Work Item** ثم **Task**.
3. العنوان: `Add contact phone to lost item`، ثم **Save**.
4. دوّن رقم المهمة (**ID**).

---

## 3. المستودع

1. **Repos** ثم **Import a repository**، والصق رابط نسختك على GitHub، ثم **Import**.
2. **Clone** ثم **Generate Git Credentials**، وانسخ كلمة المرور.
3. نفّذ الأوامر التالية كل سطر وحده، واستبدل `ORG` باسم منظمتك:

```bash
cd /workspaces
git config --global credential.helper store
git clone https://ORG@dev.azure.com/ORG/lost-items/_git/lost-items
cd lost-items
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

عند طلب **Password** الصق كلمة المرور.

> ⚠️ أي Terminal جديد يفتح في المجلد الخطأ. اكتب أولًا: `cd /workspaces/lost-items`

---

## 4. الفرع والتعديل

أنشئ فرعًا وافتح ملف البرنامج:

```bash
git checkout -b feature/contact-phone
code app/main.py
```

**أ. غيّر رقم الإصدار:**

```python
APP_VERSION = "1.1.0"
```

**ب. داخل `validate_item`، قبل سطر `return errors`:**

```python
    phone = str(data.get("contact_phone", "")).strip()
    if phone and not (len(phone) == 10 and phone.isdigit() and phone.startswith("05")):
        errors.append("contact_phone must be 10 digits starting with 05")
```

**ج. داخل `create_item`، قبل سطر `"created_at"`:**

```python
        "contact_phone": data.get("contact_phone", "").strip(),
```

احفظ الملف (**Ctrl+S**)، ثم افتح ملف الاختبارات:

```bash
code tests/test_app.py
```

**د. أضف في آخر الملف، بعد سطرين فارغين:**

```python
def test_wrong_phone_format_is_rejected():
    data = {"found_at": "محطة الحافلات", "category": "keys", "contact_phone": "0412345678"}
    assert validate_item(data)
```

احفظ الملف، ثم افحص:

```bash
python -m pytest -q
python -m flake8 app tests
```

✅ النتيجة: `7 passed`، ولا يطبع `flake8` شيئًا.

> ⚠️ انتبه للمسافات في أول السطر: 4 مسافات داخل الدالة، و8 في سطر `"contact_phone"`.

---

## 5. الحفظ والإرسال

استبدل `ID` برقم مهمتك:

```bash
git status
git add .
git commit -m "Add contact phone to lost item #ID"
git push -u origin HEAD
```

---

## 6. طلب الدمج

1. **Repos** ثم **Pull requests** ثم **New pull request**، من `feature/contact-phone` إلى `main`.
2. أضف **Reviewers**، واربط المهمة من **Work items to link**، ثم **Create**.
3. المراجع يضغط **Approve**.
4. اضغط **Complete** واختر **Squash commit**.
5. فعّل **Complete associated work items** و**Delete branch**، ثم **Complete merge**.

---

## 7. الإصدار

```bash
cd /workspaces/lost-items
git checkout main
git pull
git log --oneline -3
git tag -a v1.1.0 -m "Add contact phone"
git push origin v1.1.0
```

✅ النتيجة: في **Repos** ثم **Tags** يظهر `v1.1.0`، والمهمة في **Boards** حالتها **Done**.

---

> 🔒 لا تُظهر أي **PAT** أو كلمة مرور في لقطة شاشة.
