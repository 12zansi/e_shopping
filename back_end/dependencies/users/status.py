

from back_end.Models.status import Status
from back_end.database.tables.tb_order import TBPlaceOrders
from back_end.database.tables.tb_status import TBStatus
from back_end.dependencies.login import UserLogin


class RStatuus(UserLogin):

    def status_add(self,stat : Status, order: TBPlaceOrders):
        query = TBStatus(id = stat.status_id)
        query = TBPlaceOrders(id = stat.status_id)
        RStatuus._add_in_table(self,query)
