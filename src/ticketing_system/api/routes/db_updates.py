from fastapi import APIRouter, Request, HTTPException
from bson import ObjectId
from .. import utils
from .. import webhooks
import traceback

router = APIRouter(prefix="/api")
db = utils.get_db_client()


@router.get("/update/issue/updatefields")
async def update_id_fields():
    update_fields = db.issues.find({"playerData.id": {"$exists": True}}, {"modlogs": 0})
    return utils.prepare_json(update_fields)


@router.get("/update/issue/putprojectonissues")
async def update_all_issues_to_include_project():
    db.issues.update_many(
        {}, {"$set": {"project_id": ObjectId("63fe47296edfc3b387628861")}}
    )
    return "done"


@router.get("/update/issue/idtodiscordid")
async def update_all_issues_to_discord_id():
    db.issues.updateMany({}, {"$rename": {"playerData.id": "playerData.discord_id"}})


@router.get("/update/addblacklistfield")
async def update_all_users_to_include_ban_field():
    db.users.update_many({}, {"$set": {"banned": False}})
