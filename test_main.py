import pytest
from main import normalize_text

test_data = [
    ("𝓣𝓮𝓼𝓽 𝓒𝓪𝓼𝓮", "Test Case"),
    ("𝕋𝕖𝕤𝕥 ℂ𝕒𝕤𝕖", "Test Case"),
    ("Ｔｅｓｔ Ｃａｓｅ", "Test Case"),
    #("ꪻꫀᦓꪻ ᥴꪖᦓꫀ", "test case"),
    ("ᴛᴇꜱᴛ ᴄᴀꜱᴇ", "TET CAE"),
    ("🇹​​🇪​​🇸​​🇹​ 🇨​​🇦​​🇸​​🇪", "TEST CASE"),
    ("T⃞    e⃞    s⃞    t⃞     C⃞    a⃞    s⃞    e⃞", "Test Case"),
    ("🅃🄴🅃 🄲🄰🅅🅃 🄲🄰🅂🄴", "TET CAVT CASE"),
    ("𝗧𝗲𝘀𝘁 𝗖𝗮𝘀𝗲", "Test Case"),
    ("𝐓𝐞𝐬𝐭 𝐂𝐚𝐬𝐞", "Test Case"),
    ("𝙏𝙚𝙨𝙩 𝘾𝙖𝙨𝙚", "Test Case"),
    ("𝘛𝘦𝘴𝘵 𝘊𝘢𝘴𝘦", "Test Case"),
    ("𝚃𝚎𝚚𝚝 𝚂𝚊𝚜𝚎", "Teqt Sase"),
    ("Ｔｅｓｔ　Ｃａｓｅ", "Test Case"),
    ("T̵̰̋͊ȩ̷̨͍̌̈ṣ̶̨̰̂͐͗t̴͓̱̗͌͋ ̵̗̲̌͝c̴̻̭̃a̶͕͕̓s̵̨͛̑e̶͔̲̽́,", "Test case,")]


@pytest.mark.parametrize("input_text, expected_output", test_data)
def test_normalize_text(input_text, expected_output):
    result = normalize_text(input_text)
    assert result == expected_output


if __name__ == "__main":
    pytest.main()