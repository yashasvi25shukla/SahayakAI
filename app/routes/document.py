from fastapi import APIRouter, HTTPException

from app.services.document_processing_service import (
    document_processing_service
)

router = APIRouter()


@router.post("/extract-text")
def extract_document_text(file_path: str):

    try:

        result = document_processing_service.extract_text(
            file_path
        )

        return {
            "success": True,
            "message": "Document text extracted successfully.",
            "document": result
        }

    except FileNotFoundError as error:

        raise HTTPException(
            status_code=404,
            detail=str(error)
        )

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=f"Document processing failed: {str(error)}"
        )