# import django_tables2 as tables
# import itertools
# from .models import RosesBouquets, OtherFlowers
# from django.utils.html import format_html


# class FlowersTable(tables.Table):
#     name = tables.Column(attrs={
#         "td": {
#             'data-name': data_name
#         }
#     })
#     price = tables.Column(attrs={
#         "td": {
#             'data-price': data_price
#         }
#     })
#     image = tables.Column(attrs={
#         "td": {
#             'data-image': data_image
#         }
#     })
#     # attrs = {
#     #     "td": {
#     #         "data-first-name": lambda record: record.first_name
#     #         "data-last-name": lambda record: record.last_name
#     #     }
#     # }
#     def render(self, record):
#         return "{} {}".format(record.first_name, record.last_name)

# class Table(tables.Table):
#     person = PersonColumn()

#     # def __init__(self, *args, **kwargs):
#     #     super().__init__(*args, **kwargs)
#     #     self.counter = itertools.count()
    
#     # def render_row_number(self):
#     #     return 'Row %d' % next(self.counter)

#     # def render_id(self, value):
#     #     return "<%s>" % value