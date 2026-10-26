from fastapi import APIRouter, UploadFile, File, HTTPException

from app.services.document_service import DocumentService


router = APIRouter()

document_service = DocumentService()


@router.post("/")
async def upload_document(
    file: UploadFile = File(...)
):

    # -----------------------------------------
    # Check filename
    # -----------------------------------------

    if not file.filename:

        raise HTTPException(
            status_code=400,
            detail="No file selected."
        )

    # -----------------------------------------
    # Read file
    # -----------------------------------------

    file_content = await file.read()

    file_size = len(file_content)

    # -----------------------------------------
    # Validate file
    # -----------------------------------------

    validation = document_service.validate_file(
        file.filename,
        file_size
    )

    if not validation["valid"]:

        raise HTTPException(
            status_code=400,
            detail=validation["message"]
        )

    # -----------------------------------------
    # Generate safe unique filename
    # -----------------------------------------

    saved_filename = document_service.generate_filename(
        file.filename
    )

    file_path = document_service.get_upload_path(
        saved_filename
    )

    # -----------------------------------------
    # Save file
    # -----------------------------------------

    with open(file_path, "wb") as saved_file:

        saved_file.write(file_content)

    # -----------------------------------------
    # Response
    # -----------------------------------------

    return {

        "success": True,

        "message": "Document uploaded successfully.",

        "document": {

            "original_filename": file.filename,

            "stored_filename": saved_filename,

            "file_type": file.content_type,

            "file_size": file_size,

            "status": "uploaded"

        }

    }