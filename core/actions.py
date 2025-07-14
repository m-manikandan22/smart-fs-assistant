import os, shutil, zipfile, time
from pdf2docx import Converter
from config.settings import DEFAULT_BASE_PATH

# Global current directory tracker (default starts here)
current_dir = ["/home/manikandan"]

def list_files(folder=None, extension=None, recursive=False):
    """
    Shows only the files and folders directly inside `folder` (like `ls`).
    Ignores subfolders completely, even if `recursive=True`.
    """
    folder = folder or current_dir[0]  # Fallback to current_dir
    if not os.path.isdir(folder):
        return f"❌ Folder not found: {folder}"

    items = []

    for item in os.listdir(folder):
        item_path = os.path.join(folder, item)
        if os.path.isfile(item_path):
            if not extension or item.lower().endswith(extension.lower()):
                items.append(item)
        elif os.path.isdir(item_path):
            items.append(item + "/")

    return "\n".join(sorted(items)) if items else "📁 No files or folders found."

def move_file(src, dst):
    try:
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.move(src, dst)
        return f"✅ Moved: {src} → {dst}"
    except Exception as e:
        return f"❌ Move error: {str(e)}"

def copy_file(src, dst):
    try:
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
        return f"✅ Copied: {src} → {dst}"
    except Exception as e:
        return f"❌ Copy error: {str(e)}"
 

def change_directory(path):
    # Resolve relative to current_dir if path is not absolute
    if not os.path.isabs(path):
        path = os.path.join(current_dir[0], path)

    if not os.path.isdir(path):
        return f"❌ Directory does not exist: {path}"

    current_dir[0] = os.path.abspath(path)
    return f"✅ Current directory changed to: {current_dir[0]}"

def delete_file(path):
    try:
        os.remove(path)
        return f"🗑️ Deleted: {path}"
    except Exception as e:
        return f"❌ Delete error: {str(e)}"

def compress_folder(src, zip_name):
    try:
        with zipfile.ZipFile(zip_name, 'w') as zipf:
            for root, _, fs in os.walk(src):
                for f in fs:
                    path = os.path.join(root, f)
                    zipf.write(path, os.path.relpath(path, src))
        return f"📦 Compressed: {src} → {zip_name}"
    except Exception as e:
        return f"❌ Compression error: {str(e)}"

def convert_pdf_to_docx(src, tgt):
    try:
        cv = Converter(src)
        cv.convert(tgt)
        cv.close()
        return f"🔄 Converted: {src} → {tgt}"
    except Exception as e:
        return f"❌ Conversion error: {str(e)}"

def search_file(filename, folder=None):
    folder = folder or current_dir[0]  # Use current_dir if folder not provided

    if not os.path.isdir(folder):
        return f"❌ Folder not found: {folder}"

    for root, _, fs in os.walk(folder):
        if filename in fs:
            return f"🔍 Found: {os.path.join(root, filename)}"

    return f"❌ File not found: {filename}"

def get_current_dir():
    return f"📂 Current directory: {current_dir[0]}"


def get_size(path):
    try:
        size = os.path.getsize(path) / 1024
        return f"📏 Size of {path}: {size:.2f} KB"
    except Exception as e:
        return f"❌ Size check error: {str(e)}"

def cleanup_old_files(folder, days):
    try:
        now = time.time()
        days = int(days)
        removed = []
        for root, _, fs in os.walk(folder):
            for f in fs:
                fp = os.path.join(root, f)
                if (now - os.path.getmtime(fp)) > days * 86400:
                    os.remove(fp)
                    removed.append(fp)
        return f"🧹 Removed {len(removed)} old files:\n" + "\n".join(removed) if removed else "No old files found."
    except Exception as e:
        return f"❌ Cleanup error: {str(e)}"
from core.actions import current_dir

def create_structure_from_text(base_path, text):
    try:
        # ✅ Fallback to current_dir if base_path is None
        base_path = base_path or current_dir[0]

        for line in text.splitlines():
            line = line.strip("│├─ ")
            if not line:
                continue
            if line.endswith("/"):
                os.makedirs(os.path.join(base_path, line), exist_ok=True)
            else:
                path = os.path.join(base_path, line)
                os.makedirs(os.path.dirname(path), exist_ok=True)
                open(path, "a").close()

        return f"🏗️ Structure created at {base_path}"
    except Exception as e:
        return f"❌ Structure creation failed: {str(e)}"


from core.actions import current_dir

def generate_structure(base_path, text):
    try:
        # Default to current directory if not provided
        base_path = base_path or current_dir[0]

        for line in text.splitlines():
            line = line.strip("│├─ ")
            if not line:
                continue

            if line.endswith("/"):
                os.makedirs(os.path.join(base_path, line), exist_ok=True)
            else:
                path = os.path.join(base_path, line)
                os.makedirs(os.path.dirname(path), exist_ok=True)
                open(path, "a").close()

        return f"🏗️ Structure created at {base_path}"
    except Exception as e:
        return f"❌ Structure creation failed: {str(e)}"

def create_file(path, content=""):
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"✅ File created: {path}"
    except Exception as e:
        return f"❌ File creation failed: {str(e)}"

def create_folder(path):
    try:
        os.makedirs(path, exist_ok=True)
        return f"📁 Folder created: {path}"
    except Exception as e:
        return f"❌ Folder creation failed: {str(e)}"
