from pathlib import Path
from uuid import uuid4


class DocumentService:

    # Allowed document types
    ALLOWED_EXTENSIONS = {
        ".pdf",
        ".jpg",
        ".jpeg",
        ".png"
    }

    # Maximum file size: 5 MB
    MAX_FILE_SIZE = 5 * 1024 * 1024

    # Folder where documents are temporarily stored
    UPLOAD_DIR = (
        Path(__file__).resolve().parent.parent.parent
        / "uploads"
    )

    def __init__(self):

        self.UPLOAD_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

    def validate_file(self, filename, file_size):

        extension = Path(filename).suffix.lower()

        # Check extension
        if extension not in self.ALLOWED_EXTENSIONS:

            return {
                "valid": False,
                "message": (
                    "Unsupported document type. "
                    "Allowed types: PDF, JPG, JPEG, PNG."
                )
            }

        # Check size
        if file_size > self.MAX_FILE_SIZE:

            return {
                "valid": False,
                "message": "File size must not exceed 5 MB."
            }

        return {
            "valid": True,
            "message": "File is valid."
        }

    def generate_filename(self, original_filename):

        extension = Path(original_filename).suffix.lower()

        unique_name = f"{uuid4().hex}{extension}"

        return unique_name

    def get_upload_path(self, filename):

        return self.UPLOAD_DIR / filename