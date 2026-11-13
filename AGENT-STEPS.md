# الاختبار العملي 2: الوكيل والـ Pipeline (خدمة المفقودات)

**المطلوب:** تشغيل الاختبارات تلقائيًا مع كل تعديل، على وكيل (Agent) خاص بك يعمل داخل Codespace.

**نقطة البداية:** انتهيت من الاختبار الأول، و`main` في Azure فيه الإصدار `v1.1.0`.

**المسار:** PAT ← تشغيل الوكيل ← إنشاء الـ Pipeline ← تشغيل أخضر ← كسر الاختبار (أحمر) ← إصلاحه (أخضر)

---

## 1. إنشاء PAT

الـ PAT مفتاح مؤقت يسمح للوكيل بالاتصال بمنظمتك.

1. في Azure DevOps اضغط أيقونة **User settings** أعلى يمين الصفحة، ثم **Personal access tokens**.
2. اضغط **New Token**.
3. **Name:** `agent`، و**Expiration:** 7 days.
4. **Scopes:** اختر **Custom defined**، ثم **Show all scopes**، ثم **Agent Pools: Read & manage**.
5. اضغط **Create**، وانسخ الـ Token واحفظه. لن يظهر مرة أخرى.

> 🔒 لا تُظهر الـ PAT في أي لقطة شاشة، ولا ترسله لأحد.

---

## 2. تحديث المستودع في Codespace

نتأكد أن ملفَي الوكيل والـ Pipeline موجودان في نسختك على Azure:

```bash
cd /workspaces/lost-items
git checkout main
git pull
ls scripts azure-pipelines.yml
```

✅ النتيجة: يظهر `setup-agent.sh` و`azure-pipelines.yml`.

> إن لم يظهرا: نسختك قديمة. افتح الـ Fork على GitHub واضغط **Sync fork**، ثم في Azure: **Repos** ثم **Files** ثم القائمة **⋮** ثم **Import repository** من جديد. أو اطلب المساعدة من المدرب.

---

## 3. تشغيل الوكيل

افتح Terminal جديدًا خاصًا بالوكيل، واستبدل `ORG` باسم منظمتك و`PAT` بالمفتاح:

```bash
cd /workspaces/lost-items
bash scripts/setup-agent.sh https://dev.azure.com/ORG PAT
```

| الجزء | معناه |
| --- | --- |
| `bash scripts/setup-agent.sh` | يشغّل سكربت التثبيت |
| `https://dev.azure.com/ORG` | رابط منظمتك، ليعرف الوكيل لمن يعمل |
| `PAT` | المفتاح الذي أنشأته في الخطوة 1 |

✅ النتيجة: `Listening for Jobs`

> ⚠️ إن ظهر `Agent is running` ثم خطأ اتصال، فهناك وكيل قديم من معمل سابق في نفس الـ Codespace. احذفه ثم أعد الأمر:
> ```bash
> rm -rf ~/azagent
> ```

> ⚠️ اترك هذا الـ Terminal مفتوحًا طوال المعمل. إغلاقه يوقف الوكيل. للأوامر الأخرى افتح Terminal جديدًا بعلامة **+**.

**تحقق في Azure:** **Project settings** ثم **Agent pools** ثم **Default** ثم **Agents**. يجب أن يظهر وكيلك وحالته **Online**.

---

## 4. إنشاء الـ Pipeline

1. **Pipelines** ثم **New pipeline**.
2. **Azure Repos Git**، ثم اختر المستودع `lost-items`.
3. **Existing Azure Pipelines YAML file**.
4. **Branch:** `main`، و**Path:** `/azure-pipelines.yml`، ثم **Continue**.
5. اضغط **Run**.
6. إن توقف أول تشغيل وظهرت رسالة **needs permission**: اضغط **View** ثم **Permit** ثم **Permit**. إن لم تظهر فتابع.
7. إن بقي التشغيل على **Queued** أكثر من دقيقة: تأكد أن Terminal الوكيل ما زال مفتوحًا ويعرض `Listening for Jobs`.

✅ النتيجة: التشغيل **أخضر**، وتبويب **Tests** فيه 7 اختبارات ناجحة.

**ماذا يفعل الـ Pipeline؟**

| الخطوة | ماذا تفعل |
| --- | --- |
| Install dependencies | تثبّت المكتبات |
| Lint (code quality) | تفحص طريقة كتابة الكود بـ `flake8` |
| Run tests | تشغّل الاختبارات |
| Publish test results | تعرض النتائج في تبويب **Tests** |

---

## 5. الأحمر: كسر اختبار عمدًا

نثبت أن الـ Pipeline يكتشف الخطأ تلقائيًا. في Terminal جديد:

```bash
cd /workspaces/lost-items
code tests/test_app.py
```

في الاختبار `test_create_and_list_item` غيّر الرقم في السطر الأخير من `1` إلى `99`:

```python
    assert client.get("/api/items").get_json()[0]["id"] == 99
```

احفظ الملف، ثم:

```bash
git add .
git commit -m "Break a test on purpose"
git push
```

✅ النتيجة: في **Pipelines** يبدأ تشغيل جديد تلقائيًا، ويتحول **أحمر** عند خطوة **Run tests**، ويظهر في **Tests** اختبار فاشل واحد.

---

## 6. الأخضر: الإصلاح

أرجع الرقم إلى `1`:

```python
    assert client.get("/api/items").get_json()[0]["id"] == 1
```

احفظ الملف، ثم:

```bash
git add .
git commit -m "Fix the broken test"
git push
```

✅ النتيجة: تشغيل جديد **أخضر**، و7 اختبارات ناجحة.

---

## 7. الإنهاء

1. في Terminal الوكيل اضغط **Ctrl+C** لإيقافه.
2. في **Agent pools** ثم **Default** ثم **Agents**، احذف وكيلك.
3. في **Personal access tokens** اضغط **Revoke** على الـ PAT.

---

## ما يجب أن يراه المدرب

| البند | أين |
| --- | --- |
| الوكيل ظهر **Online** | Agent pools ثم Default |
| تشغيل أخضر ثم أحمر ثم أخضر | Pipelines ثم Runs |
| تبويب Tests فيه 7 اختبارات | آخر تشغيل |
