# كود التعديل: رقم هاتف المُبلِّغ

## الملف الأول: `app/main.py`

**1. رقم الإصدار:**

```python
APP_VERSION = "1.1.0"
```

**2. داخل `validate_item`، قبل سطر `return errors`:**

```python
    phone = str(data.get("contact_phone", "")).strip()
    if phone and not (len(phone) == 10 and phone.isdigit() and phone.startswith("05")):
        errors.append("contact_phone must be 10 digits starting with 05")
```

**3. داخل `create_item`، قبل سطر `"created_at"`:**

```python
        "contact_phone": data.get("contact_phone", "").strip(),
```

## الملف الثاني: `tests/test_app.py`

**في آخر الملف، بعد سطرين فارغين:**

```python
def test_wrong_phone_format_is_rejected():
    data = {"found_at": "محطة الحافلات", "category": "keys", "contact_phone": "0412345678"}
    assert validate_item(data)
```

> انتبه للمسافات في أول السطر: 4 مسافات داخل الدالة، و8 في سطر `"contact_phone"`.
