import unicodedata

s = '𝑹𝒐𝒕𝒆𝒎'
s = '𝓗ëⓁ𝕝ᴏ'
from confusables import normalize

def normalize_compatibily(s):
    return unicodedata.normalize('NFKD', s)

def remove_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c).startswith('L'))

print(s)
s = normalize_compatibily(s)
print(s)
s = remove_accents(s)
print(s)
# Test cases
test_cases = [
    ("𝓣𝓮𝓼𝓽 𝓒𝓪𝓼𝓮", "Test Case"),
    ("𝕋𝕖𝕤𝕥 ℂ𝕒𝕤𝕖", "Test Case"),
    ("Ｔｅｓｔ Ｃａｓｅ", "Test Case"),
    ("ꪻꫀᦓꪻ ᥴꪖᦓꫀ", "test case"),
    ("ᴛᴇꜱᴛ ᴄᴀꜱᴇ", "test case"),
    ("🇹​​🇪​​🇸​​🇹​ 🇨​​🇦​​🇸​​🇪", "TEST CASE"),
    ("T⃞    e⃞    s⃞    t⃞     C⃞    a⃞    s⃞    e⃞", "Test Case"),
    ("🅃🄴🅃 🄲🄰🅅🅃 🄲🄰🅂🄴", "TEST CASE"),
    ("𝗧𝗲𝘀𝘁 𝗖𝗮𝘀𝗲", "Test Case"),
    ("𝐓𝐞𝐬𝐭 𝐂𝐚𝐬𝐞", "Test Case"),
    ("𝙏𝙚𝙨𝙩 𝘾𝙖𝙨𝙚", "Test Case"),
    ("𝘛𝘦𝘴𝘵 𝘊𝘢𝘴𝘦", "Test Case"),
    ("𝚃𝚎𝚚𝚝 𝚂𝚊𝚜𝚎", "Test Case"),
    ("Ｔｅｓｔ　Ｃａｓｅ", "Test Case")
]

for text, expected_output in test_cases:
    result = normalize(text, prioritize_alpha=True)
    result = normalize_compatibily(result[0])
    result = remove_accents(result)


    print(f"Original: {text}")
    print(f"Normalized: {result}")
    print(f"Expected: {expected_output}")
    print(f"Pass: {result == expected_output}")
    print()
