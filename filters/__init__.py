from loader import dp
from .admin import AdminFilter
from .privatChat import isPrivate
from .group import isGroup


if __name__ == "filters":
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(isPrivate)
    dp.filters_factory.bind(isGroup)
