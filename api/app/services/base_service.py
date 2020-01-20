from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from api.app.database.instance import db
from api.base_error import BaseError
from ..utils.paginator import Paginator

class BaseService:
    def __init__(self, model, dto):
        self.model = model
        self.dto = dto

    def list_paginate(page = None, per_page = None):
        return Paginator.paginate(self.model, page, per_page)

    def get_by_id(id):
        model = db.session.query(self.model).get(id)
        return dto.dump(model)
        
    def create(params):
        model_to_save = map(self.model(), params)
        try:
            db.session.add(model_to_save)
            db.session.commit()
            return self.dto.dump(model_to_save)
        except SQLAlchemyError as error:
            raise BaseError(error)

    def edit(id, params):
        model_to_save = db.session.query(self.model).get(id)
        model_to_save = map(model_to_save, params)
        try:
            db.session.add(model_to_save)
            db.session.commit()
            return self.dto.dump(model_to_save)
        except SQLAlchemyError as error:
            raise BaseError(error)

    def delete(id):
        self.model.query.filter_by(id=id).delete()
        db.session.commit()
        return id

    def map(model, dto):
        return model