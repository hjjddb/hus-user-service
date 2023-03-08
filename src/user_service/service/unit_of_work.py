from __future__ import annotations
import abc

from infrastructures.dependencies import repositories


class AbstractUnitOfWork(abc.ABC):
    repo: repositories.AbstractRepository

    def __init__(self):
        self.session = None

    def __enter__(self) -> AbstractUnitOfWork:
        return self

    def __exit__(self, *args):
        self.rollback()

    def commit(self):
        self._commit()

    def collect_new_events(self):
        for model in self.repo.cache:
            while model.events:
                yield model.events.pop(0)

    @abc.abstractmethod
    def _commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError


class SQLAlchemyUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session_factory):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory
        self.repo = repositories.SQLAlchemyRepository(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def _commit(self):
        self.session.close()

    def rollback(self):
        self.session.rollback()
