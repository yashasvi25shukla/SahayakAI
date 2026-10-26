from pathlib import Path

from pypdf import PdfReader
from PIL import Image
import pytesseract


class DocumentProcessingService:

    # --------------------------------------------------
    # MAIN FUNCTION
    # --------------------------------------------------

    def extract_text(self, file_path: str):

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError("Document not found.")

        extension = path.suffix.lower()

        # PDF
        if extension == ".pdf":
            return self._extract_from_pdf(path)

        # IMAGE
        if extension in [".jpg", ".jpeg", ".png", ".webp"]:
            return self._extract_from_image(path)

        raise ValueError(
            "Unsupported document type. "
            "Supported types: PDF, JPG, JPEG, PNG, WEBP."
        )

    # --------------------------------------------------
    # PDF TEXT EXTRACTION
    # --------------------------------------------------

    def _extract_from_pdf(self, path: Path):

        reader = PdfReader(str(path))

        extracted_text = []

        for page_number, page in enumerate(reader.pages, start=1):

            try:
                text = page.extract_text()

                if text:
                    extracted_text.append(
                        f"\n--- Page {page_number} ---\n{text}"
                    )

            except Exception:
                continue

        final_text = "\n".join(extracted_text).strip()

        return {
            "document_type": "pdf",
            "pages": len(reader.pages),
            "text": final_text,
            "text_found": bool(final_text)
        }

    # --------------------------------------------------
    # IMAGE OCR
    # --------------------------------------------------

    def _extract_from_image(self, path: Path):

        image = Image.open(path)

        text = pytesseract.image_to_string(image)

        text = text.strip()

        return {
            "document_type": "image",
            "pages": 1,
            "text": text,
            "text_found": bool(text)
        }


# ------------------------------------------------------
# SINGLE SERVICE INSTANCE
# ------------------------------------------------------

document_processing_service = DocumentProcessingService()