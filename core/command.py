import json
from core.actions import (
    list_files,
    move_file,
    copy_file,
    delete_file,
    compress_folder,
    convert_pdf_to_docx,
    search_file,
    get_size,
    cleanup_old_files,
    create_structure_from_text,
    generate_structure,
    create_file,
    change_directory,
    get_current_dir
)
from core import actions 
def parse_command(raw):
    if not raw.strip():
        raise ValueError("LLM response is empty.")
    try:
        data = json.loads(raw)
        return data if isinstance(data, list) else [data]
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON from LLM: {e}")

def route_command(cmd):
    """
    Routes the command to the appropriate function based on the action.
    """
    action = cmd["action"].strip().lower()
    args = cmd["args"]

    print(f"🧪 DEBUG: action='{action}', args={args}")

    match action:
        case "list_files":
            return list_files(**args)
        case "get_current_dir":
            return get_current_dir()
        case "move_file":
            return move_file(**args)
        case "copy_file":
            return copy_file(**args)
        case "delete_file":
            return delete_file(**args)
        case "create_file":
            return create_file(**args)
        case "compress_folder":
            return compress_folder(**args)
        case "convert_file":
            return convert_pdf_to_docx(**args)
        case "search_file":
            return search_file(**args)
        case "cd":
            return actions.change_directory(**args)
        case "get_size":
            return get_size(**args)
        case "cleanup_old_files":
            return cleanup_old_files(**args)
        case "create_structure_from_text":
            return create_structure_from_text(**args)
        case "generate_structure":
            return generate_structure(**args)
        case _:
            return f"❓ Unknown command: '{action}'"
