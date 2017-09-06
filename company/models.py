# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Company(models.Model):
    name = models.TextField()
    sector = models.TextField()
    siren = models.IntegerField(unique=True)

    @property
    def results(self):
        return CompanyResult.objects.filter(company=self)

class CompanyResult(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    ca = models.IntegerField()
    margin = models.IntegerField()
    loss = models.IntegerField()
    ebitda = models.IntegerField()
    date = models.DateField()

    @property
    def has_evolved(self):
        """Search for older instance of CompanyResult of this company. Check if value evolved"""
        if CompanyResult.objects.filter(
            company=self.company,
            date__lt=self.date
        ).exclude(ca=self.ca, margin=self.margin, loss=self.loss, ebitda=self.ebitda):
            return True
        return False

    @property
    def previous(self):
        """Get the previous company result"""
        return CompanyResult.objects.filter(company=self.company, date__lt=self.date).order_by('-date').first()
