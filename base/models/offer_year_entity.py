##############################################################################
#
#    OSIS stands for Open Student Information System. It's an application
#    designed to manage the core business of higher education institutions,
#    such as universities, faculties, institutes and professional schools.
#    The core business involves the administration of students, teachers,
#    courses, programs and so on.
#
#    Copyright (C) 2015-2017 Université catholique de Louvain (http://www.uclouvain.be)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    A copy of this license - GNU General Public License - is available
#    at the root of the source code of this program.  If not,
#    see http://www.gnu.org/licenses/.
#
##############################################################################
from django.contrib import admin
from base.models.enums import offer_year_entity_type
from django.db import models


class OfferYearEntityAdmin(admin.ModelAdmin):
    list_display = ('offer_year', 'entity', 'type',)
    fieldsets = ((None, {'fields': ('offer_year', 'entity', 'type')}),)
    search_fields = ['type', 'entity__entityversion__acronym', 'offer_year__acronym']
    list_filter = ('type', 'offer_year__academic_year',)


class OfferYearEntity(models.Model):
    external_id = models.CharField(max_length=100, blank=True, null=True)
    changed = models.DateTimeField(null=True, auto_now=True)
    offer_year = models.ForeignKey('OfferYear')
    entity = models.ForeignKey('Entity')
    type = models.CharField(max_length=30, blank=True, null=True, choices=offer_year_entity_type.TYPES)

    class Meta:
        unique_together = ('offer_year', 'type')

    def __str__(self):
        return u"%s - %s - %s" % (self.offer_year, self.entity, self.type)


def search(**kwargs):
    queryset = OfferYearEntity.objects

    if 'entity' in kwargs:
        queryset = queryset.filter(entity__exact=kwargs['entity'])

    if 'offer_year' in kwargs:
        queryset = queryset.filter(offer_year=kwargs['offer_year'])

    if 'type' in kwargs:
        queryset = queryset.filter(type__exact=kwargs['type'])

    return queryset


def get_from_offer_year_and_type(offer_year, type):
    return OfferYearEntity.objects.get(offer_year=offer_year, type=type)
