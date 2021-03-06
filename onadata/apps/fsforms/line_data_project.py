import datetime
from collections import OrderedDict

from django.db.models import Count

from .models import FInstance


class LineChartGenerator(object):

    def __init__(self, project):
        self.project = project

    def get_count(self, date):
        return self.project.project_instances.filter(date__contains=date.date()).count()

    def data(self):
        d = OrderedDict()
        dt = [(datetime.datetime.today() - datetime.timedelta(days=x)) for x in range(0,30)]
        dt = dt[::-1]
        for date in dt:
            count = self.get_count(date)
            d[date.date().strftime('%Y-%m-%d')] = count
        return d


class LineChartGeneratorOrganization(object):

    def __init__(self, organization):
        self.organization = organization

    def get_count(self, date):
        return FInstance.objects.filter(project__organization=self.organization, date__contains=date.date()).count()

    def data(self):
        d = OrderedDict()
        dt = [(datetime.datetime.today() - datetime.timedelta(days=x)) for x in range(0,30)]
        dt = dt[::-1]
        for date in dt:
            count = self.get_count(date)
            d[date.date().strftime('%Y-%m-%d')] = count
        return d


class LineChartGeneratorSite(object):

    def __init__(self, site):
        self.site = site

    def get_count(self, date):
        return self.site.site_instances.filter(date__contains=date.date()).count()

    def data(self):
        d = OrderedDict()
        dt = [(datetime.datetime.today() - datetime.timedelta(days=x)) for x in range(0,30)]
        dt = dt[::-1]
        for date in dt:
            count = self.get_count(date)
            d[date.date().strftime('%Y-%m-%d')] = count
        return d


