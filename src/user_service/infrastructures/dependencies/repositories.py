import abc
from typing import Type, Union, List
import sqlalchemy as sql

from domains import models


class AbstractRepository(abc.ABC):
    def __init__(self):
        self.cache = {}

    def add(
        self,
        model: Type[models.Model],
        *args,
        **kwargs,
    ):
        self._add(model)
        model_type = type(model)
        self.cache[model_type][model.id] = model

    def get(
        self,
        model_type: Type[models.Model],
        many: bool = False,
        *args,
        **kwargs,
    ) -> Union[List[Type[models.Model]], Type[models.Model]]:
        result = self._get(*args, **kwargs)
        if result is not None:
            if model_type not in self.cache:
                self.cache[model_type] = {}
            if many:
                for model in result:
                    self.cache[model_type][model.id] = model
            else:
                self.cache[model_type][result.id] = result
        return result

    @abc.abstractmethod
    def _add(
        self,
        model: Type[models.Model],
        *args,
        **kwargs,
    ):
        raise NotImplementedError

    @abc.abstractmethod
    def _get(
        self,
        model_type: Type[models.Model],
        many: bool = False,
        *args,
        **kwargs,
    ) -> Union[List[Type[models.Model]], Type[models.Model]]:
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        super().__init__()
        self.session = session

    def _add(
        self,
        model: Type[models.Model],
        *args,
        **kwargs,
    ):
        self.session.add(model)

    def _get(
        self,
        model_type: Type[models.Model],
        many: bool = False,
        *args,
        **kwargs,
    ) -> Union[List[Type[models.Model]], Type[models.Model]]:
        result = self.session.query(model_type).filter_by(**kwargs)
        if many:
            return result.all()
        return result.first()
