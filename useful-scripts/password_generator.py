"""
Password Generator Script / اسکریپت تولید رمز عبور
--------------------------------------------------
Generate strong, random passwords with various options
تولید رمزهای عبور قوی و تصادفی با گزینه‌های مختلف

Features / ویژگی‌ها:
- Customizable length / طول قابل تنظیم
- Include/exclude character types / شامل/عدم شامل انواع کاراکترها
- Password strength checker / بررسی قدرت رمز عبور
- Generate multiple passwords / تولید چندین رمز عبور
- Save passwords to file (encrypted) / ذخیره رمزها در فایل (رمزگذاری شده)
"""

import random
import string
import argparse
import hashlib
import base64
from pathlib import Path
from datetime import datetime

class PasswordGenerator:
    """
    Password generator class / کلاس تولید رمز عبور
    """
    
    # Character sets / مجموعه کاراکترها
    LOWERCASE = string.ascii_lowercase
    UPPERCASE = string.ascii_uppercase
    DIGITS = string.digits
    SYMBOLS = "!@#$%^&*()_+-=[]{}|;:,.<>?/~"
    
    # Common weak passwords for checking / رمزهای ضعیف رایج برای بررسی
    COMMON_PASSWORDS = {
        'password', '123456', '123456789', 'qwerty', 'abc123',
        'password123', 'admin', 'letmein', 'welcome', 'monkey',
        'dragon', 'master', 'hello', 'freedom', 'whatever'
    }
    
    def __init__(self):
        """Initialize password generator / مقداردهی اولیه تولید رمز عبور"""
        pass
    
    def generate(self, length=16, use_lower=True, use_upper=True, 
                 use_digits=True, use_symbols=True, exclude_similar=False):
        """
        Generate a random password / تولید یک رمز عبور تصادفی
        
        Args:
            length: Password length / طول رمز عبور
            use_lower: Include lowercase letters / شامل حروف کوچک
            use_upper: Include uppercase letters / شامل حروف بزرگ
            use_digits: Include digits / شامل اعداد
            use_symbols: Include symbols / شامل نمادها
            exclude_similar: Exclude similar characters (l1IO0) / حذف کاراکترهای مشابه
        
        Returns:
            str: Generated password / رمز عبور تولید شده
        """
        # Build character pool / ساخت مجموعه کاراکترها
        chars = ''
        if use_lower:
            chars += self.LOWERCASE
        if use_upper:
            chars += self.UPPERCASE
        if use_digits:
            chars += self.DIGITS
        if use_symbols:
            chars += self.SYMBOLS
        
        if not chars:
            raise ValueError("At least one character type must be selected!")
        
        # Remove similar characters if requested / حذف کاراکترهای مشابه در صورت درخواست
        if exclude_similar:
            similar = 'l1IO0'
            chars = ''.join(c for c in chars if c not in similar)
        
        # Ensure password has at least one of each type / اطمینان از وجود حداقل یک از هر نوع
        password = []
        if use_lower:
            password.append(random.choice(self.LOWERCASE))
        if use_upper:
            password.append(random.choice(self.UPPERCASE))
        if use_digits:
            password.append(random.choice(self.DIGITS))
        if use_symbols:
            password.append(random.choice(self.SYMBOLS))
        
        # Fill remaining length / پر کردن طول باقی‌مانده
        remaining = length - len(password)
        for _ in range(remaining):
            password.append(random.choice(chars))
        
        # Shuffle to avoid predictable pattern / مخلوط کردن برای جلوگیری از الگوی قابل پیش‌بینی
        random.shuffle(password)
        
        return ''.join(password)
    
    def generate_multiple(self, count=5, **kwargs):
        """
        Generate multiple passwords / تولید چندین رمز عبور
        """
        return [self.generate(**kwargs) for _ in range(count)]
    
    def check_strength(self, password):
        """
        Check password strength / بررسی قدرت رمز عبور
        
        Returns:
            dict: Strength score and feedback / امتیاز قدرت و بازخورد
        """
        score = 0
        feedback = []
        
        # Length check / بررسی طول
        if len(password) >= 12:
            score += 2
        elif len(password) >= 8:
            score += 1
        else:
            feedback.append("Password is too short (minimum 8 characters)")
        
        # Character diversity / تنوع کاراکترها
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_symbol = any(c in self.SYMBOLS for c in password)
        
        if has_lower and has_upper and has_digit and has_symbol:
            score += 3
        elif has_lower and has_upper and (has_digit or has_symbol):
            score += 2
        elif has_lower and (has_upper or has_digit or has_symbol):
            score += 1
        else:
            feedback.append("Use a mix of character types")
        
        # Check against common passwords / بررسی با رمزهای رایج
        if password.lower() in self.COMMON_PASSWORDS:
            score -= 2
            feedback.append("This is a commonly used password")
        
        # Check for patterns / بررسی الگوها
        if len(set(password)) < len(password) * 0.5:
            score -= 1
            feedback.append("Too many repeated characters")
        
        # Determine strength level / تعیین سطح قدرت
        if score >= 5:
            strength = "Strong"
        elif score >= 3:
            strength = "Medium"
        else:
            strength = "Weak"
        
        return {
            'score': max(0, min(5, score)),
            'strength': strength,
            'feedback': feedback if feedback else ["Good password!"]
        }
    
    def generate_memorable(self, words=3, separator='-', numbers=True):
        """
        Generate a memorable password (passphrase) / تولید رمز عبور به یادماندنی (عبارت رمزی)
        """
        word_list = [
            'apple', 'banana', 'orange', 'grape', 'melon', 'peach',
            'sun', 'moon', 'star', 'cloud', 'rain', 'snow',
            'happy', 'brave', 'calm', 'wise', 'kind', 'bold',
            'tiger', 'lion', 'eagle', 'panda', 'wolf', 'fox',
            'blue', 'red', 'gold', 'silver', 'green', 'purple'
        ]
        
        words_chosen = random.sample(word_list, words)
        password = separator.join(words_chosen)
        
        if numbers:
            password = f"{password}{random.randint(10, 99)}"
        
        return password
    
    def save_passwords(self, passwords, filename='passwords.txt', encrypt=False):
        """
        Save passwords to file / ذخیره رمزها در فایل
        
        Args:
            passwords: List of passwords / لیست رمزهای عبور
            filename: Output filename / نام فایل خروجی
            encrypt: Encrypt the file / رمزگذاری فایل
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        content = f"Generated Passwords - {timestamp}\n"
        content += "=" * 40 + "\n"
        
        for i, pwd in enumerate(passwords, 1):
            content += f"{i}. {pwd}\n"
        
        if encrypt:
            # Simple encryption (base64) - For demo purposes / رمزگذاری ساده - برای نمایش
            encoded = base64.b64encode(content.encode()).decode()
            content = encoded
        
        with open(filename, 'w') as f:
            f.write(content)
        
        print(f"✓ Passwords saved to: {filename}")


def main():
    """
    Command line interface / رابط خط فرمان
    """
    parser = argparse.ArgumentParser(
        description='Generate strong, random passwords'
    )
    parser.add_argument(
        '-l', '--length',
        type=int,
        default=16,
        help='Password length (default: 16)'
    )
    parser.add_argument(
        '-c', '--count',
        type=int,
        default=1,
        help='Number of passwords to generate (default: 1)'
    )
    parser.add_argument(
        '--no-lower',
        action='store_true',
        help='Exclude lowercase letters'
    )
    parser.add_argument(
        '--no-upper',
        action='store_true',
        help='Exclude uppercase letters'
    )
    parser.add_argument(
        '--no-digits',
        action='store_true',
        help='Exclude digits'
    )
    parser.add_argument(
        '--no-symbols',
        action='store_true',
        help='Exclude symbols'
    )
    parser.add_argument(
        '-e', '--exclude-similar',
        action='store_true',
        help='Exclude similar characters (l1IO0)'
    )
    parser.add_argument(
        '-m', '--memorable',
        action='store_true',
        help='Generate memorable password (passphrase)'
    )
    parser.add_argument(
        '-w', '--words',
        type=int,
        default=3,
        help='Number of words for memorable password (default: 3)'
    )
    parser.add_argument(
        '-s', '--save',
        metavar='FILE',
        help='Save passwords to file'
    )
    parser.add_argument(
        '--strength',
        action='store_true',
        help='Check password strength'
    )
    
    args = parser.parse_args()
    
    # Create generator / ایجاد تولیدکننده
    generator = PasswordGenerator()
    
    print("=" * 60)
    print("🔐 PASSWORD GENERATOR / تولید رمز عبور")
    print("=" * 60)
    
    # Generate passwords / تولید رمزها
    if args.memorable:
        # Generate memorable passwords / تولید رمزهای به یادماندنی
        passwords = []
        for _ in range(args.count):
            pwd = generator.generate_memorable(
                words=args.words,
                numbers=not args.no_digits
            )
            passwords.append(pwd)
    else:
        # Generate random passwords / تولید رمزهای تصادفی
        kwargs = {
            'length': args.length,
            'use_lower': not args.no_lower,
            'use_upper': not args.no_upper,
            'use_digits': not args.no_digits,
            'use_symbols': not args.no_symbols,
            'exclude_similar': args.exclude_similar
        }
        
        if args.count == 1:
            passwords = [generator.generate(**kwargs)]
        else:
            passwords = generator.generate_multiple(args.count, **kwargs)
    
    # Display passwords / نمایش رمزها
    print("\n📝 Generated Passwords:")
    for i, pwd in enumerate(passwords, 1):
        print(f"  {i}. {pwd}")
    
    # Check strength if requested / بررسی قدرت در صورت درخواست
    if args.strength and passwords:
        print("\n🔍 Password Strength:")
        for pwd in passwords[:3]:  # Check first 3 passwords
            strength = generator.check_strength(pwd)
            print(f"\n  {pwd}")
            print(f"    Score: {strength['score']}/5")
            print(f"    Strength: {strength['strength']}")
            for msg in strength['feedback']:
                print(f"    • {msg}")
    
    # Save to file if requested / ذخیره در فایل در صورت درخواست
    if args.save:
        generator.save_passwords(passwords, args.save)


if __name__ == "__main__":
    main()

# === Example Usage / مثال استفاده ===
print("\n" + "=" * 60)
print("PASSWORD GENERATOR - EXAMPLES / مثال‌ها")
print("=" * 60)

print("""
🔐 How to use / نحوه استفاده:

1. Generate a strong password (default length 16):
   python password_generator.py

2. Generate 5 passwords:
   python password_generator.py --count 5

3. Generate a 32-character password:
   python password_generator.py --length 32

4. Generate without special characters:
   python password_generator.py --no-symbols

5. Generate memorable password:
   python password_generator.py --memorable --words 4

6. Save to file:
   python password_generator.py --save my_passwords.txt

7. Check password strength:
   python password_generator.py --strength

8. Generate password without similar characters:
   python password_generator.py --exclude-similar

Examples:
  Strong:     "xK9#mP2$vL5@qR8&"
  Memorable:  "apple-moon-brave-42"
  Secure:     "4G!s7F#n8K@qR$mP"
""")
