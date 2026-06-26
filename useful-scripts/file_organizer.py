"""
File Organizer Script / اسکریپت سازماندهی فایل‌ها
------------------------------------------------
Organizes files in a directory by their extensions
سازماندهی فایل‌ها در یک دایرکتوری بر اساس پسوند آنها

Features / ویژگی‌ها:
- Group files by extension / گروه‌بندی فایل‌ها بر اساس پسوند
- Create folders for each extension / ایجاد پوشه برای هر پسوند
- Move files to appropriate folders / انتقال فایل‌ها به پوشه‌های مناسب
- Handle duplicate file names / مدیریت نام‌های تکراری فایل
- Log operations for tracking / لاگ‌گیری عملیات برای پیگیری
"""

import os
import shutil
from pathlib import Path
from datetime import datetime
import argparse

class FileOrganizer:
    """
    File organizer class / کلاس سازماندهی فایل‌ها
    """
    
    # Default folder structure / ساختار پوشه پیش‌فرض
    EXTENSION_MAP = {
        # Images / تصاویر
        '.jpg': 'Images', '.jpeg': 'Images', '.png': 'Images',
        '.gif': 'Images', '.bmp': 'Images', '.svg': 'Images',
        '.ico': 'Images', '.webp': 'Images',
        
        # Documents / اسناد
        '.pdf': 'Documents', '.doc': 'Documents', '.docx': 'Documents',
        '.txt': 'Documents', '.rtf': 'Documents', '.odt': 'Documents',
        '.xls': 'Documents', '.xlsx': 'Documents', '.ppt': 'Documents',
        '.pptx': 'Documents', '.csv': 'Documents',
        
        # Archives / فایل‌های فشرده
        '.zip': 'Archives', '.rar': 'Archives', '.7z': 'Archives',
        '.tar': 'Archives', '.gz': 'Archives', '.bz2': 'Archives',
        
        # Audio / صوتی
        '.mp3': 'Audio', '.wav': 'Audio', '.flac': 'Audio',
        '.aac': 'Audio', '.ogg': 'Audio', '.wma': 'Audio',
        
        # Video / ویدئویی
        '.mp4': 'Video', '.avi': 'Video', '.mkv': 'Video',
        '.mov': 'Video', '.wmv': 'Video', '.flv': 'Video',
        '.webm': 'Video',
        
        # Code / کد
        '.py': 'Code', '.js': 'Code', '.html': 'Code',
        '.css': 'Code', '.cpp': 'Code', '.java': 'Code',
        '.c': 'Code', '.go': 'Code', '.rs': 'Code',
        '.php': 'Code', '.rb': 'Code', '.json': 'Code',
        '.xml': 'Code', '.yaml': 'Code', '.yml': 'Code',
        
        # Executable / اجرایی
        '.exe': 'Executables', '.msi': 'Executables',
        '.app': 'Executables', '.deb': 'Executables',
        
        # Others / متفرقه
        '.torrent': 'Others', '.log': 'Others',
        '.tmp': 'Others', '.bak': 'Others',
    }
    
    def __init__(self, directory, dry_run=False):
        """
        Initialize file organizer / مقداردهی اولیه سازماندهی فایل‌ها
        
        Args:
            directory: Directory to organize / دایرکتوری مورد نظر
            dry_run: If True, only show what would be done / اگر True، فقط عملیات را نمایش می‌دهد
        """
        self.directory = Path(directory)
        self.dry_run = dry_run
        self.log = []
        self.stats = {
            'total_files': 0,
            'moved_files': 0,
            'created_folders': 0,
            'errors': 0
        }
    
    def log_message(self, message, level='INFO'):
        """
        Log a message / لاگ یک پیام
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] [{level}] {message}"
        self.log.append(log_entry)
        print(log_entry)
    
    def get_extension(self, filename):
        """
        Get file extension / دریافت پسوند فایل
        """
        return filename.suffix.lower()
    
    def get_category(self, extension):
        """
        Get category for extension / دریافت دسته‌بندی برای پسوند
        """
        return self.EXTENSION_MAP.get(extension, 'Others')
    
    def create_folder(self, folder_path):
        """
        Create folder if it doesn't exist / ایجاد پوشه در صورت عدم وجود
        """
        if not folder_path.exists():
            if not self.dry_run:
                folder_path.mkdir(parents=True)
                self.stats['created_folders'] += 1
            self.log_message(f"Creating folder: {folder_path}")
            return True
        return False
    
    def get_unique_filename(self, destination_path):
        """
        Generate unique filename if file exists / ایجاد نام یکتا در صورت وجود فایل
        """
        if not destination_path.exists():
            return destination_path
        
        # Add number to filename / اضافه کردن عدد به نام فایل
        counter = 1
        while True:
            new_path = destination_path.parent / f"{destination_path.stem}_{counter}{destination_path.suffix}"
            if not new_path.exists():
                return new_path
            counter += 1
    
    def organize_files(self):
        """
        Main method to organize files / متد اصلی برای سازماندهی فایل‌ها
        """
        self.log_message("=" * 60)
        self.log_message(f"Starting file organization in: {self.directory}")
        self.log_message(f"Mode: {'DRY RUN' if self.dry_run else 'LIVE'}")
        self.log_message("=" * 60)
        
        # Get all files in directory / دریافت همه فایل‌های دایرکتوری
        files = [f for f in self.directory.iterdir() if f.is_file()]
        self.stats['total_files'] = len(files)
        
        if not files:
            self.log_message("No files found in directory!")
            return
        
        self.log_message(f"Found {len(files)} files to organize")
        
        # Process each file / پردازش هر فایل
        for file_path in files:
            try:
                # Skip system files / رد کردن فایل‌های سیستمی
                if file_path.name.startswith('.'):
                    continue
                
                # Get file extension / دریافت پسوند فایل
                extension = self.get_extension(file_path)
                if not extension:
                    category = 'NoExtension'
                    self.log_message(f"No extension for: {file_path.name}", 'WARNING')
                else:
                    category = self.get_category(extension)
                
                # Create destination folder / ایجاد پوشه مقصد
                dest_folder = self.directory / category
                self.create_folder(dest_folder)
                
                # Create destination path / ایجاد مسیر مقصد
                dest_path = dest_folder / file_path.name
                
                # Handle duplicate filenames / مدیریت نام‌های تکراری
                dest_path = self.get_unique_filename(dest_path)
                
                # Move file / انتقال فایل
                if not self.dry_run:
                    shutil.move(str(file_path), str(dest_path))
                    self.stats['moved_files'] += 1
                
                self.log_message(f"Moved: {file_path.name} -> {category}/{dest_path.name}")
                
            except Exception as e:
                self.stats['errors'] += 1
                self.log_message(f"Error processing {file_path.name}: {str(e)}", 'ERROR')
        
        # Summary / خلاصه
        self.print_summary()
    
    def print_summary(self):
        """
        Print summary of operations / چاپ خلاصه عملیات
        """
        self.log_message("=" * 60)
        self.log_message("SUMMARY / خلاصه")
        self.log_message("=" * 60)
        self.log_message(f"Total files processed: {self.stats['total_files']}")
        self.log_message(f"Files moved: {self.stats['moved_files']}")
        self.log_message(f"Folders created: {self.stats['created_folders']}")
        self.log_message(f"Errors: {self.stats['errors']}")
        
        if self.dry_run:
            self.log_message("\n⚠️  This was a DRY RUN. No files were actually moved.")
            self.log_message("   Remove --dry-run flag to perform actual operation.")
    
    def save_log(self, log_file='organization_log.txt'):
        """
        Save log to file / ذخیره لاگ در فایل
        """
        log_path = self.directory / log_file
        with open(log_path, 'w') as f:
            f.write('\n'.join(self.log))
        print(f"\n📋 Log saved to: {log_path}")


def main():
    """
    Command line interface / رابط خط فرمان
    """
    parser = argparse.ArgumentParser(
        description='Organize files by extension into folders'
    )
    parser.add_argument(
        'directory',
        nargs='?',
        default='.',
        help='Directory to organize (default: current directory)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be done without actually doing it'
    )
    parser.add_argument(
        '--log',
        action='store_true',
        help='Save log to file'
    )
    
    args = parser.parse_args()
    
    # Create organizer / ایجاد سازماندهی
    organizer = FileOrganizer(args.directory, args.dry_run)
    
    # Organize files / سازماندهی فایل‌ها
    organizer.organize_files()
    
    # Save log if requested / ذخیره لاگ در صورت درخواست
    if args.log:
        organizer.save_log()


if __name__ == "__main__":
    main()

# === Example Usage / مثال استفاده ===
print("\n" + "=" * 60)
print("FILE ORGANIZER - EXAMPLES / مثال‌ها")
print("=" * 60)

print("""
📁 How to use / نحوه استفاده:

1. Organize current directory (dry run):
   python file_organizer.py --dry-run

2. Organize a specific directory:
   python file_organizer.py /path/to/directory

3. Organize with logging:
   python file_organizer.py /path/to/directory --log

4. Organize current directory (live):
   python file_organizer.py

Example structure before:
📁 MyDownloads/
  ├── image1.jpg
  ├── document.pdf
  ├── song.mp3
  └── script.py

After organization:
📁 MyDownloads/
  ├── Images/
  │   └── image1.jpg
  ├── Documents/
  │   └── document.pdf
  ├── Audio/
  │   └── song.mp3
  └── Code/
      └── script.py
""")
