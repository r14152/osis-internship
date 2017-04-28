##############################################################################
#
#    OSIS stands for Open Student Information System. It's an application
#    designed to manage the core business of higher education institutions,
#    such as universities, faculties, institutes and professional schools.
#    The core business involves the administration of students, teachers,
#    courses, programs and so on.
#
#    Copyright (C) 2015-2016 Université catholique de Louvain (http://www.uclouvain.be)
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
from ckeditor.fields import RichTextField
from django.contrib import admin
from django.db import models

from cms.enums.entity_name import ENTITY_NAME
from reference.models.language import Language
from .text_label import TextLabel


class TranslatedTextAdmin(admin.ModelAdmin):
    list_display = ('text_label', 'entity', 'reference', 'language', 'text',)
    ordering = ('text_label',)


class TranslatedText(models.Model):
    language = models.ForeignKey(Language)
    text_label = models.ForeignKey(TextLabel, blank=None, null=True)
    entity = models.CharField(db_index=True, max_length=25, choices=ENTITY_NAME)
    reference = models.IntegerField(db_index=True)
    text = RichTextField(null=True)

    def __str__(self):
        return self.entity


def find_by_id(id):
    return TranslatedText.objects.get(pk=id)