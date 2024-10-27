# FastAPI OAuth2

## Model
Bu kod `username` degan o'zgaruvchiga `str` yoki `None` qiymatlarini qabul qilish imkonini beradi. Keling, detallab tushuntirib beraman:

```python
username: str or None = None
```
Bu yerdagi koddagi har bir qismning ma'nosi:

- username: O'zgaruvchi nomi.
- `: str or None`: Bu "type hint" bo'lib, username o'zgaruvchisi str (string, ya'ni matn) yoki None qiymatini qabul qilishini bildiradi. str - matnni ifodalaydi, None esa qiymatning bo'sh yoki mavjud emasligini bildiradi.
- `= None`: O'zgaruvchiga boshlang'ich qiymat sifatida None berilmoqda. Bu shuni anglatadiki, dastur ishga tushganda username o'zgaruvchisi None qiymatiga ega bo'ladi va agar kerak bo'lsa, keyinroq str tipidagi qiymat bilan yangilanishi mumkin.
Qisqacha, bu kodda username o'zgaruvchisi boshida None qiymatiga ega bo'lib, agar kerak bo'lsa, matn (str) qiymat bilan almashtirilishi mumkin.

## Secret ket generate
```bash
# openssl rand - hex 32
```

## get password hash
```python
pwd = get_password_hash('mrx1234')
print(pwd)
```