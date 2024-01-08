from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from app import models, schemas, utils
from app.database import get_db

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.CreateUser, db: Session = Depends(get_db)):
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    validate_email = utils.email_validation(user.email)

    if validate_email.get("deliverability") == "DELIVERABLE":
        new_user = models.User(**user.model_dump())
        print(new_user)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Email: {user.email} is not valid. Powered by AbstractAPI (https://www.abstractapi.com/)",
        )


@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id: {id} does not exist",
        )

    return user
