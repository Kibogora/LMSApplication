import fastapi

router = fastapi.APIRouter()

# Corrected the path parameter syntax by replacing ":id" with "{id}"
@router.get("/sections/{id}")
async def read_section(id: int):
    return {"courses": []}

# Corrected the path parameter syntax by replacing ":id" with "{id}"
@router.get("/sections/{id}/content-blocks")
async def read_section_content_blocks(id: int):
    return {"courses": []}

# Corrected the path parameter syntax by replacing ":id" with "{id}"
@router.get("/content-blocks/{id}")
async def read_content_block(id: int):
    return {"courses": []}