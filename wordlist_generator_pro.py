import itertools
import string
import time
from datetime import datetime

def print_banner():
    banner = """
    ╔══════════════════════════════════════════════════════╗
    ║         Wordlist Generator Pro v1.0                  ║
    ║         Coded by Pakistani Ethical Hacker            ║
    ║         Mr. Sabaz Ali Khan                          ║
    ║         Date: {}                            ║
    ╚══════════════════════════════════════════════════════╝
    """.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print(banner)

def get_user_input():
    print("\n[+] Wordlist Generator Configuration")
    print("-" * 40)
    
    min_length = int(input("[*] Enter minimum length of words: "))
    max_length = int(input("[*] Enter maximum length of words: "))
    
    use_lowercase = input("[*] Include lowercase letters? (y/n): ").lower() == 'y'
    use_uppercase = input("[*] Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("[*] Include numbers? (y/n): ").lower() == 'y'
    use_special = input("[*] Include special characters? (y/n): ").lower() == 'y'
    
    custom_chars = input("[*] Enter any custom characters to include (or press Enter): ")
    
    output_file = input("[*] Enter output filename (e.g., wordlist.txt): ")
    
    return {
        'min_length': min_length,
        'max_length': max_length,
        'use_lowercase': use_lowercase,
        'use_uppercase': use_uppercase,
        'use_digits': use_digits,
        'use_special': use_special,
        'custom_chars': custom_chars,
        'output_file': output_file
    }

def generate_charset(config):
    charset = ""
    
    if config['use_lowercase']:
        charset += string.ascii_lowercase
    if config['use_uppercase']:
        charset += string.ascii_uppercase
    if config['use_digits']:
        charset += string.digits
    if config['use_special']:
        charset += string.punctuation
    if config['custom_chars']:
        charset += config['custom_chars']
    
    if not charset:
        print("[!] Error: No character set selected!")
        exit(1)
    
    return charset

def generate_wordlist(config, charset):
    output_file = config['output_file']
    total_combinations = 0
    
    print(f"\n[+] Generating wordlist to {output_file}...")
    print(f"[*] Character set: {charset}")
    
    start_time = time.time()
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for length in range(config['min_length'], config['max_length'] + 1):
            count = 0
            for combination in itertools.product(charset, repeat=length):
                word = ''.join(combination)
                f.write(word + '\n')
                count += 1
                if count % 10000 == 0:
                    print(f"[*] Generated {count} words of length {length}...")
            
            total_combinations += count
    
    end_time = time.time()
    duration = end_time - start_time
    
    print(f"\n[+] Wordlist generation complete!")
    print(f"[*] Total words generated: {total_combinations}")
    print(f"[*] Time taken: {duration:.2f} seconds")
    print(f"[*] Wordlist saved to: {output_file}")

def main():
    print_banner()
    
    try:
        config = get_user_input()
        charset = generate_charset(config)
        generate_wordlist(config, charset)
        
    except KeyboardInterrupt:
        print("\n[!] Process interrupted by user!")
    except Exception as e:
        print(f"\n[!] An error occurred: {str(e)}")

if __name__ == "__main__":
    main()